from __future__ import annotations

import io
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def source_block(path: str, marker: str) -> str:
    """Return the Python fenced block containing marker from the published lesson."""
    content = (ROOT / path).read_text(encoding="utf-8")
    for block in content.split("```python\n")[1:]:
        code = block.split("```", 1)[0]
        if marker in code:
            return code
    raise AssertionError(f"No Python block with {marker!r} in {path}")


def run_source(code: str) -> list[str]:
    output = io.StringIO()
    with redirect_stdout(output):
        exec(code, {})
    return output.getvalue().splitlines()


def test_compound_assignment_example_narrates_each_real_balance() -> None:
    code = source_block(
        "content/modulo-02/01-operadores-aritmeticos.qmd", "saldo = 1000"
    )

    assert run_source(code) == [
        "1200",
        "1400",
        "1250",
        "2500",
        "625.0",
        "208.0",
        "5.0",
        "25.0",
    ]


def test_floor_division_example_shows_floor_for_negative_and_float_operands() -> None:
    code = source_block(
        "content/modulo-02/01-operadores-aritmeticos.qmd", "division_entera = a // b"
    )

    assert run_source(code)[-2:] == ["-3", "2.0"]


def test_visitor_access_rule_requires_an_accompanying_person() -> None:
    code = source_block(
        "content/modulo-02/03-operadores-logicos.qmd", "acceso_visitante ="
    )

    for has_appointment, accompanied, expected in [(True, False, False), (False, True, False), (True, True, True)]:
        scenario = code.replace("es_empleado = True", "es_empleado = False").replace("es_visitante = False", "es_visitante = True").replace("tiene_cita = True", f"tiene_cita = {has_appointment}")
        scenario = scenario.replace("esta_acompanado = True", f"esta_acompanado = {accompanied}")
        assert run_source(scenario) == [str(expected)]


def test_comment_example_contains_comments_not_a_string_literal() -> None:
    import ast
    code = source_block("content/modulo-01/03-hola-mundo.qmd", "# Esto es un comentario de una línea")
    assert ast.get_docstring(ast.parse(code)) is None
    assert run_source(code) == ["Los comentarios no se imprimen"]


def test_rfind_narration_matches_the_printed_index() -> None:
    path = "content/modulo-02/05-strings-avanzado.qmd"
    code = source_block(path, 'frase.rfind("Python")')
    assert run_source(code)[:3] == ["0", "18", "2"]
    assert '— 18 (última aparición)' in code
    assert "Devuelve `18`" in (ROOT / path).read_text(encoding="utf-8")
