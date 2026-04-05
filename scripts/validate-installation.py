#!/usr/bin/env python3
"""
Script de validación inicial para verificar instalación de Python y Quarto
Este script verifica que el entorno de desarrollo esté correctamente configurado
para el curso de Programación Python Fundamentos.
"""

import sys
import subprocess
import platform
from pathlib import Path


def check_python_version():
    """Verifica que la versión de Python sea compatible."""
    print("🔍 Verificando versión de Python...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(
            f"❌ Error: Se requiere Python 3.8 o superior. Versión actual: {version.major}.{version.minor}"
        )
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True


def check_quarto_installation():
    """Verifica que Quarto esté instalado y accesible."""
    print("\n🔍 Verificando instalación de Quarto...")
    try:
        result = subprocess.run(
            ["quarto", "--version"], capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Quarto {version} - Instalado correctamente")
            return True
        else:
            print(f"❌ Error al ejecutar Quarto: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ Error: Quarto no encontrado en el PATH")
        return False
    except subprocess.TimeoutExpired:
        print("❌ Error: Timeout al ejecutar Quarto")
        return False


def check_quarto_python_kernel():
    """Verifica que Quarto tenga el kernel de Python disponible."""
    print("\n🔍 Verificando kernel de Python para Quarto...")
    try:
        result = subprocess.run(
            ["quarto", "check"], capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            if "Python 3 installation....OK" in result.stdout:
                print("✅ Kernel de Python para Quarto - Disponible")
                return True
            else:
                print(
                    "⚠️  Advertencia: Kernel de Python podría no estar completamente configurado"
                )
                print("   Salida de quarto check:")
                print(result.stdout)
                return True  # Aún así continuamos
        else:
            print(f"❌ Error al ejecutar quarto check: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("❌ Error: Timeout al ejecutar quarto check")
        return False


def check_virtual_environment():
    """Verifica si estamos en un entorno virtual."""
    print("\n🔍 Verificando entorno virtual...")
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        print("✅ Entorno virtual detectado")
        print(f"   Ruta: {sys.prefix}")
        return True
    else:
        print("⚠️  Advertencia: No se detecta entorno virtual activo")
        print(
            "   Se recomienda usar un entorno virtual para evitar conflictos de dependencias"
        )
        return True  # No es crítico, solo una advertencia


def check_required_packages():
    """Verifica que los paquetes requeridos estén instalados."""
    print("\n🔍 Verificando paquetes requeridos...")
    required_packages = {
        "pytest": "pytest",
        "requests": "requests",
        "beautifulsoup4": "bs4",
        "flask": "flask",
    }
    missing_packages = []

    for display_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✅ {display_name} - Instalado")
        except ImportError:
            print(f"❌ {display_name} - No instalado")
            missing_packages.append(display_name)

    if missing_packages:
        print(f"\n💡 Para instalar los paquetes faltantes, ejecuta:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    return True


def check_project_structure():
    """Verifica la estructura básica del proyecto."""
    print("\n🔍 Verificando estructura del proyecto...")
    required_dirs = [
        "content",
        "instructor",
        "shared",
        "output",
        "scripts",
        "tests",
        "config",
        "docs",
    ]
    missing_dirs = []

    for directory in required_dirs:
        if Path(directory).is_dir():
            print(f"✅ {directory}/ - Directorio encontrado")
        else:
            print(f"❌ {directory}/ - Directorio faltante")
            missing_dirs.append(directory)

    if missing_dirs:
        print(f"\n💡 Para crear los directorios faltantes, ejecuta:")
        print(f"   mkdir -p {' '.join(missing_dirs)}")
        return False
    return True


def main():
    """Función principal de validación."""
    print("=" * 60)
    print("🚀 VALIDACIÓN DE INSTALACIÓN - CURSO PYTHON FUNDAMENTOS")
    print("=" * 60)
    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Arquitectura: {platform.machine()}")
    print()

    checks = [
        check_python_version,
        check_quarto_installation,
        check_quarto_python_kernel,
        check_virtual_environment,
        check_required_packages,
        check_project_structure,
    ]

    passed = 0
    total = len(checks)

    for check in checks:
        if check():
            passed += 1

    print("\n" + "=" * 60)
    print(f"📊 RESULTADO: {passed}/{total} verificaciones exitosas")

    if passed == total:
        print(
            "🎉 ¡Todas las verificaciones pasaron! El entorno está listo para el curso."
        )
        return 0
    else:
        print(
            "⚠️  Algunas verificaciones fallaron. Por favor, revisa los mensajes arriba."
        )
        print("   Después de corregir los problemas, ejecuta este script nuevamente.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
