# Proposal: Programación Python Fundamentos con Quarto

## Intent

Crear un curso de Programación Python Fundamentos que utilize Quarto como plataforma de enseñanza, siguiendo la metodología de aprendizaje basado en retos de Diego Saavedra, transformando a principiantes en desarrolladores Python competentes mediante desafíos progresivos y buenas prácticas de código limpio.

## Scope

### In Scope
- Diseño de currículo de 50 horas para Python Fundamentos
- Integración de Quarto como plataforma principal de entrega de contenido
- 70+ challenges prácticos progresivos
- Materiales de estudio, repositorios de código y guías para instructores
- Sistema de evaluación basado en participación, desafíos, proyecto integrador y examen
- Guía logística para impartir el curso (duración, requisitos técnicos, inversión)

### Out of Scope
- Temas avanzados de Python como desarrollo web con Django/Flask
- Enseñanza de frameworks específicos de ciencia de datos (aunque se introdúcirán conceptos básicos)
- Certificaciones internacionales de Python
- Desarrollo de aplicaciones móviles con Python

## Capabilities

### New Capabilities
- `python-fundamentos-quarto`: Curso completo de Programación Python Fundamentos usando Quarto como plataforma de enseñanza

### Modified Capabilities
- Ninguno (este es un nuevo curso)

## Approach

Utilizar Quarto para crear una experiencia de aprendizaje interactiva que combine teoría, demostraciones en vivo y laboratorios prácticos. El curso seguirá la metodología de 70+ challenges de Diego Saavedra, donde cada concepto se introduce mediante analogías del mundo real antes de mostrar la sintaxis, seguido de práctica inmediata en laboratorios donde los estudiantes escriben y ejecutan código real en VS Code. Se enfatizará el principio "Code is Communication" con nombres reveladores y documentación viva.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `curso-python-fundamentos` | Nuevo | Creación completa del currículo, materiales y guías |
| `plataforma-quarto` | Nuevo | Implementación de Quarto como sistema de gestión de aprendizaje para el curso |
| `metodologia-abacom` | Modificado | Adaptación de la metodología existente para incorporar Quarto y enfoques de aprendizaje basado en retos |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Resistencia al cambio de plataformas tradicionales a Quarto | Medio | Proveer capacitación previa a instructores y demostrar beneficios de Quarto para educación técnica |
| Sobrecarga de contenido para principiantes | Bajo | Aplicar progresión cuidadosa de los challenges y enfocarse en conceptos fundamentales |
| Problemas técnicos con la configuración de entornos de desarrollo | Bajo | Proveer guías detalladas de instalación y soporte técnico durante el curso |
| Dificultad para evaluar proyectos integradores de forma consistente | Medio | Desarrollar rúbricas detalladas y ejemplos de proyectos aceptables |

## Rollback Plan

Mantener la plataforma actual de entrega de materiales mientras se prueba Quarto con un grupo piloto. Si surgen problemas significativos, continuar con la plataforma existente y posponer la implementación completa de Quarto hasta resolver los problemas identificados.

## Dependencies

- Quarto instalado y configurado en los sistemas de instructores y estudiantes
- Python 3.9+ instalado
- Visual Studio Code con extensiones recomendadas
- Conexión a internet estable para acceso a materiales y repositorios

## Success Criteria

- [ ] El 85% de los participantes completa al menos el 85% de los challenges propuestos
- [ ] El 80% de los participantes asiste al menos al 80% de las sesiones sincrónicas
- [ ] El 70% de los participantes obtiene una puntuación mínima del 70% en la evaluación general
- [ ] El 90% de los participantes califica el curso como efectivo o muy efectivo en encuestas de satisfacción
- [ ] Se entregan al menos 3 proyectos integradores funcionales que demuestren aplicación de conceptos aprendidos