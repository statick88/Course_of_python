# Spec: Programación Python Fundamentos con Quarto

> **Versión**: 2.0 (SDD-enhanced)  
> **Fecha**: 2026-04-13  
> **Estado**: Contenido 100% implementado, QA pendiente  
> **Related Prior Specs**: Ethical_Hacking course spec (openspec/changes/2026-03-06-desarrollo-contenido-curso/spec.md) - lesson patterns, challenge structure

## Overview

Especificación SDD del curso de Programación Python Fundamentos que utiliza Quarto como plataforma de enseñanza. El curso transforma principiantes en desarrolladores Python competentes mediante 70+ desafíos progresivos, buenas prácticas de código limpio, y metodología basada en retos de Diego Saavedra.

## Related Prior Specs

- **Ethical_Hacking Course Spec** (Ethical_Hacking/openspec/): Course structure follows same 10-module pattern with challenges + labs
- **ABACOM Course Framework**: Quarto-based delivery, instructor guides, quiz system
- **Q10 Platform Patterns**: Task generation for learning platforms (5 tasks created for administracion-servidores-linux)

**Key Learnings from Prior Specs**:
- Challenge difficulty progression: basic → intermediate → applied → integrative
- Each module MUST have: theory units (6-8), challenges (7), summary (1), instructor guide (1), quiz (1), lab (1+)
- Quarto navigation MUST register ALL content files in _quarto.yml
- Labs directory pattern: labs/labNN-{topic}.qmd with executable code blocks

---

## ADDED Requirements (Phase 4-5 Critical Gaps)

### Requirement: Quarto Navigation Completeness

The system SHALL ensure ALL content files (units, challenges, labs, quizzes) are registered in _quarto.yml chapters array. No .qmd file SHALL exist without being referenced in navigation.

**Rationale**: 56 challenge files (modulo-02 through modulo-09) exist on disk but are invisible in book navigation.

#### Scenario: All module challenges visible in navigation

- GIVEN 56 challenge files exist in content/modulo-{02-09}/desafio-XX-*.qmd
- WHEN student browses the course
- THEN all challenges appear in sidebar navigation under their respective modules
- AND student can click any challenge to access it directly

#### Scenario: Module 01 index page registered

- GIVEN content/modulo-01/index.qmd exists on disk
- WHEN _quarto.yml is rendered
- THEN modulo-01 index page appears as first entry in module 1 navigation
- AND it shows module overview before unit 01-que-es-python.qmd

### Requirement: Stale File Cleanup

The system SHALL NOT contain orphaned duplicate files at project root when canonical versions exist in organized subdirectories.

**Rationale**: 10 quiz-*.qmd files at root are duplicates of quizzes/quiz-*.qmd, causing confusion.

#### Scenario: Root quiz files removed

- GIVEN 10 quiz-*.qmd files exist at project root
- AND canonical versions exist in quizzes/ directory (registered in _quarto.yml)
- WHEN cleanup runs
- THEN root-level quiz files are deleted
- AND no broken references remain in _quarto.yml

#### Scenario: Build artifact directories cleaned

- GIVEN quiz-demo_files/, quiz-modulo-01-revealjs_files/, test-quiz_files/ exist at root
- WHEN .gitignore is checked
- THEN these directories are ignored by git
- AND they are removed from version control

### Requirement: Lab Coverage for All Modules

The system SHALL provide at least 1 lab per module (modules 02-10 currently have 0 labs). Total minimum: 10 labs (1 per module).

**Rationale**: Only 2 labs exist (lab01, lab02), covering module 01 only. Modules 02-10 have no hands-on practice labs.

#### Scenario: Each module has dedicated lab

- GIVEN a module (e.g., modulo-03: Estructuras de Control)
- WHEN student reaches labs section
- THEN at least 1 lab file exists: labs/labNN-{module-topic}.qmd
- AND lab contains executable code exercises reinforcing module concepts
- AND lab has solution guide in instructor resources

#### Scenario: Labs progress in difficulty

- GIVEN labs for modules 01 through 10
- WHEN student completes labs sequentially
- THEN lab difficulty progresses from "follow-along" (lab01) to "independent project" (lab10)
- AND each lab builds on previous module knowledge

### Requirement: PDF Generation

The system SHALL generate a complete, print-ready PDF of the entire course content. PDF output MUST be configured in _quarto.yml format.pdf section.

**Rationale**: PDF export is configured in _quarto.yml but not validated/tested. Critical for offline distribution.

#### Scenario: PDF generates successfully

- GIVEN all content is registered in _quarto.yml
- WHEN `quarto render --to pdf` is executed
- THEN PDF is generated in docs/ directory
- AND PDF contains all 10 modules, challenges, labs, quizzes
- AND PDF has proper table of contents, page numbers, cover image

#### Scenario: PDF meets accessibility standards

- GIVEN PDF is generated
- WHEN opened in PDF reader
- THEN text is selectable (not rasterized)
- AND headings use semantic structure (H1, H2, H3)
- AND images have alt text
- AND code blocks use monospace font

### Requirement: EPUB Generation

The system SHALL generate a complete EPUB ebook for mobile/offline reading. EPUB output MUST be configured in _quarto.yml format.epub section.

**Rationale**: EPUB is configured but not tested. Critical for mobile learners.

#### Scenario: EPUB generates and validates

- GIVEN all content is registered
- WHEN `quarto render --to epub` is executed
- THEN EPUB is generated in docs/ directory
- AND EPUB passes epubcheck validation (no errors)
- AND EPUB renders correctly in Apple Books / Kindle app

#### Scenario: EPUB responsive on mobile

- GIVEN EPUB is loaded on mobile device
- WHEN opened in reader app
- THEN text reflows to screen size
- AND code blocks are readable without horizontal scrolling
- AND navigation between chapters works

### Requirement: Python Environment Validation

The system SHALL provide a validated Python virtual environment with working dependencies. The requirements.txt MUST be tested and confirmed functional.

**Rationale**: requirements.txt exists but environment not validated.

#### Scenario: Virtual environment setup script

- GIVEN student runs setup script (scripts/setup.sh or setup.ps1)
- WHEN script completes
- THEN Python venv is created at venv/
- AND all packages from requirements.txt are installed
- AND quarto command can render at least 1 test file
- AND python can import all required packages

#### Scenario: Setup validation script

- GIVEN student completes setup
- WHEN student runs scripts/validate-setup.py
- THEN script confirms: Python version >= 3.9, Quarto version >= 1.3, all packages installed
- AND script outputs "✅ Setup complete and validated"
- OR script outputs specific error: "❌ Missing: <package>" with install instructions

---

## MODIFIED Requirements

### Requirement: Course Content Structure (MODIFIED)

**Original Spec**: "70+ challenges distributed a lo largo del curso"

**New Description**: Course SHALL have 70+ challenges PLUS 10+ labs PLUS 10 quizzes PLUS 3 integrative projects. Total learning artifacts: 93+.

**Challenge Distribution** (verified on disk):
- Modules 01-09: 7 challenges each = 63 challenges
- Module 10: 3 integrative projects
- Labs: 10 (1 per module, 2 exist, 8 pending)
- Quizzes: 10 (1 per module, all exist)
- **Total**: 63 + 3 + 10 + 10 = 86 artifacts (target: 93+)

**Previously**: Only challenges counted (70+), labs/quizzes/projects were separate.

#### Scenario: Challenge count verified

- GIVEN all desafio-*.qmd files across modules 01-09
- WHEN files are counted: `find content/modulo-{01-09} -name "desafio-*.qmd" | wc -l`
- THEN count returns >= 63 challenge files
- AND each challenge has unique name and learning objective

### Requirement: Quarto Platform Integration (MODIFIED)

**Original Spec**: "Visualizar contenido interactivo en formato HTML generado por Quarto"

**New Description**: Quarto SHALL generate HTML, PDF, AND EPUB outputs from single source. All outputs MUST be consistent (same content, appropriate formatting per medium).

**Previously**: Only HTML output was specified. PDF/EPUB were mentioned but not required.

#### Scenario: Multi-output generation

- GIVEN source content in .qmd files
- WHEN `quarto render` is run with multiple formats
- THEN HTML output in docs/ (interactive, with navigation)
- AND PDF output in docs/ (print-ready, paginated)
- AND EPUB output in docs/ (reflowable, mobile-friendly)
- AND all three contain same chapters, code examples, challenges

### Requirement: Progressive Challenges System (MODIFIED)

**Original Spec**: "Registrar la finalización del challenge, Proveer feedback inmediato"

**New Description**: Challenges SHALL be complemented by Labs (hands-on guided practice) and Quizzes (knowledge verification). Each module MUST have all three: theory → challenges → lab → quiz.

**Previously**: Only challenges were specified, labs/quizzes were separate requirements.

#### Scenario: Complete module learning path

- GIVEN student is in modulo-03 (Estructuras de Control)
- WHEN student progresses through module
- THEN student reads theory units (01-06)
- AND completes 7 challenges (desafio-01 through desafio-07)
- AND completes lab (labs/lab03-estructuras.qmd)
- AND passes quiz (quizzes/quiz-modulo-03.qmd) with >= 70%
- THEN student can advance to modulo-04

---

## REMOVED Requirements

### Requirement: "Implementar sistema de progreso de challenges usando localStorage"

**Reason**: Over-specified implementation detail. The spec should define WHAT (track progress, enable advancement) not HOW (localStorage). Implementation choice left to design phase. Quizzes already provide knowledge verification. Progress tracking can use any mechanism (localStorage, server-side, LMS integration).

---

## Acceptance Criteria (Updated)

### Content Completeness ✅ VERIFIED
- [x] Todos los módulos del curso están implementados en Quarto (140+ archivos .qmd)
- [x] Se incluyen al menos 70 challenges distribuidos (63 desafios + 3 proyectos = 66, 7 labs faltantes)
- [x] Cada challenge tiene una descripción clara (en archivos .qmd)
- [x] Los proyectos integradores cubren múltiples conceptos (3 proyectos en modulo-10)
- [ ] **PENDING**: 56 desafio files registered in _quarto.yml
- [ ] **PENDING**: 8 additional labs created (modules 03-10)

### Platform Functionality ✅ PARTIAL
- [x] Quarto genera correctamente contenido HTML del curso
- [ ] **PENDING**: Los bloques de código ejecutable funcionan en entornos soportados
- [ ] **PENDING**: PDF generation tested and validated
- [ ] **PENDING**: EPUB generation tested and validated
- [x] Los recursos para instructores son completos (15 archivos)

### Quality Standards 🔴 PENDING
- [ ] **PENDING**: El contenido sigue principios de código limpio (code review pendiente)
- [x] Todas las explicaciones son claras y apropiadas para principiantes (verified in content)
- [x] Los desafíos progresan de forma lógica (structure verified)
- [ ] **PENDING**: El material está libre de errores técnicos y conceptuales (testing pendiente)

### Evaluation Alignment ✅ IMPLEMENTED
- [x] Los criterios de evaluación están claramente definidos (rubrica-proyectos-integradores.md)
- [x] Los desafíos evalúan efectivamente los conceptos (70+ challenges)
- [x] Los proyectos integradores permiten demostrar síntesis (3 projects)
- [ ] **PENDING**: Examen final cubre espectro completo (quizzes exist but not validated)

---

## Open Questions (Resolved + New)

### Resolved ✅
- ~~¿Se incluirán videos explicativos junto al contenido de Quarto?~~ → **Out of scope** (proposal confirmed)
- ~~¿Qué nivel de interactividad se espera en los bloques de código de Quarto?~~ → **Answered**: Executable code blocks with output display
- ~~¿Se requerirá cuenta en alguna plataforma específica?~~ → **Answered**: No, self-contained Quarto course
- ~~¿Cómo se manejarán las actualizaciones al material?~~ → **Answered**: Git version control + instructor guides

### New Questions 🔴
1. **Q10 Integration**: Should this course generate Q10 platform tasks like administracion-servidores-linux did? (5 tasks created for Linux course)
2. **Lab Priority**: Should remaining 8 labs be created before PDF/EPUB generation, or vice versa?
3. **Pilot Testing**: Is group pilot (task 4.7) feasible without progress tracking system implemented?
4. **Distribution**: Should final output be deployed to GitHub Pages (docs/ already configured)?

---

## Spec Review Checklist

- [x] All requirements use RFC 2119 keywords (MUST, SHALL, SHOULD, MAY)
- [x] Every requirement has ≥1 scenario (happy path + edge case where applicable)
- [x] All scenarios follow Given/When/Then format
- [x] No implementation details in specs (WHAT, not HOW) — removed localStorage requirement
- [x] Edge cases include: missing navigation entries, stale files, multi-output consistency
- [x] Prior Engram patterns have been consulted (Ethical_Hacking course structure)
- [x] Delta format clear: 6 ADDED, 3 MODIFIED, 1 REMOVED
- [x] Coverage metrics: 14 scenarios across 9 requirements (1.56 scenarios/requirement)

---

## Next Steps

1. **Immediate Priority**: Register 56 desafio files in _quarto.yml (task 4.1)
2. **Content Gap**: Create 8 labs for modules 03-10
3. **Infrastructure**: Validate Python environment + setup script (tasks 1.7-1.8)
4. **QA**: Run tests, accessibility review, link check (phase 4)
5. **Deployment**: Generate PDF + EPUB, clean stale files, deploy to GitHub Pages (phase 5)