# Guía de Instalación para Estudiantes

## Requisitos del Sistema

### Mínimo
- **Sistema operativo**: Windows 10+, macOS 10.15+, Ubuntu 20.04+
- **RAM**: 4 GB
- **Espacio en disco**: 500 MB
- **Procesador**: Dual-core 1.6 GHz

### Recomendado
- **RAM**: 8 GB
- **Espacio en disco**: 1 GB
- **Conexión a internet**: Para instalar paquetes adicionales

---

## Paso 1: Instalar Python

### Windows

1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Ejecuta el instalador
3. **IMPORTANTE**: Marca la opción **"Add Python to PATH"**
4. Click en "Install Now"
5. Verifica la instalación:
   ```cmd
   python --version
   ```

### macOS

**Opción A - Instalador oficial:**
1. Descarga desde [python.org](https://www.python.org/downloads/macos/)
2. Ejecuta el instalador

**Opción B - Homebrew (recomendado):**
```bash
brew install python3
```

**Verificar:**
```bash
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

---

## Paso 2: Instalar VS Code

1. Descarga desde [code.visualstudio.com](https://code.visualstudio.com/Download)
2. Ejecuta el instalador
3. **Extensiones esenciales** (instala desde VS Code):
   - Python (Microsoft)
   - Pylance
   - Jupyter
   - Material Icon Theme

### Configuración de VS Code

1. Abre VS Code
2. Presiona `Ctrl + ,` (Windows) o `Cmd + ,` (macOS)
3. Busca y configura:
   - `Python: Default Interpreter Path`: `python3` (Linux/macOS) o `python` (Windows)
   - `Editor: Format On Save`: Activado
   - `Files: Auto Save`: `afterDelay`

---

## Paso 3: Crear Entorno Virtual (Recomendado)

### Windows

```cmd
cd tu_carpeta_de_proyecto
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
cd tu_carpeta_de_proyecto
python3 -m venv venv
source venv/bin/activate
```

---

## Paso 4: Instalar Paquetes del Curso

Con el entorno virtual activo:

```bash
pip install pytest ipython jupyter
```

---

## Paso 5: Descargar Materiales del Curso

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/python-fundamentos.git
cd python-fundamentos
```

2. O descarga el archivo ZIP desde el LMS

---

## Verificación de Instalación

Ejecuta este script para verificar que todo está correcto:

```python
# verificador.py
import sys
print(f"Python: {sys.version}")

try:
    import pytest
    print(f"pytest: {pytest.__version__}")
except ImportError:
    print("pytest: NO INSTALADO")

try:
    import jupyter
    print(f"jupyter: OK")
except ImportError:
    print("jupyter: NO INSTALADO")

print("\n✅ Instalación completa si ves Python y pytest")
```

Ejecuta:
```bash
python verificador.py
```

---

## Solución de Problemas Comunes

### "python no se reconoce como comando" (Windows)

**Solución:**
1. Busca "Variables de entorno" en Windows
2. Edita la variable PATH
3. Agrega: `C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python3XX\`

### Error de permisos al instalar paquetes (Linux)

```bash
sudo apt install python3-pip
```

### VS Code no detecta Python

1. Presiona `Ctrl + Shift + P`
2. Escribe "Python: Select Interpreter"
3. Selecciona tu instalación de Python

---

## Próximos Pasos

1. ✅ 完成 Instalación
2. 📖 Lee el Módulo 1: Introducción a Python
3. 💻 Completa el Laboratorio 1: Tu primer programa
4. 🎯 Intenta el Desafío 1: Saludo personalizado

---

## Soporte

Si tienes problemas:
- Revisa la sección de FAQ en el material del curso
- Pregunta en el grupo de WhatsApp del curso
- Consulta con tu instructor durante las sesiones