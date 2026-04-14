# Design: SDD Apply — Security/Marketing/Dev Improvements v3.0

> **Spec**: spec.md v3.0 (SDD-enhanced + Security/Marketing Audit)  
> **Date**: 2026-04-13  
> **Scope**: Apply all Critical and High findings from audit  
> **Change Name**: `apply-sdd-security-marketing-v3`

---

## Architecture Decision

### Approach: Incremental Fixes (No Restructuring)

All changes are **scoped to specific files** without modifying the course structure. Each fix is independent and can be rolled back individually.

| Finding | File(s) Affected | Change Type | Risk |
|---------|-----------------|-------------|------|
| S1 (API keys in examples) | `content/modulo-08/desafio-05-api-clima.qmd` | Code edit | Low |
| S2 (Hardcoded passwords) | `labs/lab03-estructuras-control.qmd`, `content/modulo-06/02-acceder-modificar.qmd` | Code edit | Low |
| S3 (Branch protection) | `.github/workflows/quarto-publish.yml` | Config edit | Low |
| S4 (Outdated deps) | `requirements.txt` | Full replace | Medium |
| S5 (No SECURITY.md) | `SECURITY.md` | New file | None |
| D1 (PDF fail) | Deferred to separate change | N/A | N/A |
| D2 (Deleted tasks) | `q10/*.md` | Git commit | None |
| D5 (Cache files) | `.gitignore` | Config edit | Low |

---

## Technical Design

### S1: API Key Security in Challenge 08-05

**Current**:
```python
API_KEY = "tu_api_key_aqui"
```

**New**:
```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("OPENWEATHER_API_KEY")

if not API_KEY:
    print("Error: Configura tu API key en .env")
    print("Crea un archivo .env con: OPENWEATHER_API_KEY=tu_clave")
    exit()
```

### S2: Remove Hardcoded Passwords

**Current** (`labs/lab03`):
```python
PASSWORD_SECRETA = "Python2026"
```

**New**:
```python
import os

# ⚠️ NUNCA hardcodees contraseñas en código real.
# Usa variables de entorno o input() para demos educativas.
PASSWORD_SECRETA = os.environ.get("DEMO_PASSWORD") or input("Ingresa la contraseña: ")
```

**Current** (`content/modulo-06/02-acceder-modificar.qmd`):
```python
admin_password = "admin123"
```

**New**:
```python
# ⚠️ En producción, usa hash con bcrypt, nunca texto plano.
import getpass
admin_password = getpass.getpass("Contraseña de admin: ")
```

### S4: Modernize requirements.txt

**Current**:
```
pytest==7.4.0
requests==2.31.0
beautifulsoup4==4.12.2
flask==3.0.0
```

**New**:
```
# Core testing
pytest>=8.0
pip-audit>=2.7  # Security vulnerability scanner

# HTTP and web
requests>=2.32
beautifulsoup4>=4.12
flask>=3.1

# Environment and security
python-dotenv>=1.0
```

### D5: .gitignore for Cache Files

**Add**:
```
# Quarto execution cache
*.quarto_ipynb*
```

---

## Verification Plan

Each change is verified by:

| Change | Verification Method | Expected Result |
|--------|-------------------|-----------------|
| S1 | `grep -r "api_key.*=" content/` | No hardcoded API keys found |
| S2 | `grep -r "PASSWORD.*=" labs/ content/` | No hardcoded passwords found |
| S3 | `cat .github/workflows/*.yml` | pull_request trigger present |
| S4 | `pip-audit -r requirements.txt` | 0 known vulnerabilities |
| S5 | `test -f SECURITY.md` | File exists |
| D5 | `git status --ignored` | Cache files shown as ignored |

---

## Rollback Plan

All changes are **file-scoped** and can be reverted with:

```bash
git revert HEAD~N  # N = number of commits in this change
```

No database migrations or infrastructure changes — zero blast radius.
