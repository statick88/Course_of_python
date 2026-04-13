# Tarea 4: Calculadora Modular con Funciones

**Módulo de referencia**: Módulo 4 - Funciones
**Unidad**: 4.1 Definir Funciones
**Dificultad**: ⭐⭐ Intermedio
**Tiempo estimado**: 60 minutos

## Descripción

Construye una calculadora que use funciones separadas para cada operación, aplicando el principio de responsabilidad única.

## Requisitos

1. Crea las siguientes funciones:
   ```python
   def sumar(a, b): ...
   def restar(a, b): ...
   def multiplicar(a, b): ...
   def dividir(a, b): ...
   def potencia(base, exponente): ...
   def raiz_cuadrada(numero): ...
   ```

2. Menú interactivo que permita elegir operación
3. Cada función debe incluir validación:
   - No dividir por cero
   - No raíz cuadrada de negativos
4. El programa se repite hasta que el usuario quiera salir

## Criterios de Éxito

- [ ] Cada operación es una función separada
- [ ] Validación de errores en cada función
- [ ] Menú claro y funcional
- [ ] Docstrings en todas las funciones

## Recursos

- [Módulo 4: Funciones](../content/modulo-04/index.qmd)
- [Desafío 7: Calculadora Funciones](../content/modulo-04/desafio-07-calculadora-funciones.qmd)
- [Lab 4: Funciones](../labs/lab04-funciones.qmd)

---

**Entrega**: Archivo `calculadora-modular.py`
**Fecha límite**: Semana 4
