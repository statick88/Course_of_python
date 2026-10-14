# Guía de Troubleshooting — Problemas Técnicos Comunes

## Instalación de Python

### Problema: "python no se reconoce como comando interno o externo"

**Windows:**
1. Busca "Variables de entorno" en el menú inicio
2. Click en "Editar variables de entorno del sistema"
3. Click en "Variables de entorno"
4. En "Variables del sistema", busca "Path"
5. Click en "Editar" → "Nuevo"
6. Agrega: `C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python3XX\`
7. Agrega también: `C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python3XX\Scripts\`

**Verifica** en una nueva terminal: `python --version`

---

### Problema: Error de permisos al instalar paquetes

**Linux:**
```bash
sudo apt update
sudo apt install python3-pip
pip install --user paquete
```

**macOS:**
```bash
brew install python3
```

---

### Problema: Versión incorrecta de Python

Verifica qué Python se ejecuta:
```bash
which python
which python3
python3 --version
```

Si tienes varias versiones y quieres cambiar el predeterminado:
- **Linux**: Actualiza el enlace simbólico o usa `alias python3=/ruta/nueva/version`
- **Windows**: Ajusta el PATH para que la versión deseada aparezca primero

---

## VS Code

### Problema: VS Code no detecta Python

1. Presiona `Ctrl + Shift + P` (Windows) o `Cmd + Shift + P` (macOS)
2. Escribe "Python: Select Interpreter"
3. Click en la opción y selecciona tu instalación de Python
4. Si no aparece,instala la extensión Python de Microsoft

---

### Problema: El depurador no funciona

1. Asegúrate de tener la extensión Python instalada
2. Crea un archivo de configuración de debug:
   - Click en "Run and Debug" (Ctrl + Shift + D)
   - Click en "create a launch.json file"
   - Selecciona "Python"
3. Verifica que el interpreter seleccionado sea correcto

---

### Problema: warnings de "Linting" constante

1. `Ctrl + ,` para abrir configuración
2. Busca "Python: Linting Enabled"
3. Desactiva si es muy molesto (no recomendado)
4. O selecciona un linter específico: "Python: Linting: Pylance"

---

## Errores de Código Frecuentes

### SyntaxError: invalid syntax

**Causa:** Error de escritura.

**Solución:**
- Verifica que todas las líneas terminen correctamente
- Asegúrate de tener `:` al final de: `if`, `for`, `while`, `def`, `class`
- Verifica paréntesis y corchetes balanceados

**Error común:**
```python
# ❌ Mal
if x > 5
    print(x)

# ✅ Bien
if x > 5:
    print(x)
```

---

### IndentationError: unexpected indent

**Causa:** Indentación incorrecta.

**Solución:**
- Usa 4 espacios, no tabs
- No indentes al inicio de líneas sueltas
- Verifica que las líneas dentro de funciones/bloques estén indentadas

---

### NameError: name 'variable' is not defined

**Causa:** Usas una variable que no existe o no se ha definido aún.

**Solución:**
- Verifica que la variable esté escrita exactamente igual
- Asegúrate de que se haya ejecutado la línea donde se define

---

### TypeError: unsupported operand type(s) for +: 'str' and 'int'

**Causa:** Estás sumando texto con número.

**Solución:**
```python
# ❌ Error
nombre = "Juan"
edad = 25
print(nombre + edad)  # Error!

# ✅ Solución
print(nombre + str(edad))  # "Juan25"
print(f"{nombre} tiene {edad} años")  # Mejor: "Juan tiene 25 años"
```

---

### ValueError: invalid literal for int() with base 10: 'abc'

**Causa:** Estás convirtiendo texto que no es número a entero.

**Solución:**
```python
# ✅ Con validación
try:
    numero = int(input("Ingresa un número: "))
    print(numero * 2)
except ValueError:
    print("Debes ingresar un número válido")
```

---

### IndexError: list index out of range

**Causa:** Estás accediendo a una posición que no existe.

**Solución:**
```python
# ❌ Error
lista = [1, 2, 3]
print(lista[5])  # No existe el índice 5

# ✅ Bien
print(lista[2])  # Accede al último elemento (índice 2)
print(lista[-1])  # Accede al último elemento
```

---

### FileNotFoundError: [Errno 2] No such file or directory

**Causa:** El archivo que intentas abrir no existe o la ruta es incorrecta.

**Solución:**
- Verifica la ruta del archivo (usa rutas relativas desde donde ejecutas el script)
- Verifica que el archivo exista: `import os; print(os.path.exists("archivo.txt"))`

---

### json.JSONDecodeError: Expecting value

**Causa:** El archivo JSON está vacío o tiene formato inválido.

**Solución:**
```python
import json

# Cargar con manejo de error
try:
    with open("datos.json") as f:
        datos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    datos = {}  # Valores por defecto si hay error
```

---

## Entornos Virtuales

### Problema: pip no funciona dentro del entorno virtual

**Síntoma:** `pip: command not found`

**Solución:**
```bash
# Windows
venv\Scripts\pip install paquete

# macOS/Linux
source venv/bin/activate
pip install paquete
```

---

### Problema: El entorno virtual no se activa

**Windows:**
```cmd
cd tu_proyecto
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
cd tu_proyecto
python3 -m venv venv
source venv/bin/activate
```

---

## Jupyter y Notebooks

### Problema: Jupyter no se inicia

```bash
pip install jupyter
jupyter notebook
```

### Problema: Kernel no conecta

1. En VS Code, presiona `Ctrl + Shift + P`
2. Busca "Jupyter: Select Kernel"
3. Selecciona un kernel válido
4. Si no hay, reinicia VS Code

---

## Errores de Git

### Problema: "fatal: not a git repository"

**Solución:**
```bash
cd tu_carpeta_del_proyecto
git init
```

---

### Problema: Conflicto de merge

1. No te asustes, es normal
2. Edita los archivos en conflicto manualmente
3. Elimina los marcadores `<<<<<<<`, `=======`, `>>>>>>>`
4. Ejecuta: `git add .` y `git commit -m "Resolver conflictos"`

---

## Depuración (Debugging)

### Técnica 1: Print debugging

Simple pero efectivo:
```python
def calcular(a, b):
    print(f"a = {a}, b = {b}")  # Debug
    resultado = a + b
    print(f"resultado = {resultado}")  # Debug
    return resultado
```

### Técnica 2: Depurador de VS Code

1. Click en el número de línea donde quieres parar
2. Presiona F5
3. Usa los botones de depuración (Step Over, Step Into, etc.)

### Técnica 3: Traceback

Lee el error de abajo hacia arriba. La última línea generalmente dice quéwent mal y en qué línea.

---

## ¿Necesitas Más Ayuda?

1. **Revisa el FAQ** del curso
2. **Busca en Google** el mensaje de error exacto
3. **Pregunta en el grupo de WhatsApp** del curso
4. **Consulta a tu instructor** durante las sesiones