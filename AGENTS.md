# AGENTS.md — Configuración de Agentes

Este archivo define los perfiles, agentes y configuraciones para el desarrollo asistido por IA en el proyecto Course_of_python.

---

## Tabla de Contenidos

1. [Perfiles Disponibles](#perfiles-disponibles)
2. [Agentes Principales](#agentes-principales)
3. [Skills por Dominio](#skills-por-dominio)
4. [MCPs Configurados](#mcps-configurados)
5. [Directorios de Agentes](#directorios-de-agentes)

---

## Perfiles Disponibles

| Perfil | Descripción | Especialidad |
|--------|-------------|--------------|
| **statick** | Senior Architect & Technical Mentor | Architecture, SDD, patterns |
| **developer** | FullStack Developer | React Native, Flutter, Next.js, Python |
| **facilitator** | Facilitator/Teacher | Course creation, mentoring |
| **researcher** | Researcher | Scientific papers, IEEE/ACM |
| **hacker** | Security researcher | Pentesting, CTF, Bug Bounty |
| **student** | Student | Learning, Master UCM |

---

## Agentes Principales

### Agentes de Desarrollo (SDD)

| Agente | Descripción | Especialidad |
|--------|-------------|--------------|
| `explore` | Exploración del codebase | Búsqueda de patrones |
| `sdd-spec` | Spec Writer | Requirements, scenarios |
| `sdd-design` | Technical Design | Arquitectura, contracts |
| `sdd-apply` | Implementador | Código según specs |
| `sdd-verify` | Verificador | Validación línea a línea |
| `sdd-tasks` | Task Breakdown | Descomposición de tareas |

### Agentes de Calidad

| Agente | Descripción | Especialidad |
|--------|-------------|--------------|
| `qa-engineer` | QA Engineer | Tests, linting, emuladores |
| `security-reviewer` | Security Review | OWASP, vulnerabilidades |
| `design-reviewer` | Design Review | UI/UX, Apple HIG |

### Agentes Especializados

| Agente | Descripción | Especialidad |
|--------|-------------|--------------|
| `cientifico` | Investigador | Papers, investigación académica |
| `pentest-methodology` | Pentester | Pentesting sistemático |
| `developer` | FullStack | React, Flutter, Python |
| `facilitator` | Docente | Creación de cursos |

---

## Skills por Dominio

### 💻 Desarrollo

| Skill | Descripción | Activador |
|-------|-------------|-----------|
| `react-19` | React 19 patterns | "React Native", "React 19" |
| `flutter` | Flutter patterns | "Flutter", "mobile" |
| `python` | Python best practices | "Python", "django" |
| `typescript` | TypeScript strict | "TypeScript", "types" |
| `nextjs-15` | Next.js 15 App Router | "Next.js", "routing" |

### 🎨 Diseño

| Skill | Descripción | Activador |
|-------|-------------|-----------|
| `ui-ux-pro-max` | UI/UX design intelligence | "design", "UI", "UX" |
| `apple-mobile-design` | Apple Design System | "Apple HIG", "iOS", "glassmorphism" |
| `awesome-design-md` | Brand design patterns | "web design", "brand" |

### 🔐 Seguridad

| Skill | Descripción | Activador |
|-------|-------------|-----------|
| `pentest-methodology` | Metodología completa | "pentest", "penetration" |
| `pentest-web` | Web app security | "web security", "OWASP" |
| `pentest-core` | Fundamentos pentesting | "pentest core" |
| `software-security` | Código seguro | "secure code", "vulnerability" |
| `dependency-scan` | Escaneo de CVEs | "CVE", "vulnerabilidades" |
| `secrets-scan` | Detección de secretos | "API keys", "passwords" |

### 🧪 Testing/QA

| Skill | Descripción | Activador |
|-------|-------------|-----------|
| `pytest` | Pytest testing | "tests", "unittest" |
| `playwright` | E2E testing | "E2E", "end-to-end" |
| `tdd` | Test-driven development | "red-green-refactor", "TDD" |
| `react-native-qa-workflow` | QA para React Native | "QA mobile", "emulator" |

### 🔬 Investigación

| Skill | Descripción | Activador |
|-------|-------------|-----------|
| `busqueda_cientifica` | Búsqueda académica | "papers", "IEEE", "ACM" |
| `cientifico` | Orquestador de investigación | "research", "investigar" |
| `redaccion_cientifica` | Redacción académica | "paper", "publicación" |
| `estructura-paper` | Estructura IMRAD | "IMRAD", "artículo" |

### 📚 Educación

| Skill | Descripción | Activador |
|-------|-------------|-----------|
| `abacom-cursos` | Cursos ABACOM | "curso ABACOM", "laboratorio" |
| `course-creation-triad` | Creación de cursos | "crear curso", "diseño curriculum" |
| `learning-integrity-anti-ai` | Integridad anti-IA | "anti-AI", "plagio" |
| `gentle-teaching` | Teaching con IA | "enseñar", "explicar" |

---

## MCPs Configurados

### MCPs de Desarrollo

| MCP | Descripción | Uso Principal |
|-----|-------------|----------------|
| `context7` | Documentación de librerías | Resolver dudas de APIs |
| `lexis` | Análisis de código | Encontrar referencias, arquitectura |
| `playwright` | Automatización de browser | Testing E2E, web scraping |
| `playwright-cli` | CLI de Playwright | Automatización avanzada |

### MCPs de Investigación

| MCP | Descripción | Uso Principal |
|-----|-------------|----------------|
| `notebooklm` | Investigación con IA | Papers, resúmenes, podcast |
| `busqueda_cientifica` | Búsqueda académica | IEEE, ACM, arXiv |
| `scientific-research` | Papers Q1/Q2 | Revistas de alto impacto |

### MCPs de Memoria

| MCP | Descripción | Uso Principal |
|-----|-------------|----------------|
| `engram` | Memoria persistente | Recordar decisiones |

### MCPs de utility

| MCP | Descripción | Uso Principal |
|-----|-------------|----------------|
| `paypal-production` | Operaciones PayPal | Pagos, suscripciones |
| `websearch` | Búsqueda web | Información actual |

---

## Directorios de Agentes

### agentes/

```
agentes/
├── agente_profesor/        # Agente educativo
│   ├── SKILL.md
│   └── config.yaml
└── agente_security/        # Agente de seguridad
    ├── SKILL.md
    └── config.yaml
```

---

## Configuración de Skills

Los skills se cargan automáticamente según la tarea. Parainvocar un skill manualmente:

```markdown
# En el prompt
Usa el skill [nombre-del-skill] para esta tarea.
```

### Instalación de Nuevos Skills

1. Crear directorio en `~/.claude/skills/` o `~/.config/opencode/skills/`
2. Agregar `SKILL.md` con instrucciones
3. El skill se cargará automáticamente cuando se necesite

---

## Métricas de Calidad

Cada HU debe pasar los gates de calidad:

- ✅ **QA Gate**: Unit tests passing, linting passed, typecheck
- ✅ **Security Gate**: No secrets exposed, no SQL injection
- ✅ **Design Gate**: Apple HIG compliance
- ✅ **Emulator Test**: iOS + Android runs without error

### Developer Score (1-10)

| Criterio | Puntuación Máxima |
|----------|-------------------|
| Architecture | /10 |
| Code Quality | /10 |
| Tests | /10 |
| Security | /10 |
| Design | /10 |
| Emulator Test | /10 |

**TOTAL**: /60 → Pass: ≥7/10

---

*Configuración basada en Gentle-AI + Spec-Driven Development*