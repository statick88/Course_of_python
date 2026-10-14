"""Pin the course render scope and the single production deployment path."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def config(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def chapter_paths(entries):
    for entry in entries:
        if isinstance(entry, str):
            yield entry
        else:
            yield from chapter_paths(entry.get("chapters", []))


def test_sessions_are_rendered_and_legacy_chapters_remain():
    book = config(ROOT / "_quarto.yml")["book"]
    chapters = set(chapter_paths(book["chapters"]))
    assert {"content/plan-del-curso.qmd", "content/mapa-de-cobertura.qmd"} <= chapters
    for day in range(1, 11):
        matches = list((ROOT / "content/sesiones").glob(f"{day:02}-*.qmd"))
        assert len(matches) == 1
        assert matches[0].relative_to(ROOT).as_posix() in chapters
    assert "content/modulo-00/index.qmd" in chapters
    assert "content/modulo-10/index.qmd" in chapters
    assert not any(path.startswith("content/sesiones/11-") for path in chapters)
    home = (ROOT / "index.qmd").read_text(encoding="utf-8")
    assert "content/plan-del-curso.qmd" in home
    assert "sesiones 1–10" in home


def test_exactly_one_main_deployer_and_pull_requests_only_validate():
    deployers = []
    for path in (ROOT / ".github/workflows").glob("*.yml"):
        workflow = config(path)
        steps = [step for job in workflow["jobs"].values() for step in job.get("steps", [])]
        if any(step.get("uses", "").startswith("actions/deploy-pages@") for step in steps):
            deployers.append(workflow)
    assert len(deployers) == 1
    workflow = deployers[0]
    assert workflow["on"]["push"]["branches"] == ["main"]
    assert "pull_request" in workflow["on"]
    assert workflow["jobs"]["deploy"]["if"] == "github.event_name != 'pull_request'"
    build_steps = workflow["jobs"]["build"]["steps"]
    commands = "\n".join(step.get("run", "") for step in build_steps)
    assert "python -m pytest -q tests" in commands
    assert "quarto render --to html --no-execute" in commands
    assert any(step.get("uses", "").startswith("actions/configure-pages@") for step in build_steps)
    upload = next(step for step in build_steps if step.get("uses", "").startswith("actions/upload-pages-artifact@"))
    assert upload["with"]["path"] == config(ROOT / "_quarto.yml")["project"]["output-dir"]
