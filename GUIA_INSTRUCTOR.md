# Guía del Instructor — Programación Python Fundamentos

> **Curso**: Programación Python Fundamentos  
> **Duración**: 50 horas (~12 semanas, 4h/semana)  
> **Instructor**: Diego Saavedra  
> **Plataforma**: Quarto (libro interactivo)  
> **Público**: Principiantes absolutos a intermedios bajos  
> **Licencia**: CC BY-NC-SA 4.0

---

## 1. Visión del Curso

Este curso transforma a principiantes en programadores Python competentes mediante **70+ desafíos prácticos progresivos**, laboratorios guiados, quizzes de evaluación y 5 proyectos integradores (incluyendo 2 inspirados en MIT 6.0001).

**Filosofía de enseñanza**:
- **Aprender haciendo**: Teoría mínima → demostración → desafío → reflexión
- **Pensamiento computacional primero**: Antes de escribir código, diseña el algoritmo
- **Código limpio desde el día uno**: PEP8, nombres descriptivos, docstrings
- **Progresión gradual**: Cada módulo construye sobre el anterior

---

## 2. Estructura del Curso

| Módulo | Tema | Duración | Desafíos | Lab | Quiz |
|--------|------|----------|----------|-----|------|
| 0 | Pensamiento Computacional | 4h | 0 | N/A | N/A |
| 1 | Introducción a Python | 5h | 7 | ✅ | ✅ |
| 2 | Tipos de Datos y Variables | 4h | 7 | ✅ | ✅ |
| 3 | Estructuras de Control | 6h | 7 | ✅ | ✅ |
| 4 | Funciones | 6h | 7 | ✅ | ✅ |
| 5 | Listas y Tuplas | 4h | 7 | ✅ | ✅ |
| 6 | Diccionarios y Sets | 4h | 7 | ✅ | ✅ |
| 7 | Manejo de Archivos | 6h | 7 | ✅ | ✅ |
| 8 | Módulos y Paquetes | 6h | 7 | ✅ | ✅ |
| 9 | Buenas Prácticas | 5h | 7 | ✅ | ✅ |
| 10 | Proyecto Integrador | 4h | 5 proyectos | ✅ | ✅ |

**Total**: 11 módulos, 158 archivos, 63 desafíos, 10 labs, 12 quizzes, 5 proyectos.

---

## 3. Preparación de Sesiones

### Plantilla de Sesión (90 minutos)

| Tiempo | Actividad | Detalle |
|--------|-----------|---------|
| 0-10 min | **Enganche** | Pregunta provocadora o demo sorprendente del tema |
| 10-30 min | **Teoría** | Conceptos clave con ejemplos en vivo (no más de 20 min seguidos) |
| 30-55 min | **Desafío guiado** | Resolver juntos el primer desafío del módulo |
| 55-75 min | **Práctica independiente** | Estudiantes resuelven 1-2 desafíos solos |
| 75-85 min | **Revisión** | Compartir soluciones, discutir alternativas |
| 85-90 min | **Cierre** | Resumen de 3 puntos clave, preview del próximo módulo |

### Checklist Pre-Curso

- [ ] Python 3.9+ instalado en tu máquina
- [ ] VS Code con extensión Python instalado
- [ ] Repositorio del curso clonado localmente
- [ ] Curso renderizado con `quarto render --to html`
- [ ] Acceso al curso publicado verificado (GitHub Pages)
- [ ] Archivos de desafíos abiertos para referencia rápida
- [ ] Plan de la sesión preparado (qué módulos, qué desafíos)
- [ ] Evaluación de diagnóstico lista para nuevos estudiantes
- [ ] Lista de estudiantes con contacto y nivel actual

---

## 4. Estrategias de Enseñanza

### 4.1 Analogías del Mundo Real

| Concepto Python | Analogía | Cuándo usarla |
|----------------|----------|---------------|
| Variable | Caja etiquetada donde guardas algo | Módulo 1, primera mención |
| Lista | Mochila con compartimentos ordenados | Módulo 5, introducción |
| Diccionario | Agenda telefónica (nombre → datos) | Módulo 6, introducción |
| Función | Receta de cocina (ingredientes → plato) | Módulo 4, definición |
| Bucle for | Repetir una acción por cada elemento de una fila | Módulo 3, introducción |
| Bucle while | "Sigue hasta que..." (ej: mientras haya hambre, come) | Módulo 3, introducción |
| Módulo | Cajón de herramientas (cada herramienta es una función) | Módulo 8, import |

### 4.2 Técnica "Yo hago, Nosotros hacemos, Tú haces"

1. **Yo hago**: El instructor resuelve un desafío en vivo, pensando en voz alta
2. **Nosotros hacemos**: La clase resuelve el siguiente desafío juntos (instructor guía, estudiantes sugieren)
3. **Tú haces**: Cada estudiante resuelve un desafío independientemente

### 4.3 Manejo de Errores como Oportunidad

**Nunca borres un error del terminal.** Úsalo como momento de enseñanza:

1. Lee el error en voz alta
2. Pregunta: "¿Qué nos dice este mensaje?"
3. Identifica la línea problemática
4. Pregunta: "¿Qué esperábamos que pasara?"
5. Corrige y ejecuta de nuevo

### 4.4 Anti-AI: Verificación de Autoría

Los desafíos están diseñados con protección anti-IA. Para verificar autoría:

- **Pide al estudiante que explique** su solución línea por línea
- **Cambia un parámetro** del desafío y pide que adapten su solución
- **Pregunta "¿qué pasaría si...?"** para verificar comprensión profunda
- Si no puede explicar: **solución generada por IA**, no cuenta

---

## 5. Gestión de Laboratorios

### 5.1 Estructura de Lab Recomendada

Cada lab debe seguir esta estructura (ya implementada en los 10 labs):

1. **Objetivos** claros y medibles
2. **Prerrequisitos** verificados antes de empezar
3. **Pasos numerados** con tiempo estimado
4. **Troubleshooting**: tabla Problema → Solución
5. **Checklist de aceptación**: checkboxes verificables
6. **Reflexión**: 2-3 preguntas para consolidar aprendizaje

### 5.2 Cuándo Hacer Cada Lab

| Lab | Módulo | Momento Ideal |
|-----|--------|---------------|
| Lab 1: Primer Programa | 1 | Después de unidad 1.3 (Hola Mundo) |
| Lab 2: Variables en Acción | 2 | Después de unidad 2.2 (Operadores) |
| Lab 3: Estructuras de Control | 3 | Después de unidad 3.4 (While) |
| Lab 4: Funciones | 4 | Después de unidad 4.3 (Return) |
| Lab 5: Listas y Tuplas | 5 | Después de unidad 5.3 (Métodos) |
| Lab 6: Diccionarios y Sets | 6 | Después de unidad 6.2 (Acceder/Modificar) |
| Lab 7: Manejo de Archivos | 7 | Después de unidad 7.3 (Escribir) |
| Lab 8: Módulos y Paquetes | 8 | Después de unidad 8.4 (Paquetes) |
| Lab 9: Buenas Prácticas | 9 | Después de unidad 9.4 (Errores) |
| Lab 10: Proyecto Integrador | 10 | Al inicio del módulo (guía todo el proyecto) |

---

## 6. Evaluación

### 6.1 Sistema de Calificación

| Componente | Peso | Detalle |
|-----------|------|---------|
| **Participación** | 20% | Asistencia a sesiones sincrónicas, engagement |
| **Desafíos** | 30% | Completion rate de los 63 desafíos |
| **Labs** | 20% | 10 labs completados con checklist |
| **Proyecto Integrador** | 30% | 1 de 5 proyectos entregado funcionando |

### 6.2 Rúbrica de Proyectos

| Criterio | Peso | Excelente (100%) | Aceptable (70%) | Insuficiente (40%) |
|----------|------|-------------------|-----------------|-------------------|
| **Funcionalidad** | 30% | Todo funciona sin errores | Funciona con errores menores | No funciona |
| **Estructura** | 20% | Funciones separadas, código limpio | Algunas funciones, código aceptable | Todo en un bloque |
| **Documentación** | 15% | Docstrings en todas las funciones | Algunas docstrings | Sin documentación |
| **Manejo de errores** | 15% | Try/except en operaciones riesgosas | Algunos try/except | Sin manejo de errores |
| **Creatividad** | 10% | Funcionalidades extra no requeridas | Cumple lo requerido | No cumple lo mínimo |
| **Entrega** | 10% | Todo completo + video/demo | Todo completo | Incompleto |

### 6.3 Evaluación de Diagnóstico

Aplica el diagnóstico (`quizzes/evaluacion-diagnostico.qmd`) al inicio:

| Puntaje | Nivel | Acción |
|---------|-------|--------|
| 0-3 | Principiante absoluto | Acompañamiento extra en Módulo 0 |
| 4-6 | Principiante con nociones | Módulo 0 rápido, ritmo normal después |
| 7-9 | Intermedio bajo | Puede saltar Módulo 0 si quiere |
| 10-12 | Intermedio | Enfocar en desafíos avanzados y proyectos |

---

## 7. Troubleshooting Común del Curso

| Problema | Solución |
|----------|----------|
| Estudiante no puede instalar Python | Usar instalador oficial de python.org, NO Microsoft Store |
| VS Code no reconoce Python | Instalar extensión "Python" de Microsoft, reiniciar VS Code |
| `quarto render` falla | Verificar `quarto --version`, reinstalar si es < 1.3 |
| Desafío no se ve en navegación | Verificar que está registrado en `_quarto.yml` chapters |
| Código no ejecuta en Quarto | Verificar que tiene `#| eval: false` si usa `input()` |
| Estudiante usa IA para resolver | Aplicar verificación de autoría (explicación línea por línea) |
| Estudiante se frustra | Recordar: "El error es tu maestro. Si no hay error, no hay aprendizaje." |
| Estudiante va muy rápido | Asignar desafíos bonus o proyectos adicionales |
| Estudiante se queda atrás | Sesión 1:1 de 15 min, identificar gap específico |

---

## 8. Mejores Prácticas para el Instructor

### Hacer
- ✅ Demostrar código en vivo (no solo leerlo)
- ✅ Pensar en voz alta mientras programas
- ✅ Celebrar errores como oportunidades de aprendizaje
- ✅ Dar feedback específico, no genérico ("tu variable `x` debería llamarse `contador_intentos`")
- ✅ Conectar cada concepto con aplicaciones del mundo real
- ✅ Verificar comprensión pidiendo que expliquen con sus palabras

### No Hacer
- ❌ Leer slides sin demostrar código
- ❌ Resolver desafíos por los estudiantes (guiar, no hacer)
- ❌ Avanzar sin verificar que la mayoría entiende
- ❌ Ignorar a estudiantes silenciosos (preguntar directamente)
- ❌ Usar jerga técnica sin explicarla primero
- ❌ Permitir copy-paste de soluciones (deben teclear)

---

## 9. Recursos del Instructor

| Recurso | Ubicación | Propósito |
|---------|-----------|-----------|
| Soluciones de desafíos | En cada `.qmd` (detalles colapsables) | Verificación rápida |
| Guía de instalación | `instructor/guia-instalacion-estudiantes.md` | Soporte técnico |
| FAQ | `instructor/faq-preguntas-frecuentes.md` | Respuestas rápidas |
| Troubleshooting | `instructor/guia-troubleshooting.md` | Diagnóstico de problemas |
| Rúbrica proyectos | `instructor/rubrica-proyectos-integradores.md` | Evaluación objetiva |
| Evaluación diagnóstico | `quizzes/evaluacion-diagnostico.qmd` | Perfilamiento inicial |
| Quizzes por módulo | `quizzes/quiz-modulo-XX.qmd` | Evaluación continua |

---

## 10. Cronograma Sugerido (12 Semanas)

| Semana | Módulo | Hitos |
|--------|--------|-------|
| 1 | Módulo 0 + 1 | Diagnóstico aplicado, primer programa ejecutado |
| 2 | Módulo 2 | Variables y tipos dominados |
| 3 | Módulo 3 | Estructuras de control (if/for/while) |
| 4 | Módulo 4 | Funciones reutilizables |
| 5 | Módulo 5 | Listas y tuplas operativas |
| 6 | Módulo 6 | Diccionarios y sets |
| 7 | **Parcial** | Quiz acumulativo módulos 0-6 |
| 8 | Módulo 7 | Archivos CSV y JSON |
| 9 | Módulo 8 | Módulos propios y pip |
| 10 | Módulo 9 | Código limpio y testing |
| 11 | Módulo 10 | Inicio de proyecto integrador |
| 12 | Módulo 10 | **Entrega de proyecto** + cierre |

---

## 11. Contacto y Soporte

| Canal | Uso | Tiempo de respuesta |
|-------|-----|--------------------|
| **Email**: dsaavedra88@gmail.com | Dudas técnicas, agendar sesiones | 24 horas |
| **WhatsApp** | Urgencias, recordatorios | 2 horas |
| **Sesiones 1:1** | Estudiantes rezagados, mentoring | Agendar con 48h |

---

> "El mejor instructor no es el que más sabe, sino el que mejor ayuda a otros a descubrir lo que pueden aprender."
> — Diego Saavedra

**Última actualización**: 2026-04-13  
**Versión**: 1.0
