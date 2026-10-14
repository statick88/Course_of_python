"""Execute the published Python examples without rewriting their definitions."""

import ast
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SESSIONS = ROOT / "content" / "sesiones"


def cells(day):
    """Extract native Python cells verbatim, excluding only Quarto option comments."""
    source = next(SESSIONS.glob(f"{day:02}-*.qmd")).read_text(encoding="utf-8")
    return re.findall(r"```\{python\}\n(.*?)\n```", source, re.DOTALL)


def definitions(source):
    """Keep original imports and definitions; examples run separately below."""
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    selected = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
            start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
            selected.extend(lines[start - 1 : node.end_lineno])
    return "".join(selected)


def run_script(workspace, source):
    script = workspace / "probe.py"
    script.write_text(source, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(script)], cwd=workspace, capture_output=True, text=True,
        timeout=30,
    )


@pytest.fixture
def workspace(tmp_path):
    for package in ("inventario_local", "inventario_local/domain", "inventario_local/infrastructure"):
        directory = tmp_path / package
        directory.mkdir(exist_ok=True)
        (directory / "__init__.py").write_text("", encoding="utf-8")
    domain_cell = next(cell for cell in cells(5) if "def validate_quantity" in cell)
    (tmp_path / "inventario_local/domain/item.py").write_text(
        definitions(domain_cell), encoding="utf-8"
    )
    (tmp_path / "inventario_local/infrastructure/sqlite_repository.py").write_text(
        definitions(cells(9)[0]), encoding="utf-8"
    )
    return tmp_path


@pytest.mark.parametrize(
    "day,index,stdout",
    [
        (6, 0, "weak and boundary assertions defined\n"),
        (6, 2, "fixture example is ready for pytest\n"),
        (7, 1, "deterministic boundary counterexample checked\n"),
        (7, 2, "error contracts preserved\n"),
        (8, 0, "parameter matrix defined\n"),
        (8, 2, "adjustment matrix defined\n"),
        (9, 0, "quoted name and complete item state persisted through bound SQL\n"),
        (9, 1, "real SQLite quoted-name integration passed\n"),
        (10, 0, "controlled JSON export passed\n"),
        (10, 2, "rollback verified by fresh read\n"),
    ],
)
def test_documented_stdout(workspace, day, index, stdout):
    result = run_script(workspace, cells(day)[index])
    assert (result.returncode, result.stdout, result.stderr) == (0, stdout, "")


@pytest.mark.parametrize("day,index", [(6, 0), (6, 2), (7, 0), (8, 0), (8, 2)])
def test_exact_pytest_examples(workspace, day, index):
    test_file = workspace / "test_example.py"
    test_file.write_text(cells(day)[index], encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(test_file)], cwd=workspace,
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stderr == ""
    assert "passed" in result.stdout


@pytest.mark.parametrize("day", [6, 8])
def test_documented_boundary_red(workspace, day):
    result = run_script(workspace, cells(day)[1])
    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr.endswith("ValueError: requested units exceed available stock\n")


@pytest.mark.parametrize(
    "value,error,message",
    [(True, "TypeError", "quantity must be an integer, not bool or fractional numeric"),
     (2.5, "TypeError", "quantity must be an integer, not bool or fractional numeric"),
     (-1, "ValueError", "quantity cannot be negative"),
     ("2", "TypeError", "quantity must be an integer, not bool or fractional numeric")],
)
def test_repository_rejects_mutated_quantity_without_writes(workspace, value, error, message):
    source = f'''from inventario_local.domain.item import Item, ItemName
from inventario_local.infrastructure.sqlite_repository import SqliteItemRepository
import sqlite3
connection = sqlite3.connect(":memory:")
repository = SqliteItemRepository(connection)
original = Item("original", ItemName("cable"), 2, {{"hardware"}})
repository.save(original)
connection.commit()
item = Item("invalid", ItemName("mouse"), 1)
item.quantity = {value!r}
changes = connection.total_changes
try:
    repository.save(item)
except {error} as error:
    assert str(error) == {message!r}
else:
    raise AssertionError("invalid quantity accepted")
assert connection.total_changes == changes
assert repository.find("invalid") is None
assert repository.find("original") == original
connection.close()
print("rejected without writes")
'''
    result = run_script(workspace, source)
    assert (result.returncode, result.stdout, result.stderr) == (0, "rejected without writes\n", "")


def test_repository_name_rejection_and_previous_round_trip(workspace):
    source = '''from inventario_local.domain.item import Item, ItemName
from inventario_local.infrastructure.sqlite_repository import SqliteItemRepository
import sqlite3
connection = sqlite3.connect(":memory:")
repository = SqliteItemRepository(connection)
valid = Item("quoted", ItemName("O'Reilly cable"), 0, {"hardware", "cable"})
repository.save(valid)
connection.commit()
assert repository.find("quoted") == valid
item = Item("invalid", ItemName("mouse"), 1)
item.name = "raw name"
changes = connection.total_changes
try:
    repository.save(item)
except TypeError as error:
    assert str(error) == "item name must be an ItemName"
else:
    raise AssertionError("invalid name accepted")
assert connection.total_changes == changes
assert repository.find("invalid") is None
assert repository.find("quoted") == valid
connection.close()
print("name rejected; previous round trip retained")
'''
    result = run_script(workspace, source)
    assert (result.returncode, result.stdout, result.stderr) == (
        0, "name rejected; previous round trip retained\n", ""
    )


@pytest.mark.parametrize("quantity,error", [(True, "TypeError"), (2.5, "TypeError"), (-1, "ValueError")])
def test_export_rejects_before_filesystem_changes(workspace, quantity, error):
    source = definitions(cells(10)[0])
    # RECORD_KEYS is a documented constant, not part of the definitions-only extraction.
    source += '\nRECORD_KEYS = {"item_id", "name", "quantity", "tags"}\n'
    source += f'''target = Path("existing.json")
target.write_text("preserve", encoding="utf-8")
records = [{{"item_id": "sku", "name": "cable", "quantity": {quantity!r}, "tags": []}}]
for destination in (target, Path("absent/items.json")):
    try:
        export_items(destination, records)
    except {error}:
        pass
    else:
        raise AssertionError("invalid export accepted")
assert target.read_text(encoding="utf-8") == "preserve"
assert not Path("absent").exists()
print("invalid export leaves files unchanged")
'''
    result = run_script(workspace, source)
    assert (result.returncode, result.stdout, result.stderr) == (
        0, "invalid export leaves files unchanged\n", ""
    )
