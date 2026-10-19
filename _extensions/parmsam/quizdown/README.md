# Quizdown in this course

The HTML filter supports both fenced `.quizdown` Divs and the legacy Quizdown
code-block format. Div content is serialized as Markdown, escaped for its HTML
host, and initialized by the existing vendor runtime. Horizontal-rule AST nodes
use `***` because Quizdown reserves `---` for YAML options. Literal text inside
code spans and code blocks is not rewritten. Outside HTML, Divs retain their AST.

The legacy code-block route is unchanged. This correction does not repair the
content or answer keys of unrelated question banks.

## Verification

Run the focused render checks with Quarto available on `PATH`:

```sh
python -m pytest -q tests/test_quizdown_m1_m2.py
```

`QUIZDOWN_QUARTO` optionally selects another Quarto executable. Tests render
isolated fixtures with the exact Lua filter explicitly selected and verify that
Git cannot discover a parent checkout. If Quarto is absent, render checks report
SKIP rather than implying a pass.

Browser checks also require `PLAYWRIGHT_MODULE` (the installed Playwright module
path) and `PLAYWRIGHT_BROWSER` (the browser executable). With those variables set,
the same command exercises Module 2 full credit, one wrong answer, restart with
no selected answers, and mounts of the other specified banks. Without them,
browser checks report SKIP; passing source checks alone is not interactive
acceptance. No browser or package is installed by these tests.
