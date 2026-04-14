# Tasks: SDD Apply v3.0 — Security/Marketing/Dev Improvements

> **Spec**: spec.md v3.0  
> **Design**: design/sdd-apply-v3-design.md  
> **Change Name**: `apply-sdd-security-marketing-v3`

---

## Phase 1: Security Fixes (Critical)

- [ ] **1.1** Fix API key in `content/modulo-08/desafio-05-api-clima.qmd`
  - Replace hardcoded `API_KEY = "..."` with `os.environ.get()`
  - Add `.env.example` file
  - Add security comment explaining why env vars are safer
  - Verify: `grep -r "API_KEY.*=" content/` returns no hardcoded values

- [ ] **1.2** Remove hardcoded passwords in `labs/lab03-estructuras-control.qmd`
  - Replace `PASSWORD_SECRETA = "Python2026"` with `os.environ.get()` or `input()`
  - Add comment: "⚠️ NUNCA hardcodees contraseñas en código real"
  - Verify: `grep "PASSWORD_SECRETA.*=" labs/lab03` returns no hardcoded value

- [ ] **1.3** Remove hardcoded passwords in `content/modulo-06/02-acceder-modificar.qmd`
  - Replace any hardcoded credentials with `getpass` or `os.environ`
  - Add security comment
  - Verify: `grep "password.*=" content/modulo-06/02` returns no hardcoded value

## Phase 2: Infrastructure Fixes (High)

- [ ] **2.1** Update `requirements.txt`
  - Replace pinned versions with `>=` constraints
  - Add `pip-audit>=2.7` for vulnerability scanning
  - Add `python-dotenv>=1.0` for secure env var loading
  - Verify: `pip-audit -r requirements.txt` runs successfully

- [ ] **2.2** Create `SECURITY.md`
  - Contact information for reporting vulnerabilities
  - Policy for reporting security issues in course content
  - Response timeline commitment
  - Verify: `test -f SECURITY.md` returns true

- [ ] **2.3** Add pull_request trigger to `.github/workflows/quarto-publish.yml`
  - Add `pull_request:` trigger alongside `push:`
  - Add branch protection recommendation in comments
  - Verify: workflow YAML is valid

## Phase 3: Cleanup (Medium)

- [ ] **3.1** Update `.gitignore`
  - Add `*.quarto_ipynb*` pattern for execution cache files
  - Verify: cache files appear as ignored in `git status --ignored`

- [ ] **3.2** Commit deleted task files
  - `git add q10/` to stage the deletion of 6 `.md` files
  - Commit message: "chore: remove old task files, replaced by HTML units in q10/unidades/"
  - Verify: `git status --short` shows no staged deletions

## Phase 4: Verification (Required)

- [ ] **4.1** Run `quarto render --to html --no-execute` — succeeds with 0 errors
- [ ] **4.2** Run security verification: `grep -rE "(API_KEY|PASSWORD|SECRET).*=" content/ labs/` — no hardcoded values
- [ ] **4.3** Run `pip-audit -r requirements.txt` — 0 known vulnerabilities
- [ ] **4.4** Commit all changes: `git add -A && git commit -m "fix(sdd-v3): apply security and infrastructure improvements"`
- [ ] **4.5** Push to remote: `git push origin main`

---

## Acceptance Criteria

- [ ] 0 hardcoded passwords or API keys in any code example
- [ ] `requirements.txt` uses `>=` constraints and includes `pip-audit`
- [ ] `SECURITY.md` exists with contact info
- [ ] `.gitignore` includes cache file patterns
- [ ] All deleted task files are committed
- [ ] HTML render succeeds with 0 errors
- [ ] All changes committed and pushed
