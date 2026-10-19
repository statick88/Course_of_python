import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def snippet(relative_path: str) -> str:
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    match = re.search(r"```\{python\}\n#\| eval: false\n(.*?)```", source, re.DOTALL)
    assert match, f"No se encontró una solución Python en {relative_path}"
    return match.group(1)


def run_snippet(relative_path: str, stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-c", snippet(relative_path)],
        input=stdin,
        env={**os.environ, "PYTHONHASHSEED": "0"},
        text=True,
        capture_output=True,
        check=False,
        timeout=5,
    )


def test_propinas_retains_float_learning_and_expected_amounts() -> None:
    result = run_snippet(
        "content/modulo-02/desafio-01-calculadora-propinas.qmd", "85.5\n15\n3\n"
    )

    assert result.returncode == 0, result.stderr
    assert "Propina (15.0%): $12.82" in result.stdout
    assert "Total con propina: $98.32" in result.stdout
    assert "Cada persona paga: $32.77" in result.stdout

    challenge = (
        ROOT / "content/modulo-02/desafio-01-calculadora-propinas.qmd"
    ).read_text(encoding="utf-8")
    assert "Propina (15.0%): $12.82" in challenge
    assert "Total con propina: $98.32" in challenge
    assert "Cada persona paga: $32.77" in challenge


def test_analizador_uses_documented_educational_token_and_separator_rules() -> None:
    texto = "Python es un lenguaje de programación versátil. Es fácil de aprender y muy poderoso."
    result = run_snippet(
        "content/modulo-02/desafio-06-analizador-texto.qmd", texto + "\n"
    )

    assert result.returncode == 0, result.stderr
    assert "Caracteres totales: 84" in result.stdout
    assert "Caracteres (sin espacios): 71" in result.stdout
    assert "Palabras: 14" in result.stdout
    assert "Letra más frecuente: 'e' (10 veces)" in result.stdout
    assert "Porcentaje de vocales: 40.6%" in result.stdout

    challenge = (ROOT / "content/modulo-02/desafio-06-analizador-texto.qmd").read_text(
        encoding="utf-8"
    )
    assert "Caracteres totales: 84" in challenge
    assert "Caracteres (sin espacios): 71" in challenge
    assert "Palabras: 14" in challenge
    assert "Letra más frecuente: 'e' (10 veces)" in challenge
    assert "Porcentaje de vocales: 40.6%" in challenge
    assert "separadores de puntuación" in challenge


def test_imc_rejects_zero_height_without_traceback() -> None:
    result = run_snippet(
        "content/modulo-01/desafio-04-calculadora-imc.qmd", "Ana\n70\n0\n"
    )

    assert result.returncode == 0
    assert "Error: la estatura debe ser mayor que cero." in result.stdout
    assert result.stderr == ""


def test_validador_edad_rejects_future_year_in_2026_context() -> None:
    result = run_snippet(
        "content/modulo-02/desafio-03-validador-edad.qmd",
        "Ana\n2027\nana@example.com\n",
    )

    assert result.returncode == 0
    assert "✗ Año inválido: no puede ser posterior a 2026" in result.stdout
    assert "--- Registro fallido: corrige los errores ---" in result.stdout
    assert "Categoría:" not in result.stdout
    assert result.stderr == ""


def test_contacto_names_the_inclusive_age_boundary() -> None:
    result = run_snippet(
        "content/modulo-01/desafio-06-formulario-contacto.qmd",
        "Ana García\nana@correo.com\n0987654321\n17\n18\n",
    )

    assert result.returncode == 0
    assert "Error: Debes tener al menos 18 años" in result.stdout
    assert "Edad:       18 años" in result.stdout
    assert result.stderr == ""


def run_cesar_function(
    message: str, displacement: int
) -> subprocess.CompletedProcess[str]:
    source = snippet("content/modulo-02/desafio-05-cifrado-cesar.qmd")
    function_source = source.split('print("=== CIFRADO CÉSAR ===")')[0]
    return subprocess.run(
        [
            sys.executable,
            "-c",
            function_source
            + f"print(cifrar_cesar({message!r}, {displacement!r}))\n"
            + f"print(cifrar_cesar(cifrar_cesar({message!r}, {displacement!r}), {-displacement!r}))\n",
        ],
        text=True,
        capture_output=True,
        check=False,
        timeout=5,
    )


def test_cesar_only_shifts_ascii_letters_and_round_trips() -> None:
    result = run_cesar_function("¡HólA ñ!", 3)

    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines() == ["¡KóoD ñ!", "¡HólA ñ!"]


def test_dni_accepts_eight_digits_and_instructor_uses_that_contract() -> None:
    valid = run_snippet("content/modulo-02/desafio-04-generador-dni.qmd", "12345678\n")
    invalid = run_snippet("content/modulo-02/desafio-04-generador-dni.qmd", "1234567\n")

    assert valid.returncode == 0, valid.stderr
    assert "DNI completo: 12345678-Z" in valid.stdout
    assert invalid.returncode == 0, invalid.stderr
    assert "exactamente 8 dígitos numéricos" in invalid.stdout

    guide = (ROOT / "instructor/modulo-02-guia-instructor.md").read_text(
        encoding="utf-8"
    )
    assert "import random" not in guide
    assert 'input("Ingresa tu número de DNI (8 dígitos): ").strip()' in guide
    assert "len(dni_input) != 8" in guide
    assert "dni_numero % 23" in guide


def test_validador_edad_rejects_year_zero_and_describes_approximate_age() -> None:
    path = "content/modulo-02/desafio-03-validador-edad.qmd"
    result = run_snippet(path, "Ana\n0000\nana@example.com\n")
    assert result.returncode == 0
    assert result.stderr == ""
    assert "✗ Año inválido: debe ser mayor que 0" in result.stdout
    assert "Categoría:" not in result.stdout
    assert "3. Calcule la edad aproximada" in (ROOT / path).read_text(encoding="utf-8")


def test_analyzer_punctuation_only_has_no_longest_word_or_traceback() -> None:
    result = run_snippet("content/modulo-02/desafio-06-analizador-texto.qmd", ".!?\n")
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert "Palabras: 0" in result.stdout
    assert "Palabra más larga: 'N/A' (0 letras)" in result.stdout


def test_analyzer_frequency_ties_use_alphabetical_order() -> None:
    result = run_snippet(
        "content/modulo-02/desafio-06-analizador-texto.qmd", "bbb aaa\n"
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    assert "Letra más frecuente: 'a' (3 veces)" in result.stdout
    source = (ROOT / "content/modulo-02/desafio-06-analizador-texto.qmd").read_text(
        encoding="utf-8"
    )
    assert "orden alfabético" in source


def test_m1_m2_challenge_and_lab_navigation_targets_exist() -> None:
    sources = [
        *sorted((ROOT / "content/modulo-01").glob("desafio-*.qmd")),
        *sorted((ROOT / "content/modulo-02").glob("desafio-*.qmd")),
        ROOT / "labs/lab01-primer-programa.qmd",
        ROOT / "labs/lab02-variables-en-accion.qmd",
    ]
    for source in sources:
        for target in re.findall(
            r"\]\(([^)]+\.qmd)\)", source.read_text(encoding="utf-8")
        ):
            assert (source.parent / target).resolve().is_file(), f"{source}: {target}"
