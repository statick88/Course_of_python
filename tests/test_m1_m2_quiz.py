"""Check the answer contract of the learner-facing Module 2 questionnaire."""

import re
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "quizzes/quiz-modulo-02.qmd"


def questions():
    text = SOURCE.read_text(encoding="utf-8")
    result = []
    for block in re.split(r"^### ", text, flags=re.MULTILINE)[1:]:
        title = block.splitlines()[0]
        options = re.findall(r"^- \[([ x])\] (.+)$", block, re.MULTILINE)
        result.append((title, options))
    return result


def test_ten_questions_have_exactly_one_correct_answer():
    items = questions()
    assert len(items) == 10
    for title, options in items:
        assert len(options) == 4, title
        assert sum(mark == "x" for mark, _ in options) == 1, title


def test_no_question_has_duplicate_visible_options():
    for title, options in questions():
        labels = [label.strip("` ") for _, label in options]
        assert len(labels) == len(set(labels)), title


def test_complex_question_accepts_both_valid_constructions():
    title, options = next(item for item in questions() if "complejo" in item[0])
    assert complex(3, 4) == 3 + 4j
    assert [label for mark, label in options if mark == "x"] == [
        "Ambos son válidos"
    ], title


def test_scientific_notation_has_no_second_valid_notation_option():
    _, options = next(item for item in questions() if "notación científica" in item[0])
    assert not any(
        mark == " " and label.strip("` ") in {"1e3", "1.0e3"} for mark, label in options
    )


def test_type_repr_is_code_not_raw_html():
    text = SOURCE.read_text(encoding="utf-8")
    assert "- [x] `<class 'int'>`" in text
    assert not re.search(r"^- \[[ x]\] <class", text, re.MULTILINE)
