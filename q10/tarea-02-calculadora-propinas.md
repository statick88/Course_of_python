# Tarea 2: Calculadora de Propinas

**Módulo de referencia**: Módulo 2 - Tipos de Datos y Variables
**Unidad**: 2.1 Operadores Aritméticos
**Dificultad**: ⭐ Fácil
**Tiempo estimado**: 45 minutos

## Descripción

Crea una calculadora de propinas que ayude a los usuarios a calcular cuánto dejar de propina en un restaurante.

## Requisitos

1. Pide el total de la cuenta al usuario
2. Pide el porcentaje de propina deseado (10%, 15%, 20%)
3. Calcula:
   - Monto de la propina
   - Total a pagar (cuenta + propina)
4. Muestra el resultado formateado

## Ejemplo de Ejecución

```
=== Calculadora de Propinas ===

Total de la cuenta: $150.00
Porcentaje de propina (10/15/20): 15

--- Resumen ---
Cuenta: $150.00
Propina (15%): $22.50
Total a pagar: $172.50
```

## Criterios de Éxito

- [ ] El programa pide cuenta y porcentaje correctamente
- [ ] Calcula la propina con la fórmula: `propina = cuenta * (porcentaje / 100)`
- [ ] Muestra el total formateado con 2 decimales
- [ ] Maneja entradas inválidas (números negativos, texto)

## Recursos

- [Módulo 2: Tipos de Datos](../content/modulo-02/index.qmd)
- [Desafío 2: Conversor de Unidades](../content/modulo-02/desafio-02-conversor-unidades.qmd)

---

**Entrega**: Archivo `calculadora-propinas.py` funcionando
**Fecha límite**: Semana 2
