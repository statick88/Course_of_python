# Contribuyendo al Curso — Programación Python Fundamentos

¡Gracias por tu interés en contribuir! Este curso es un proyecto educativo abierto bajo licencia **CC BY-NC-SA 4.0**.

## ¿Cómo Puedes Contribuir?

### 1. Reportar Errores
- Errores tipográficos o gramaticales en el contenido
- Código de ejemplo que no funciona
- Enlaces rotos
- Explicaciones confusas

**Cómo**: Abre un [Issue](https://github.com/statick88/Course_of_python/issues) con el título `[Bug] Breve descripción`.

### 2. Sugerir Mejoras
- Nuevos desafíos o laboratorios
- Mejoras en explicaciones existentes
- Analogías adicionales
- Ejemplos del mundo real

**Cómo**: Abre un [Issue](https://github.com/statick88/Course_of_python/issues) con el título `[Enhancement] Breve descripción`.

### 3. Corregir Contenido
- Si encuentras un error y sabes cómo arreglarlo, haz un Pull Request.

### 4. Traducir
- Traducciones a otros idiomas son bienvenidas. Crea una carpeta `i18n/idioma/`.

## Proceso de Pull Request

1. **Fork** el repositorio
2. **Crea una branch**: `git checkout -b fix/nombre-del-cambio`
3. **Haz tus cambios** y haz commit: `git commit -m "fix: breve descripción"`
4. **Push** a tu fork: `git push origin fix/nombre-del-cambio`
5. **Abre un Pull Request** describiendo qué cambiaste y por qué

## Estándares de Código

- **Python**: Sigue PEP 8, usa `black` para formatear, `ruff` para linting
- **Quarto**: Líneas máximo 80 caracteres, código con `#| eval: false` si usa `input()`
- **Nombres de archivo**: `kebab-case.qmd` para contenido, `snake_case.py` para código Python
- **Commit messages**: Conventional Commits (`fix:`, `feat:`, `docs:`, `chore:`)

## Verificación y publicación

La publicación usa un único workflow: `.github/workflows/pages.yml`.
En **Settings → Pages → Source** seleccione **GitHub Actions**; no publique
la copia histórica de `main:/docs`. El workflow prueba las soluciones y los
fragmentos originales de las sesiones, renderiza HTML con `--no-execute` y
publica el artefacto `docs` después de un push a `main`. Los pull requests
verifican y renderizan, pero no despliegan.

Para comprobar cambios localmente en un entorno Python 3.14 aislado:

```bash
python3.14 -m venv .venv
.venv/bin/python -m pip install pytest hypothesis PyYAML
.venv/bin/python -m pytest -q tests
quarto render --to html --no-execute
```

No confirme el entorno virtual ni los archivos generados por una comprobación.
El render anterior actualiza `docs`: úselo en una copia de trabajo aislada si
necesita conservar el resultado local existente. Añada toda sesión publicable a
`book.chapters` en `_quarto.yml`; tener un archivo QMD no basta para publicarlo.
Las sesiones 1–10 están disponibles; 11–15 y la ruta complementaria siguen en
preparación. Mantenga accesibles los módulos iniciales al ampliar la ruta.

## Licencia

Al contribuir, aceptas que tu contribución será licenciada bajo **CC BY-NC-SA 4.0**.

---

*Última actualización: 2026-04-13*
