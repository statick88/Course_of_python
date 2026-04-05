# 📊 Rúbrica de Evaluación — Módulo 10: Proyecto Integrador

## Instrucciones para el evaluador

Esta rúbrica se aplica a **cualquiera de los tres proyectos** del Módulo 10. Cada criterio se evalúa en una escala de 0 a 4 puntos.

## Escala de evaluación

| Puntuación | Nivel | Descripción |
|------------|-------|-------------|
| 4 | Excelente | Supera las expectativas. Código profesional. |
| 3 | Competente | Cumple todos los requisitos. Código funcional y limpio. |
| 2 | En desarrollo | Cumple la mayoría de requisitos. Algunos errores menores. |
| 1 | Principiante | Cumple requisitos mínimos. Errores significativos. |
| 0 | Insuficiente | No cumple los requisitos básicos. |

## Criterios de evaluación

### 1. Funcionalidad (30%)

| Puntos | Criterio |
|--------|----------|
| 4 | Todas las funcionalidades obligatorias y opcionales funcionan perfectamente |
| 3 | Todas las funcionalidades obligatorias funcionan correctamente |
| 2 | La mayoría de funcionalidades obligatorias funcionan, con errores menores |
| 1 | Solo algunas funcionalidades obligatorias funcionan |
| 0 | El programa no funciona o tiene errores críticos |

**Evidencia a buscar:**
- ¿El programa se ejecuta sin crashes?
- ¿Todas las opciones del menú funcionan?
- ¿Los datos se guardan y cargan correctamente?
- ¿Las operaciones CRUD (crear, leer, actualizar, eliminar) funcionan?

### 2. Estructura y organización del código (20%)

| Puntos | Criterio |
|--------|----------|
| 4 | Módulos bien separados, cada uno con responsabilidad clara. Código sigue PEP 8 perfectamente |
| 3 | Buena separación en módulos. Código sigue PEP 8 con excepciones menores |
| 2 | Algo de código en módulos incorrectos. Algunas violaciones de PEP 8 |
| 1 | Mayoría del código en un solo archivo. Poca organización |
| 0 | Todo en un archivo sin estructura |

**Evidencia a buscar:**
- ¿Existen los archivos esperados (`main.py`, `modulos/`, `datos/`)?
- ¿Cada módulo tiene una responsabilidad clara?
- ¿`main.py` solo orquesta y no implementa lógica?
- ¿Se siguen las convenciones de Python (snake_case, indentación)?

### 3. Manejo de datos y persistencia (15%)

| Puntos | Criterio |
|--------|----------|
| 4 | Persistencia perfecta. Datos se guardan y cargan sin pérdida. Manejo elegante de archivos inexistentes |
| 3 | Persistencia funcional. Datos se guardan y cargan correctamente |
| 2 | Persistencia básica. Algunos datos se pierden o hay errores menores |
| 1 | Persistencia parcial. Funciona pero con problemas |
| 0 | No hay persistencia de datos |

**Evidencia a buscar:**
- ¿Los datos persisten al cerrar y reabrir el programa?
- ¿Se maneja el caso de archivo inexistente?
- ¿El formato de datos (JSON/CSV) es correcto y legible?
- ¿Se crea el directorio de datos si no existe?

### 4. Validación y manejo de errores (15%)

| Puntos | Criterio |
|--------|----------|
| 4 | Todas las entradas del usuario se validan. Mensajes de error claros y útiles. El programa nunca se bloquea |
| 3 | La mayoría de entradas se validan. Mensajes de error adecuados |
| 2 | Validación básica. Algunos casos de error no manejados |
| 1 | Validación mínima. El programa puede bloquearse con entrada inválida |
| 0 | No hay validación de entrada |

**Evidencia a buscar:**
- ¿Qué pasa si el usuario ingresa texto en vez de número?
- ¿Qué pasa si el usuario ingresa un ID que no existe?
- ¿Qué pasa si el archivo de datos está corrupto?
- ¿Los mensajes de error son claros y en español?

### 5. Documentación (10%)

| Puntos | Criterio |
|--------|----------|
| 4 | README profesional completo. Docstrings en todas las funciones. Comentarios explicativos donde es necesario |
| 3 | README completo. Docstrings en la mayoría de funciones |
| 2 | README básico. Algunos docstrings |
| 1 | README mínimo. Sin docstrings |
| 0 | Sin documentación |

**Evidencia a buscar:**
- ¿El README explica qué hace el proyecto?
- ¿El README incluye instrucciones de uso?
- ¿Las funciones tienen docstrings con descripción, args y returns?
- ¿Los comentarios explican el "por qué", no el "qué"?

### 6. Creatividad y funcionalidades extra (10%)

| Puntos | Criterio |
|--------|----------|
| 4 | 4-5 funcionalidades extra implementadas y funcionando. Innovación notable |
| 3 | 3 funcionalidades extra implementadas. Buenas adiciones |
| 2 | 2 funcionalidades extra implementadas |
| 1 | 1 funcionalidad extra implementada |
| 0 | Solo lo mínimo requerido |

**Evidencia a buscar:**
- ¿Se implementaron funcionalidades opcionales?
- ¿Las funcionalidades extra son útiles y bien integradas?
- ¿Hay evidencia de pensamiento creativo en la solución?

## Cálculo de la nota final

```
Nota = (Funcionalidad × 0.30) + (Estructura × 0.20) + (Persistencia × 0.15) +
       (Validación × 0.15) + (Documentación × 0.10) + (Creatividad × 0.10)
```

| Rango | Calificación |
|-------|--------------|
| 3.6 - 4.0 | Excelente (A) |
| 2.8 - 3.5 | Competente (B) |
| 2.0 - 2.7 | En desarrollo (C) |
| 1.0 - 1.9 | Principiante (D) |
| 0.0 - 0.9 | Insuficiente (F) |

## Observaciones del evaluador

```
Fortalezas del proyecto:
_________________________________________________
_________________________________________________

Áreas de mejora:
_________________________________________________
_________________________________________________

Comentarios adicionales:
_________________________________________________
_________________________________________________
```

---

> **Readability counts.** Un proyecto bien documentado y organizado siempre será mejor evaluado que uno que solo "funciona".
