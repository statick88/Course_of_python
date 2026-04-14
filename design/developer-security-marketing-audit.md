# Audit: Developer + Security + Marketing — Python Fundamentos ABACOM

> **Fecha**: 2026-04-13  
> **Auditores**: Developer Profile + NotebookLM (Dev/Marketing/Security)  
> **Scope**: Código, infraestructura, seguridad, posicionamiento

---

## 1. Executive Summary

El curso Python Fundamentos de ABACOM está **~85% completo** con contenido educativo de alta calidad (158 archivos .qmd, 196 HTML generados, 11 módulos, 5 proyectos MIT-inspired). La infraestructura de Quarto/CI-CD funciona correctamente (workflow con environment github-pages). Sin embargo, se identificaron **3 hallazgos de seguridad** (archivos con referencias a credenciales en ejemplos, workflow sin branch protection, requirements.txt con versiones desactualizadas), **5 hallazgos de marketing** (sin landing page diferenciada, meta tags incompletos, sin call-to-action para inscripción), y **4 hallazgos de desarrollo** (PDF render fail sin investigar, 6 tareas .md eliminadas sin reemplazo, .gitignore ignora output/ pero no se usa, notebooks .ipynb ignorados pero se usan cache files).

---

## 2. Detailed Findings

### 2.1 Security Findings

| # | Hallazgo | Severidad | Archivo | Descripción | Mitigación |
|---|----------|-----------|---------|-------------|------------|
| S1 | **Referencias a API keys en contenido educativo** | 🟡 Medium | `content/modulo-08/desafio-05-api-clima.qmd` | El desafío de API del clima menciona usar una API key de OpenWeatherMap sin instrucción clara de no commitearla | Agregar `.env` instruction en el desafío y crear `.env.example` |
| S2 | **Contraseñas hardcodeadas en ejemplos** | 🟡 Medium | `labs/lab03-estructuras-control.qmd`, `content/modulo-06/02-acceder-modificar.qmd` | Ejemplos usan `PASSWORD_SECRETA = "Python2026"` — si bien es educativo, normaliza malas prácticas | Usar `os.environ.get("PASSWORD")` en ejemplos |
| S3 | **Workflow sin branch protection** | 🟢 Low | `.github/workflows/quarto-publish.yml` | El workflow se ejecuta en push a main sin require review | Agregar `pull_request` trigger + require approvals |
| S4 | **requirements.txt con versiones de 2024** | 🟢 Low | `requirements.txt` | requests==2.31.0 (Jul 2023), flask==3.0.0 (Sep 2023) — posibles CVE conocidos | Actualizar a versiones 2026: requests>=2.32, flask>=3.1 |
| S5 | **No hay SECURITY.md ni CODE_OF_CONDUCT.md activo** | 🟢 Low | Root | No hay proceso para reportar vulnerabilidades del curso | Crear SECURITY.md con contacto de reporte |

### 2.2 Development Findings

| # | Hallazgo | Severidad | Archivo | Descripción | Mitigación |
|---|----------|-----------|---------|-------------|------------|
| D1 | **PDF render fail sin root cause analysis** | 🔴 High | `_quarto.yml` | Error "YAML parse exception at line 33649" — 4 intentos fallidos sin diagnóstico profundo | Crear issue en quarto-dev/quarto-cli con archivo mínimo reproducible |
| D2 | **6 tareas .md eliminadas sin tracking** | 🟡 Medium | `q10/tarea-*.md` | `git status` muestra 6 archivos eliminados sin commit — pérdida de trabajo anterior | Commit con mensaje explicando migración a .html |
| D3 | **output/ en .gitignore pero se usa para NLM downloads** | 🟡 Medium | `.gitignore`, `output/` | Los archivos generados por NotebookLM (study-guide, quiz, flashcards) se ignoran | Crear subdirectorio `output/generated/` excluido de gitignore |
| D4 | **196 HTML en docs/ sin versioning** | 🟢 Low | `docs/` | Docs se regeneran en cada build — no necesitan estar en git | Agregar docs/ a .gitignore y usar GitHub Actions artifact |
| D5 | **Cache files .quarto_ipynb_* en git** | 🟢 Low | `content/modulo-*/` | 180+ archivos de cache de ejecución de código — aumentan repo innecesariamente | Agregar `*.quarto_ipynb_*` a .gitignore |

### 2.3 Marketing Findings

| # | Hallazgo | Severidad | Archivo | Descripción | Mitigación |
|---|----------|-----------|---------|-------------|------------|
| M1 | **Sin landing page de ventas** | 🔴 High | `index.qmd` | La página actual es informativa, no convierte visitantes en estudiantes | Crear landing page con CTA, testimonios, beneficios, precio |
| M2 | **Meta description genérica** | 🟡 Medium | `_quarto.yml` | "Curso completo de programación Python para principiantes" — no diferencia de freeCodeCamp/CS50 | Agregar propuesta de valor única: metodología basada en retos, 70+ desafíos, proyectos MIT-inspired |
| M3 | **Sin analytics ni tracking** | 🟡 Medium | `index.qmd` | No hay Google Analytics, Plausible ni ningún sistema de métricas de visitantes | Agregar script de analytics en `include-in-header` |
| M4 | **Sin brochures descargables** | 🟡 Medium | `output/` | No hay PDF de syllabus, brochure de ventas ni certificado de muestra | Crear brochure en PDF con diseño profesional |
| M5 | **Sin social proof** | 🟢 Low | `index.qmd`, `about.qmd` | No hay testimonios de estudiantes, logos de universidades, estadísticas de graduación | Agregar sección de social proof en index y about |

---

## 3. SDD Delta Spec

### ADDED Requirements

#### Requirement: Security-Aware Code Examples

The course **SHALL** use secure coding practices in ALL example code. No hardcoded passwords, API keys, or secrets SHALL appear in any code block — even in educational examples.

**Scenario: Password example uses environment variable**
- GIVEN a challenge that requires authentication
- WHEN the example code is displayed
- THEN it uses `os.environ.get("PASSWORD")` or `input()`
- AND it includes a comment explaining why hardcoding is bad practice

**Scenario: API key example uses .env file**
- GIVEN a challenge that requires an API key
- WHEN the example code references credentials
- THEN it loads from `.env` using `python-dotenv`
- AND the `.env` file is listed in `.gitignore`
- AND an `.env.example` template is provided

#### Requirement: Analytics and Conversion Tracking

The course site **MUST** include visitor analytics to measure engagement and conversion rates.

**Scenario: Visitor tracking enabled**
- GIVEN a student visits the course landing page
- WHEN the page loads
- THEN an analytics script is executed (Plausible or Google Analytics)
- AND the visitor's session is tracked anonymously
- AND no PII is collected

#### Requirement: Sales Landing Page

The course **SHALL** have a dedicated landing page that converts visitors into enrolled students with clear value proposition, testimonials, and call-to-action.

**Scenario: Landing page conversion**
- GIVEN a visitor arrives at the course URL
- WHEN they view the landing page
- THEN they see: hero section, course benefits, syllabus overview, testimonials, instructor bio, pricing, CTA button
- AND the page loads in under 2 seconds
- AND it is mobile-responsive

### MODIFIED Requirements

#### Requirement: Requirements Currency (MODIFIED)

**Previous**: `requirements.txt` lists specific versions (requests==2.31.0, flask==3.0.0)

**New**: `requirements.txt` **MUST** use minimum version constraints and be updated at least quarterly. `requirements.txt` SHALL include `safety` or `pip-audit` for vulnerability scanning.

**Rationale**: Pinned versions from 2023 may have known CVEs. Using `>=` allows students to get patched versions.

#### Requirement: PDF Generation (MODIFIED)

**Previous**: PDF generation is configured but untested.

**New**: PDF generation **SHALL** either be fixed or replaced with an alternative printable format (browser print-to-PDF guide). If Quarto PDF fails, the course **MUST** provide a documented workaround.

### REMOVED Requirements

#### Requirement: output/ in .gitignore (REMOVED)

**Reason**: `output/` is now used for NotebookLM-generated content (study guides, quizzes, flashcards) that should be tracked. Replace with `output/generated/` exclusion pattern.

---

## 4. Prioritized Action Items

| # | Acción | Impacto | Esfuerzo | Prioridad |
|---|--------|---------|----------|-----------|
| 1 | **Commit: eliminar 6 tareas .md + tracking** | Limpieza repo | 5 min | 🔴 Urgente |
| 2 | **Actualizar requirements.txt** (seguridad) | Eliminar CVE conocidos | 15 min | 🔴 Alta |
| 3 | **Crear SECURITY.md** | Proceso de reporte | 10 min | 🟡 Media |
| 4 | **Agregar analytics (Plausible)** | Métricas de conversión | 20 min | 🟡 Media |
| 5 | **Crear landing page con CTA** | Conversión de visitantes | 2 horas | 🔴 Alta |
| 6 | **Fix PDF o crear workaround** | Formato offline | 1 hora | 🟡 Media |
| 7 | **Agregar .env.example para API challenge** | Buenas prácticas seguridad | 10 min | 🟡 Media |
| 8 | **Reemplazar passwords hardcodeadas** | Educación en seguridad | 30 min | 🟡 Media |
| 9 | **Agregar social proof a index/about** | Credibilidad | 30 min | 🟢 Baja |
| 10 | **Limpiar cache files de git** | Reducir repo size | 20 min | 🟢 Baja |

---

## 5. Risk Assessment Matrix

| Riesgo | Probabilidad | Impacto | Nivel | Mitigación |
|--------|-------------|---------|-------|------------|
| CVE en dependencies | Media | Alto | 🟡 Medio | Actualizar requirements.txt + pip-audit |
| Credenciales expuestas en ejemplos | Baja | Alto | 🟢 Bajo | Reemplazar con .env/os.environ |
| Baja conversión de visitantes | Alta | Alto | 🔴 Alto | Landing page + CTA + analytics |
| PDF no disponible | Alta | Medio | 🟡 Medio | Workaround print-to-PDF |
| Repo grow por cache files | Media | Bajo | 🟢 Bajo | .gitignore para cache |

---

**Audit completed**: 2026-04-13  
**Next review**: After landing page implementation  
**Responsible**: Diego Saavedra
