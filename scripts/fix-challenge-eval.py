#!/usr/bin/env python3
"""
Fix challenge code blocks to not execute during Quarto render.

All challenge files have Python code blocks with input() calls that fail
during Quarto render. This script adds '#| eval: false' directive to all
```{python} blocks in challenge files.

Usage:
    python3 scripts/fix-challenge-eval.py
"""

import glob
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

def fix_challenge_file(filepath: Path) -> bool:
    """Add eval: false to all {python} code blocks in a challenge file."""
    content = filepath.read_text()
    
    # Pattern: ```{python} followed by code (not already having eval directive)
    # We need to add #| eval: false right after ```{python}
    pattern = r'(```\{python\})\n(?!#)'
    replacement = r'\1\n#| eval: false\n'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        filepath.write_text(new_content)
        return True
    return False

def main():
    """Fix all challenge files across all modules."""
    challenge_pattern = "content/modulo-*/desafio-*.qmd"
    files = list(PROJECT_ROOT.glob(challenge_pattern))
    
    if not files:
        print("❌ No challenge files found")
        sys.exit(1)
    
    print(f"🔧 Processing {len(files)} challenge files...")
    
    modified_count = 0
    for filepath in sorted(files):
        if fix_challenge_file(filepath):
            modified_count += 1
            print(f"  ✅ {filepath.relative_to(PROJECT_ROOT)}")
    
    print(f"\n✅ Modified {modified_count}/{len(files)} challenge files")
    print("   All Python code blocks will now display without executing during render")

if __name__ == "__main__":
    main()
