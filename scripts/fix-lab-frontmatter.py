#!/usr/bin/env python3
"""
Fix YAML frontmatter in lab files that are missing it.
PDF generation fails when files don't start with --- frontmatter ---.
"""

import sys
from pathlib import Path

LABS_DIR = Path(__file__).parent.parent / "labs"

LAB_METADATA = {
    "lab03-estructuras-control.qmd": {
        "title": "Laboratorio 3: Estructuras de Control",
        "module": "3",
        "topic": "Estructuras de Control",
    },
    "lab04-funciones.qmd": {
        "title": "Laboratorio 4: Funciones",
        "module": "4",
        "topic": "Funciones",
    },
    "lab05-listas-tuplas.qmd": {
        "title": "Laboratorio 5: Listas y Tuplas",
        "module": "5",
        "topic": "Listas y Tuplas",
    },
    "lab06-diccionarios-sets.qmd": {
        "title": "Laboratorio 6: Diccionarios y Sets",
        "module": "6",
        "topic": "Diccionarios y Sets",
    },
    "lab07-manejo-archivos.qmd": {
        "title": "Laboratorio 7: Manejo de Archivos",
        "module": "7",
        "topic": "Manejo de Archivos",
    },
    "lab08-modulos-paquetes.qmd": {
        "title": "Laboratorio 8: Módulos y Paquetes",
        "module": "8",
        "topic": "Módulos y Paquetes",
    },
    "lab09-buenas-practicas.qmd": {
        "title": "Laboratorio 9: Buenas Prácticas",
        "module": "9",
        "topic": "Buenas Prácticas",
    },
    "lab10-proyecto-integrador.qmd": {
        "title": "Laboratorio 10: Proyecto Integrador",
        "module": "10",
        "topic": "Proyecto Integrador",
    },
}


def fix_lab(filepath: Path) -> bool:
    """Add YAML frontmatter if missing."""
    content = filepath.read_text()

    # Already has frontmatter
    if content.startswith("---"):
        return False

    meta = LAB_METADATA.get(filepath.name)
    if not meta:
        print(f"  ⚠️  No metadata template for {filepath.name}")
        return False

    frontmatter = f"""---
title: "{meta['title']}"
execute:
  eval: false
---

"""

    filepath.write_text(frontmatter + content)
    return True


def main():
    """Fix all lab files missing frontmatter."""
    fixed = 0
    for filename, _ in LAB_METADATA.items():
        filepath = LABS_DIR / filename
        if filepath.exists():
            if fix_lab(filepath):
                print(f"  ✅ {filename}")
                fixed += 1
            else:
                print(f"  ⏭️  {filename} (already has frontmatter)")

    print(f"\n{'✅' if fixed > 0 else 'ℹ️'}  {fixed} lab(s) fixed")


if __name__ == "__main__":
    main()
