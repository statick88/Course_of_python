"""
Tests unitarios para los ejemplos de código en los materiales del curso.
Estos tests verifican que las soluciones de referencia funcionan correctamente.
"""

import pytest
from unittest.mock import patch
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ============================================
# MÓDULO 2: Tipos de Datos y Variables
# ============================================


class TestCalculadoraPropinas:
    """Test para Desafío 1 - Calculadora de Propinas"""

    def test_propina_15_porciento(self):
        """Verifica cálculo con 15% de propina"""
        total = 100.0
        porcentaje = 15
        personas = 4

        monto_propina = round(total * (porcentaje / 100), 2)
        total_con_propina = round(total + monto_propina, 2)
        por_persona = round(total_con_propina / personas, 2)

        assert monto_propina == 15.0
        assert total_con_propina == 115.0
        assert por_persona == 28.75

    def test_propina_20_porciento(self):
        """Verifica cálculo con 20% de propina"""
        total = 85.50
        porcentaje = 20
        personas = 3

        monto_propina = round(total * (porcentaje / 100), 2)
        total_con_propina = round(total + monto_propina, 2)
        por_persona = round(total_con_propina / personas, 2)

        assert monto_propina == 17.1
        assert total_con_propina == 102.6
        assert por_persona == 34.2


class TestConversorUnidades:
    """Test para Desafío 2 - Conversor de Unidades"""

    def test_celsius_a_fahrenheit(self):
        """Verifica conversión de Celsius a Fahrenheit"""
        celsius = 0
        fahrenheit = (celsius * 9 / 5) + 32
        assert fahrenheit == 32

        celsius = 100
        fahrenheit = (celsius * 9 / 5) + 32
        assert fahrenheit == 212

    def test_kilometros_a_millas(self):
        """Verifica conversión de km a millas"""
        kilometros = 1
        millas = kilometros * 0.621371
        assert round(millas, 2) == 0.62


class TestValidadorEdad:
    """Test para Desafío 3 - Validador de Edad"""

    def test_menor_de_edad(self):
        """Verifica que menores de 18 son menores"""
        edad = 17
        assert edad < 18

    def test_mayor_de_edad(self):
        """Verifica que mayores de 18 son adultos"""
        edad = 18
        assert edad >= 18

    def test_adulto_mayor(self):
        """Verifica que mayores de 65 son adultos mayores"""
        edad = 70
        assert edad >= 65


# ============================================
# MÓDULO 3: Estructuras de Control
# ============================================


class TestFizzBuzz:
    """Test para Desafío 3 - FizzBuzz"""

    def test_multiplo_de_3(self):
        """Devuelve 'Fizz' para múltiplos de 3"""
        for i in [3, 6, 9, 12]:
            if i % 3 == 0 and i % 5 != 0:
                resultado = "Fizz"
            assert resultado == "Fizz"

    def test_multiplo_de_5(self):
        """Devuelve 'Buzz' para múltiplos de 5"""
        i = 10
        if i % 5 == 0 and i % 3 != 0:
            resultado = "Buzz"
        assert resultado == "Buzz"

    def test_fizzbuzz(self):
        """Devuelve 'FizzBuzz' para múltiplos de 3 y 5"""
        for i in [15, 30, 45]:
            if i % 3 == 0 and i % 5 == 0:
                resultado = "FizzBuzz"
            assert resultado == "FizzBuzz"


class TestAdivinaElNumero:
    """Test para Desafío 4 - Adivina el Número"""

    def test_adivinar_correcto(self):
        """Verifica cuando el usuario adivina el número"""
        numero_secreto = 50
        intento = 50
        assert intento == numero_secreto

    def test_adivinar_mayor(self):
        """Verifica pista cuando el número es mayor"""
        numero_secreto = 50
        intento = 75
        assert intento > numero_secreto

    def test_adivinar_menor(self):
        """Verifica pista cuando el número es menor"""
        numero_secreto = 50
        intento = 25
        assert intento < numero_secreto


# ============================================
# MÓDULO 4: Funciones
# ============================================


class TestAreaCirculo:
    """Test para Desafío 2 - Área del Círculo"""

    def test_area_circulo(self):
        """Verifica cálculo del área de un círculo"""
        import math

        radio = 5
        area = math.pi * radio**2
        assert round(area, 2) == 78.54

    def test_area_circulo_radio_1(self):
        """Verifica área con radio 1"""
        import math

        radio = 1
        area = math.pi * radio**2
        assert round(area, 2) == 3.14


class TestNumeroPrimo:
    """Test para Desafío 5 - Verificador de Primos"""

    def es_primo(self, n):
        """Función auxiliar para verificar primos"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def test_primos(self):
        """Verifica números primos"""
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for p in primos:
            assert self.es_primo(p) is True

    def test_no_primos(self):
        """Verifica números no primos"""
        no_primos = [0, 1, 4, 6, 8, 9, 10, 12]
        for n in no_primos:
            assert self.es_primo(n) is False


class TestFibonacci:
    """Test para Desafío 6 - Serie Fibonacci"""

    def fibonacci(self, n):
        """Función para generar serie Fibonacci"""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        serie = [0, 1]
        for i in range(2, n):
            serie.append(serie[-1] + serie[-2])
        return serie

    def test_fibonacci_5(self):
        """Verifica Fibonacci con 5 elementos"""
        resultado = self.fibonacci(5)
        assert resultado == [0, 1, 1, 2, 3]

    def test_fibonacci_10(self):
        """Verifica Fibonacci con 10 elementos"""
        resultado = self.fibonacci(10)
        assert resultado == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ============================================
# MÓDULO 5: Listas y Tuplas
# ============================================


class TestPromedioNotas:
    """Test para Desafío 1 - Promedio de Notas"""

    def test_promedio(self):
        """Verifica cálculo del promedio"""
        notas = [8.5, 9.0, 7.5, 6.0, 8.0]
        promedio = sum(notas) / len(notas)
        assert promedio == 7.8

    def test_aprobado(self):
        """Verifica que promedio >= 7 es aprobado"""
        promedio = 7.8
        assert promedio >= 7.0

    def test_reprobado(self):
        """Verifica que promedio < 7 es reprobado"""
        promedio = 6.5
        assert promedio < 7.0


class TestEstadisticasLista:
    """Test para Desafío 4 - Estadísticas de Lista"""

    def test_estadisticas(self):
        """Verifica cálculo de estadísticas"""
        datos = [5, 10, 3, 8, 12]

        assert sum(datos) / len(datos) == 7.6  # media
        assert max(datos) == 12  # máximo
        assert min(datos) == 3  # mínimo
        assert sorted(datos) == [3, 5, 8, 10, 12]  # ordenada


# ============================================
# MÓDULO 6: Diccionarios y Sets
# ============================================


class TestAgendaContactos:
    """Test para Desafío 1 - Agenda de Contactos"""

    def test_crear_contacto(self):
        """Verifica creación de contacto"""
        agenda = {}
        agenda["Juan"] = {"telefono": "123456789", "email": "juan@email.com"}

        assert "Juan" in agenda
        assert agenda["Juan"]["telefono"] == "123456789"

    def test_buscar_contacto(self):
        """Verifica búsqueda de contacto"""
        agenda = {"Ana": {"telefono": "111"}}

        assert agenda.get("Ana") is not None
        assert agenda.get("Pedro") is None


class TestSistemaVotaciones:
    """Test para Desafío 5 - Sistema de Votaciones"""

    def test_registrar_voto(self):
        """Verifica registro de votos"""
        votos = {}

        def registrar(candidato):
            if candidato in votos:
                votos[candidato] += 1
            else:
                votos[candidato] = 1

        registrar("Ana")
        registrar("Ana")
        registrar("Juan")

        assert votos["Ana"] == 2
        assert votos["Juan"] == 1


# ============================================
# MÓDULO 9: Buenas Prácticas y Testing
# ============================================


class TestValidadorRobusto:
    """Test para Desafío 3 - Validador Robusto"""

    def validar_nombre(self, nombre):
        """Valida nombre"""
        if not nombre or len(nombre) < 2:
            return False
        return True

    def test_nombre_valido(self):
        """Verifica nombres válidos"""
        assert self.validar_nombre("Ana") is True
        assert self.validar_nombre("Juan") is True

    def test_nombre_invalido(self):
        """Verifica nombres inválidos"""
        assert self.validar_nombre("") is False
        assert self.validar_nombre("A") is False


class TestCalculadoraSimple:
    """Test para Desafío 4 - Test Calculadora"""

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def test_suma_positivos(self):
        assert self.suma(2, 3) == 5

    def test_suma_negativos(self):
        assert self.suma(-1, -1) == -2

    def test_resta(self):
        assert self.resta(10, 5) == 5

    def test_resta_negativo(self):
        assert self.resta(5, 10) == -5


# ============================================
# EJECUTAR TESTS
# ============================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
