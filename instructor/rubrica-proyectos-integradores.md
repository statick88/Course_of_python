# Rúbrica de Evaluación — Proyectos Integradores (Módulo 10)

## Proyectos Disponibles

| # | Proyecto | Descripción | Complejidad |
|---|----------|-------------|-------------|
| 1 | Gestor de Tareas | CRUD de tareas con JSON | ⭐⭐ Media |
| 2 | Tienda de Productos | Inventario y ventas | ⭐⭐ Media |
| 3 | Analizador de Datos | CSV y estadísticas | ⭐⭐⭐ Alta |

---

## Criterios de Evaluación General

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Funcionalidad** | 30% | El programa funciona correctamente |
| **Estructura y Organización** | 20% | Código bien modularizado |
| **Calidad del Código** | 15% | Legibilidad, nombres, comentarios |
| **Manejo de Errores** | 15% | Validación y excepciones |
| **Documentación** | 10% | README, docstrings |
| **Creatividad/Extras** | 10% | Funcionalidades adicionales |

---

## Escala de Calificación

| Nivel | Puntuación | Descripción |
|-------|------------|-------------|
| **Excelente** | 90-100% | Supera todas las expectativas |
| **Bueno** | 75-89% | Cumple con todos los requisitos |
| **Satisfactorio** | 60-74% | Cumple con los requisitos básicos |
| **Necesita Mejorar** | < 60% | No cumple los requisitos mínimos |

---

## Rúbrica Detallada

### 1. Funcionalidad (30%)

| Nivel | Puntuación | Criterios |
|-------|------------|-----------|
| Excelente | 27-30 | Todas las funcionalidades obligatorias + extras funcionan perfectamente |
| Bueno | 22-26 | Todas las funcionalidades obligatorias funcionan, algunos extras |
| Satisfactorio | 18-21 | Mayoría de funcionalidades работают, algunos errores menores |
| Necesita Mejorar | 0-17 | Funcionalidades básicas no funcionan o muy incompletas |

**Funcionalidades Obligatorias - Gestor de Tareas:**
- [ ] Agregar tarea
- [ ] Listar tareas (todas y pendientes)
- [ ] Completar tarea
- [ ] Eliminar tarea
- [ ] Persistencia JSON
- [ ] Menú interactivo

### 2. Estructura y Organización (20%)

| Nivel | Puntuación | Criterios |
|-------|------------|-----------|
| Excelente | 18-20 | Módulos bien separados, responsabilidades claras, arquitectura limpia |
| Bueno | 14-17 | Algo de código en main pero mayoría modularizado |
| Satisfactorio | 10-13 | Código en 2-3 archivos, responsabilidades mezcladas |
| Necesita Mejorar | 0-9 | Todo en un archivo, sin estructura |

**Ejemplo de estructura esperada:**
```
gestor_tareas/
├── main.py          # Punto de entrada, menú
├── datos/
│   └── tareas.json  # Archivo de datos
└── modulos/
    ├── __init__.py
    ├── gestor.py    # Lógica de negocio
    └── utilidades.py # Funciones helper
```

### 3. Calidad del Código (15%)

| Nivel | Puntuación | Criterios |
|-------|------------|-----------|
| Excelente | 14-15 | Nombres descriptivos, funciones cortas, sin código redundante |
| Bueno | 11-13 | Buenos nombres, algunas funciones largas |
| Satisfactorio | 8-10 | Nombres aceptables, código repetido |
| Necesita Mejorar | 0-7 | Nombres poco claros (x, y, temp), código spaghetti |

**Checklist de calidad:**
- [ ] Variables con nombres descriptivos (`tarea` no `t`)
- [ ] Funciones con una sola responsabilidad
- [ ] Máximo 30 líneas por función
- [ ] Sin variables globales innecesarias
- [ ] Código DRY (Don't Repeat Yourself)

### 4. Manejo de Errores (15%)

| Nivel | Puntuación | Criterios |
|-------|------------|-----------|
| Excelente | 14-15 | Valida entrada del usuario, maneja todos los errores posibles |
| Bueno | 11-13 | Maneja errores principales, algunos casos no considerados |
| Satisfactorio | 8-10 | Algunos try/except pero incompletos |
| Necesita Mejorar | 0-7 | No maneja errores, programa crashea con entrada inválida |

**Errores a manejar:**
- Entrada inválida (texto donde se espera número)
- Archivo no existe al cargar
- Carpeta de datos no existe
- Identificador inválido
- División por cero

### 5. Documentación (10%)

| Nivel | Puntuación | Criterios |
|-------|------------|-----------|
| Excelente | 9-10 | README completo + docstrings en todas las funciones |
| Bueno | 7-8 | README básico + docstrings principales |
| Satisfactorio | 5-6 | Solo comentarios básicos |
| Necesita Mejorar | 0-4 | Sin documentación |

**README debe incluir:**
- Título y descripción del proyecto
- Instrucciones de instalación
- Cómo ejecutar el programa
- Funcionalidades disponibles
- Estructura de archivos

### 6. Creatividad/Extras (10%)

| Puntuación | Funcionalidades Extra |
|------------|----------------------|
| 10 | 5+ extras implementados |
| 8 | 3-4 extras |
| 5 | 1-2 extras |
| 0 | Solo lo mínimo |

**Extras sugeridos:**
- Estadísticas (total, pendientes, completadas, %)
- Filtrar por texto
- Fecha de creación automática
- Exportar a CSV
- Colores en terminal
- Buscar tarea por ID

---

## Ejemplo de Evaluación

### Proyecto: Gestor de Tareas (Estudiante: Juan Pérez)

| Criterio | Puntuación Posible | Puntuación Obtenida |
|----------|-------------------|---------------------|
| Funcionalidad | 30 | 28 (Todas las func. + 3 extras) |
| Estructura | 20 | 18 (Estructura perfecta) |
| Calidad código | 15 | 12 (Buena, algunas funciones largas) |
| Manejo errores | 15 | 13 (Maneja la mayoría) |
| Documentación | 10 | 8 (README + docstrings principales) |
| Creatividad | 10 | 8 (Estadísticas + colores) |
| **TOTAL** | **100** | **87** |

**Resultado: Bueno (87%)**

---

## Retroalimentación para el Estudiante

### fortalezas:
- ✅ Estructura de proyecto profesional
- ✅ Todas las funcionalidades obligatorias funcionan
- ✅ Implementó estadísticas y фильтрация

### Áreas de mejora:
- 📝 La función `guardar_tareas()` tiene 45 líneas, debería dividirse
- ⚠️ No maneja el caso cuando el archivo JSON está corrupto
- 📝 Falta docstring en `mostrar_menu()`

### Próximos pasos:
- Refactorizar funciones largas
- Agregar validación de JSON
- Completar documentación