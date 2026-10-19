"""Exercise Quizdown's rendered public contract with current Quarto APIs."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/quizdown-m1-m2"
QUARTO = os.environ.get("QUIZDOWN_QUARTO") or shutil.which("quarto")


def isolated_environment(project: Path) -> dict[str, str]:
    environment = {
        key: value
        for key, value in os.environ.items()
        if key not in {"GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR"}
    }
    environment["GIT_CEILING_DIRECTORIES"] = str(project.parent)
    guard = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=project,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    assert guard.returncode == 128, guard.stdout + guard.stderr
    return environment


def render_fixture(tmp_path: Path, name: str, source: Path | None = None) -> Path:
    if not QUARTO:
        pytest.skip("Quarto is not installed")

    project = tmp_path / "quizdown-project"
    (project / "_extensions/parmsam").mkdir(parents=True)
    shutil.copytree(
        ROOT / "_extensions/parmsam/quizdown", project / "_extensions/parmsam/quizdown"
    )
    shutil.copy(source or FIXTURES / name, project / name)
    (project / "_quarto.yml").write_text(
        "project:\n  type: default\nformat: html\nfilters:\n  - quizdown\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [
            str(QUARTO),
            "render",
            name,
            "--lua-filter",
            "_extensions/parmsam/quizdown/quizdown.lua",
        ],
        cwd=project,
        env=isolated_environment(project),
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return project / Path(name).with_suffix(".html")


def test_fenced_div_quiz_preserves_markdown_answers_and_scripts(tmp_path: Path):
    html = render_fixture(tmp_path, "div-quiz.qmd").read_text(encoding="utf-8")

    assert 'class="quizdown"' in html
    assert "quizdown-init.js" in html
    # The raw host must contain Quizdown's Markdown payload, not Quarto-rendered
    # checkboxes. Escaping preserves literal type reprs for browser textContent.
    assert "&lt;class 'int'&gt;" in html
    assert '<input type="checkbox"' not in html
    assert "some_value" in html


def test_fenced_div_preserves_literals_inside_code_blocks(tmp_path: Path):
    html = render_fixture(tmp_path, "div-quiz.qmd").read_text(encoding="utf-8")
    assert 'print("{=html}")' in html
    assert 'print("&lt;code&gt;literal&lt;/code&gt;")' in html


def test_legacy_fenced_code_block_keeps_its_quiz_host(tmp_path: Path):
    html = render_fixture(tmp_path, "legacy-quiz.qmd").read_text(encoding="utf-8")

    assert 'class="quizdown"' in html
    assert "Legacy question" in html
    assert "quizdown-init.js" in html


def quiz_answers(source: Path):
    import re

    text = source.read_text(encoding="utf-8")
    result = []
    for block in re.split(r"^### ", text, flags=re.MULTILINE)[1:]:
        options = re.findall(r"^- \[([ x])\] (.+)$", block, re.MULTILINE)
        result.append(
            {
                "title": block.splitlines()[0].replace("`", ""),
                "answers": [
                    re.sub(r"</?code>", "", label).replace("`", "")
                    for _, label in options
                ],
                "correct": [
                    re.sub(r"</?code>", "", label).replace("`", "")
                    for mark, label in options
                    if mark == "x"
                ],
            }
        )
    return result


def test_other_quiz_banks_mount_without_page_errors(tmp_path: Path):
    if not QUARTO:
        pytest.skip("Quarto is not installed")
    playwright = os.environ.get("PLAYWRIGHT_MODULE")
    browser = os.environ.get("PLAYWRIGHT_BROWSER")
    if not playwright or not browser:
        pytest.skip("PLAYWRIGHT_MODULE and PLAYWRIGHT_BROWSER are required")

    project = tmp_path / "quizdown-banks"
    (project / "_extensions/parmsam").mkdir(parents=True)
    shutil.copytree(
        ROOT / "_extensions/parmsam/quizdown", project / "_extensions/parmsam/quizdown"
    )
    (project / "_quarto.yml").write_text(
        "project:\n  type: default\nformat: html\nfilters:\n  - quizdown\n",
        encoding="utf-8",
    )
    sources = [
        ROOT / "quizzes" / f"quiz-modulo-{number:02}.qmd"
        for number in [1, *range(3, 11)]
    ]
    sources.append(ROOT / "quizzes/quiz-anexo-git-github.qmd")
    for source in sources:
        shutil.copy(source, project / source.name)
    for source in sources:
        result = subprocess.run(
            [
                str(QUARTO),
                "render",
                source.name,
                "--lua-filter",
                "_extensions/parmsam/quizdown/quizdown.lua",
            ],
            cwd=project,
            env=isolated_environment(project),
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
    pages = [source.with_suffix(".html").name for source in sources]
    pages_path = tmp_path / "pages.json"
    pages_path.write_text(__import__("json").dumps(pages), encoding="utf-8")
    browser_result = subprocess.run(
        [
            "node",
            str(FIXTURES / "mount-check.cjs"),
            playwright,
            str(project),
            str(pages_path),
            browser,
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert browser_result.returncode == 0, browser_result.stderr


def test_module_two_quiz_is_browser_interactive(tmp_path: Path):
    playwright = os.environ.get("PLAYWRIGHT_MODULE")
    browser = os.environ.get("PLAYWRIGHT_BROWSER")
    if not playwright or not browser:
        pytest.skip("PLAYWRIGHT_MODULE and PLAYWRIGHT_BROWSER are required")

    source = ROOT / "quizzes/quiz-modulo-02.qmd"
    html = render_fixture(tmp_path, "quiz.qmd", source)
    expected = quiz_answers(source)
    expected_path = tmp_path / "expected.json"
    expected_path.write_text(__import__("json").dumps(expected), encoding="utf-8")
    result = subprocess.run(
        [
            "node",
            str(FIXTURES / "browser-check.cjs"),
            playwright,
            str(html.parent),
            str(expected_path),
            browser,
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
