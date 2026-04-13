# Tarea 5: Gestor de Inventario con Listas

**Módulo de referencia**: Módulo 5 - Listas y Tuplas
**Unidad**: 5.1 Crear Listas
**Dificultad**: ⭐⭐ Intermedio
**Tiempo estimado**: 75 minutos

## Descripción

Crea un sistema de inventario para una tienda pequeña usando listas y tuplas.

## Requisitos

1. Cada producto es una tupla: `(nombre, precio, stock)`
2. Funcionalidades:
   - Agregar producto
   - Eliminar producto por nombre
   - Actualizar stock
   - Mostrar inventario completo
   - Calcular valor total del inventario (precio × stock)
3. El inventario se almacena en una lista

## Ejemplo

```python
# Estructura interna
inventario = [
    ("Laptop", 999, 5),
    ("Mouse", 25, 50),
    ("Teclado", 45, 30)
]

# Valor total: (999*5) + (25*50) + (45*30) = $7,495
```

## Criterios de Éxito

- [ ] Productos como tuplas dentro de lista
- [ ] CRUD completo (Crear, Leer, Actualizar, Eliminar)
- [ ] Cálculo de valor total correcto
- [ ] Código limpio y documentado

## Recursos

- [Módulo 5: Listas y Tuplas](../content/modulo-05/index.qmd)
- [Desafío 7: Gestor Inventario](../content/modulo-05/desafio-07-gestor-inventario.qmd)
- [Lab 5: Listas y Tuplas](../labs/lab05-listas-tuplas.qmd)

---

**Entrega**: Archivo `gestor-inventario.py`
**Fecha límite**: Semana 5
