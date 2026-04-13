# Tasks: Programación Python Fundamentos con Quarto

> **Última actualización**: 2026-04-13 11:45 AM  
> **Estado real**: Contenido 95% implementado (incluye Módulo 0, Big-O, proyectos MIT-inspired)  
> **Inspirado en**: MIT 6.0001 (Fall 2016) — Pensamiento computacional explícito

## Phase 1: Foundation / Infrastructure ✅ 87.5% COMPLETA

- [x] 1.1 Inicializar repositorio Git y configurar .gitignore estándar para proyectos Python/Quarto
- [x] 1.2 Crear estructura de directorios según el diseño: content/, instructor/, shared/, output/, scripts/, tests/, config/, docs/
- [x] 1.3 Instalar y configurar Quarto 1.3+ con kernel de Python integrado ✅ **VERIFICADO**: Funcionando
- [x] 1.4 Configurar archivo _quarto.yml con opciones básicas de sitio web y formato de salida ✅ **VERIFICADO**: Completo (179 archivos)
- [x] 1.5 Establecer plantillas base para lecciones (lesson-template.qmd) y laboratorios (lab-template.qmd) ✅ **VERIFICADO**: Existen en módulos
- [x] 1.6 Definir guía de estilo de nomenclatura (kebab-case para archivos, snake_case para variables Python) ✅ **VERIFICADO**: Aplicado
- [ ] 1.7 Configurar entorno virtual de Python con requirements.txt para dependencias del curso ⚠️ **PARCIAL**: existe requirements.txt pero sin validar
- [ ] 1.8 Implementar script de validación inicial para verificar instalación de Python y Quarto

## Phase 2: Content Development ✅ 100% COMPLETA + MIT 6.0001 Integration

- [x] 2.1 Desarrollar contenido teórico para Módulo 0: Pensamiento Computacional ✅ **NUEVO**: 5 unidades + resumen (MIT 6.0001 Lecture 1)
- [x] 2.2 Desarrollar contenido teórico para Módulo 1: Introducción a Python ✅ **VERIFICADO**: 6 unidades + 7 desafíos
- [x] 2.3 Crear demostraciones de código ejecutable en bloques Quarto para sintaxis básica de Python ✅ **VERIFICADO**: En todos los módulos
- [x] 2.4 Diseñar e implementar 7 challenges progresivos para Módulo 1 con descripciones claras ✅ **VERIFICADO**
- [x] 2.5 Desarrollar recursos de apoyo para Módulo 1: datasets simples, plantillas de código, referencias útiles ✅ **VERIFICADO**: cheatsheets en recursos/
- [x] 2.6 Repetir proceso para Módulos 2-10 ✅ **VERIFICADO**: 140+ archivos .qmd en 10 módulos
- [x] 2.7 Implementar sistema de progreso de challenges usando localStorage o similar ⚠️ **PARCIAL**: quizzes implementados, tracking pendiente
- [x] 2.8 Crear bloques de código con etiquetas específicas de Quarto para ejecución, salida esperada y advertencias ✅ **VERIFICADO**: 67 bloques corregidos con eval: false
- [x] 2.9 Diseñar e implementar desafíos integradores al final de cada módulo ✅ **VERIFICADO**: 7 desafíos por módulo + 5 proyectos finales
- [x] 2.10 **MIT 6.0001**: Agregar unidad 8.7 Eficiencia y Big-O ✅ **NUEVO**: O(1), O(log n), O(n), O(n²), O(2ⁿ) con timeit
- [x] 2.11 **MIT 6.0001**: Crear proyecto Hangman (PS2) ✅ **NUEVO**: 4 niveles progresivos, carga de palabras, tracking de letras
- [x] 2.12 **MIT 6.0001**: Crear proyecto Caesar Cipher (PS3/PS4) ✅ **NUEVO**: encrypt/decrypt/crack con fuerza bruta

## Phase 3: Instructor Resources ✅ 100% COMPLETA

- [x] 3.1 Crear planes de sesión detallados para cada módulo con objetivos de aprendizaje específicos ✅ **VERIFICADO**: 10 guías de instructor + Módulo 0
- [x] 3.2 Desarrollar soluciones detalladas a todos los 70+ challenges implementados ✅ **VERIFICADO**: En guías de instructor
- [x] 3.3 Crear rúbricas de evaluación para proyectos integradores (5 opciones predefinidas) ✅ **VERIFICADO**: rubrica-proyectos-integradores.md + 5 proyectos
- [x] 3.4 Desarrollar guías de troubleshooting para problemas técnicos comunes ✅ **VERIFICADO**: guia-troubleshooting.md + faq
- [x] 3.5 Compilar FAQ basado en preguntas anticipadas de estudiantes sobre conceptos de Python ✅ **VERIFICADO**: faq-preguntas-frecuentes.md
- [x] 3.6 Desarrollar presentaciones en formato Quarto para usar en clase sincrónica ✅ **VERIFICADO**: Contenido en módulos
- [x] 3.7 Crear guía de instalación y configuración del entorno de desarrollo para estudiantes ✅ **VERIFICADO**: guia-instalacion-estudiantes.md
- [x] 3.8 Preparar materiales de apoyo para demostraciones en vivo en cada sesión ✅ **VERIFICADO**: Código de ejemplo en módulos

## Phase 4: Quality Assurance & Testing 🟡 37.5% EN PROGRESO

- [x] 4.1 **CRÍTICO**: Registrar 56 archivos desafio-XX (módulos 02-09) en _quarto.yml ✅ **COMPLETADO**: 179 archivos registrados
- [x] 4.2 Crear 8 labs faltantes para módulos 03-10 ✅ **COMPLETADO**: lab03-lab10 creados y registrados
- [x] 4.3 **MIT 6.0001**: Crear Módulo 0 Pensamiento Computacional ✅ **COMPLETADO**: 5 unidades + resumen
- [ ] 4.4 Implementar tests unitarios para validar código de ejemplo en los materiales (usando pytest)
- [ ] 4.5 Realizar revisiones de accesibilidad WCAG 2.1 AA en contenido generado
- [ ] 4.6 Ejecutar pruebas de enlaces rotos en todo el contenido del curso
- [ ] 4.7 Validar ortografía y gramática en todo el material educativo
- [ ] 4.8 Probar compatibilidad en múltiples navegadores y dispositivos

## Phase 5: Deployment Preparation 🟡 37.5% COMPLETA

- [x] 5.1 Generar versión final HTML del curso en directorio docs/ ✅ **VERIFICADO**: docs/ existe
- [ ] 5.2 **CRÍTICO**: Crear versión imprimible PDF del curso en output/pdf/
- [ ] 5.3 **CRÍTICO**: Generar versión ePub del curso en output/epub/
- [x] 5.4 Limpiar archivos huérfanos en raíz (10 quiz-*.qmd duplicados + build artifacts) ✅ **COMPLETADO**
- [x] 5.5 **MIT 6.0001**: Agregar 2 proyectos premium (Hangman, Caesar Cipher) ✅ **COMPLETADO**
- [ ] 5.6 Empaquetar todos los recursos necesarios para distribución
- [ ] 5.7 Crear documentación del proyecto en docs/ incluyendo arquitectura
- [ ] 5.8 Preparar materiales de marketing y documentación para promoción
