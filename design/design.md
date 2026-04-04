# Technical Design: Programación Python Fundamentos con Quarto

## Architecture Decisions

### 1. Platform Selection: Quarto
**Decision**: Utilizar Quarto como plataforma principal de entrega de contenido educativo.
**Justification**: 
- Quarto permite crear contenido reproducible que combina texto, código y resultados
- Soporta múltiples formatos de salida (HTML, PDF, ePub) desde una sola fuente
- Integración nativa con kernels de Python para ejecución de código en vivo
- Basado en Pandoc y Markdown, familiar para la comunidad técnica
- Código abierto y activamente mantenido

### 2. Course Structure: Modular Progresiva
**Decision**: Organizar el curso en 10 módulos progresivos siguiendo la estructura de la propuesta original.
**Justification**:
- Permite una curva de aprendizaje adecuada para principiantes
- Cada módulo construye sobre los conceptos aprendidos previamente
- Facilita la planificación y seguimiento del progreso
- Alineado con las mejores prácticas de diseño instruccional

### 3. Learning Materials Organization
**Decision**: Estructura de directorios que separa claramente los diferentes tipos de contenido.
**Justification**:
- Mejora la mantenibilidad y escalabilidad del curso
- Facilita la colaboración entre múltiples instructores
- Permite reutilizar componentes en futuras ediciones
- Seguir convenciones estándar de proyectos educativos técnicos

### 4. Progressive Challenges System
**Decision**: Implementar un sistema de challenges con seguimiento de progreso y feedback inmediato.
**Justification**:
- Basado en la metodología probada de 70+ challenges de Diego Saavedra
- El aprendizaje activo mejora la retención y comprensión
- El feedback inmediato corrige errores antes de que se conviertan en hábitos
- Permite adaptar la dificultad al ritmo de cada estudiante

### 5. Evaluation Approach
**Decision**: Sistema de evaluación múltiple que combina participación, challenges, proyecto integrador y examen.
**Justification**:
- Evalúa diferentes aspectos del aprendizaje (teórico, práctico, aplicativo)
- Reduce la dependencia de un único tipo de evaluación
- Proporciona múltiples oportunidades para demostrar el aprendizaje
- Alineado con las mejores prácticas de evaluación educativa

## Directory Structure

```
course_of_python/
├── .git/                           # Repositorio Git
├── .quarto/                        # Configuración local de Quarto
├── assets/                         # Recursos estáticos (imágenes, iconos, etc.)
│   ├── images/                     # Ilustraciones y diagramas
│   ├── icons/                      # Iconos para la interfaz
│   └── styles/                     # CSS personalizado
├── content/                        # Contenido principal del curso
│   ├── modules/                    # Módulos del curso (1-10)
│   │   ├── module-01/              # Módulo 1: Introducción a Python
│   │   │   ├── index.qmd           # Página principal del módulo
│   │   │   ├── lessons/            # Lecciones individuales
│   │   │   │   ├── lesson-01.qmd   # Historia y evolución de Python
│   │   │   │   ├── lesson-02.qmd   # Instalación y configuración
│   │   │   │   └── ...
│   │   │   ├── labs/               # Laboratorios prácticos
│   │   │   │   ├── lab-01.qmd      # Primer programa: Hola Mundo
│   │   │   │   ├── lab-02.qmd      # Variables y tipos de datos
│   │   │   │   └── ...
│   │   │   ├── challenges/         # Challenges del módulo
│   │   │   │   ├── challenge-01.qmd
│   │   │   │   ├── challenge-02.qmd
│   │   │   │   └── ...
│   │   │   └── resources/          # Recursos específicos del módulo
│   │   │       ├── datasets/       # Conjuntos de datos para ejercicios
│   │   │       ├── templates/      # Plantillas de código
│   │   │       └── references/     # Bibliografía y enlaces útiles
│   │   └── ...
│   ├── instructor/                 # Recursos para instructores
│   │   ├── lesson-plans/           # Planes de sesión detallados
│   │   ├── solutions/              # Soluciones a challenges y ejercicios
│   │   ├── rubrics/                # Rúbricas de evaluación
│   │   ├── presentations/          # Presentaciones para usar en clase
│   │   ├── faq/                    # Preguntas frecuentes
│   │   └── troubleshooting/        # Guías de solución de problemas
│   └── shared/                     # Recursos compartidos entre módulos
│       ├── code-snippets/          # Fragmentos de código reutilizables
│       ├── datasets/               # Datasets comunes
│       └── templates/              # Plantillas de documentos
├── output/                         # Contenido generado (HTML, PDF, etc.)
│   ├── html/                       # Versión web del curso
│   ├── pdf/                        # Versión imprimible del curso
│   └── epub/                       # Versión ePub del curso
├── scripts/                        # Scripts de automatización y utilidades
│   ├── build/                      # Scripts de construcción del curso
│   ├── deploy/                     # Scripts de despliegue
│   ├── validate/                   # Scripts de validación
│   └── utils/                      # Funciones utilitarias
├── tests/                          # Tests para validar contenido y funcionalidad
│   ├── unit/                       # Tests unitarios
│   ├── integration/                # Tests de integración
│   └── acceptance/                 # Tests de aceptación
├── config/                         # Archivos de configuración
│   ├── quarto/                     # Configuración específica de Quarto
│   ├── build/                      # Configuración de construcción
│   └── deploy/                     # Configuración de despliegue
├── docs/                           # Documentación del proyecto
│   ├── architecture/               # Decisiones de arquitectura
│   ├── api/                        # Documentación de APIs internas
│   └── user-guides/                # Guías para usuarios finales
├── .quarto.yml                     # Configuración principal de Quarto
├── README.md                       # Descripción del proyecto
├── LICENSE                         # Licencia del curso
└── CONTRIBUTING.md                 # Guía para contribuir al curso
```

## Technology Stack

### Core Technologies
- **Quarto 1.3+**: Plataforma de publicación científica y técnica
- **Python 3.9+**: Lenguaje de programación enseñado
- **Jupyter Kernel**: Para ejecución de código en vivo en Quarto
- **VS Code**: IDE recomendado para desarrollo

### Development & Build Tools
- **Git**: Control de versiones
- **Make** o **npm scripts**: Automatización de tareas
- **HTMLMinifier**: Optimización de salida HTML
- **CSSMinifier**: Optimización de estilos
- **ImageOptim**: Optimización de imágenes

### Quality Assurance
- **HTML Validator**: Validación de salida HTML
- **Link Checker**: Verificación de enlaces rotos
- **Spell Checker**: Ortografía y gramática
- **Accessibility Checker**: Verificación WCAG 2.1
- **Python Linters**: Flake8, Black, Ruff para validar código de ejemplo

## Implementation Approach

### Phase 1: Foundation Setup
1. Configurar repositorio Git y estructura de directorios
2. Instalar y configurar Quarto con kernels de Python
3. Crear plantillas base para lecciones y laboratorios
4. Establecer guías de estilo y convenciones de nombrado

### Phase 2: Content Development
1. Desarrollar contenido teórico para cada módulo en Quarto
2. Crear demostraciones de código ejecutable
3. Diseñar challenges progresivos con soluciones
4. Desarrollar materiales de apoyo (datasets, referencias)

### Phase 3: Instructor Resources
1. Crear planes de sesión detallados
2. Desarrollar soluciones a todos los challenges
3. Crear rúbricas de evaluación para proyectos
4. Desarrollar guías de troubleshooting y FAQ

### Phase 4: Quality Assurance & Testing
1. Implementar tests para validar contenido y funcionalidad
2. Realizar revisiones de accesibilidad y usabilidad
3. Probar en múltiples navegadores y dispositivos
4. Validar con grupo piloto de estudiantes

### Phase 5: Deployment Preparation
1. Generar versiones finales en HTML, PDF y ePub
2. Crear guías de instalación y configuración
3. Empaquetar recursos para distribución
4. Preparar materiales de marketing y documentación

## Standards and Conventions

### Naming Conventions
- **Archivos Quarto**: kebab-case (ej. `introduccion-python.qmd`)
- **Directorios**: kebab-case (ej. `manejode-archivos/`)
- **Variables de código**: snake_case (ej. `numero_usuarios`)
- **Funciones**: snake_case (ej. `calcular_factorial()`)
- **Clases**: PascalCase (ej. `ClasePersona`)
- **Constantes**: UPPER_SNAKE_CASE (ej. `MAX_INTENTOS`)

### Code Style
- Seguir PEP 8 para código Python
- Máximo 79 caracteres por línea
- Indentación de 4 espacios
- Importaciones agrupadas y ordenadas
- Docstrings en formato Google o NumPy

### Quarto Specific
- Usar bloques de código con etiquetas específicas:
  ```{python}
  # Código ejecutable
  ```
- Bloques de salida:
  ```{python}
  # Código que genera salida
  ```
  ```
  # Salida esperada
  ```
- Bloques de advertencia:
  ::: {.callout-warning}
  Contenido de advertencia
  :::
- Bloques de información:
  ::: {.callout-tip}
  Consejo o información adicional
  :::

### Accessibility
- Contraste mínimo de 4.5:1 para texto normal
- Contraste mínimo de 3:1 para texto grande
- Texto alternativo descriptivo para todas las imágenes
- Navegación completa por teclado
- Etiquetas ARIA apropiadas para componentes interactivos
- Estructura semántica con encabezados h1-h6 apropiados

## Risk Mitigation

### Technical Risks
- **Problemas de compatibilidad de Quarto**: Mantener versión LTS y probar exhaustivamente
- **Conflictos de dependencias de Python**: Usar entornos virtuales y archivos requirements.txt
- **Fallos en ejecución de código**: Proveer ejecuciones alternativas y capturas de pantalla esperadas

### Pedagogical Risks
- **Sobrecarga cognitiva**: Aplicar progresión cuidadosa y chunking de información
- **Desmotivación**: Incorporar logros visibles y retroalimentación positiva
- **Brechas de conocimiento**: Diseñar desafíos que identifiquen y llenen gaps de comprensión

### Operational Risks
- **Deserción estudiantil**: Implementar seguimiento proactivo y soporte temprano
- **Problemas técnicos**: Tener guías de troubleshooting y soporte disponible
- **Actualizaciones de contenido**: Establecer proceso claro para revisiones y actualizaciones

## Success Metrics

### Learning Outcomes
- Porcentaje de challenges completados (>85%)
- Calificación promedio en proyecto integrador (>75%)
- Puntuación en examen final (>70%)
- Retención de conocimientos a 3 meses (>70%)

### Engagement Metrics
- Asistencia a sesiones sincrónicas (>80%)
- Tiempo dedicado por challenge (appropriado a dificultad)
- Participación en foros y discusiones
- Encuestas de satisfacción (>4/5)

### Quality Metrics
- Errores técnicos en material (<5 por módulo)
- Enlaces rotos (0%)
- Cumplimiento de accesibilidad WCAG 2.1 AA
- Tiempo de carga de página (<3s)

## Open Questions

1. ¿Qué nivel de interactividad se espera en los bloques de código de Quarto?
2. ¿Se incluirán videos explicativos pre-grabados junto al contenido de Quarto?
3. ¿Qué plataforma se usará para hospedar la versión en línea del curso?
4. ¿Cómo se manejará el seguimiento de progreso de los estudiantes (base de datos, localStorage, etc.)?
5. ¿Se requerirá autenticación para acceder a ciertos materiales del curso?
