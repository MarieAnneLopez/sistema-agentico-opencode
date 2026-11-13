"""Pruebas de la calculadora: cubren CA-01..CA-06 de docs/REQUISITOS.md.

Nivel unitario: funciones de src/calculadora.py y src/main.py.
Nivel extremo a extremo: subprocess con `python src/main.py ...`.

Comparaciones numéricas (RNF-06): assertAlmostEqual y float(stdout).
Solo biblioteca estándar (RNF-01): unittest + subprocess + sys + os.
"""

import os
import subprocess
import sys
import unittest

RUTA_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RUTA_SRC = os.path.join(RUTA_RAIZ, "src")
sys.path.insert(0, RUTA_SRC)

import calculadora  # noqa: E402
import main  # noqa: E402

MENSAJE_DIV_CERO = "Error: no se puede dividir entre cero"
MENSAJE_OP_INVALIDO = "Error: operador inválido: '^'. Operadores válidos: + - * /"
MENSAJE_NO_NUMERO = "Error: 'a' no es un número válido"
MENSAJE_NO_NUMERO_INF = "Error: 'inf' no es un número válido"
MENSAJE_NO_NUMERO_NAN = "Error: 'nan' no es un número válido"


def _ejecutar_main(*args: str) -> subprocess.CompletedProcess:
    """Ejecuta `python src/main.py <args>` y devuelve el proceso terminado."""
    return subprocess.run(
        [sys.executable, os.path.join("src", "main.py"), *args],
        cwd=RUTA_RAIZ,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


class PruebasCalculadora(unittest.TestCase):
    """CA-01..CA-05, parte unitaria: funciones puras de calculadora.py."""

    def test_ca01_sumar_2_mas_3_da_5(self):
        self.assertAlmostEqual(calculadora.sumar(2, 3), 5.0, places=7)

    def test_ca02_restar_7_menos_10_da_menos_3(self):
        self.assertAlmostEqual(calculadora.restar(7, 10), -3.0, places=7)

    def test_ca03_multiplicar_4_por_2_5_da_10(self):
        self.assertAlmostEqual(calculadora.multiplicar(4, 2.5), 10.0, places=7)

    def test_ca04_dividir_9_entre_3_da_3(self):
        self.assertAlmostEqual(calculadora.dividir(9, 3), 3.0, places=7)

    def test_ca05_dividir_5_entre_0_lanza_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(5, 0)

    def test_ca05_dividir_0_entre_0_tambien_lanza(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(0, 0)


class PruebasMainUnitarias(unittest.TestCase):
    """CA-06, parte unitaria: validación en main.py (sin consola)."""

    def test_ca06_validar_operador_invalido_lanza_value_error(self):
        with self.assertRaises(ValueError):
            main.validar_operador("^")

    def test_ca06_parsear_numero_no_numerico_lanza_value_error(self):
        with self.assertRaises(ValueError):
            main.parsear_numero("a")

    def test_parsear_numero_acepta_enteros_y_decimales(self):
        self.assertAlmostEqual(main.parsear_numero("2"), 2.0, places=7)
        self.assertAlmostEqual(main.parsear_numero("2.5"), 2.5, places=7)
        self.assertAlmostEqual(main.parsear_numero("-3"), -3.0, places=7)

    def test_validar_operador_acepta_los_cuatro(self):
        self.assertEqual(main.validar_operador("+"), "+")
        self.assertEqual(main.validar_operador("-"), "-")
        self.assertEqual(main.validar_operador("*"), "*")
        self.assertEqual(main.validar_operador("/"), "/")

    def test_calcular_selecciona_cada_operacion(self):
        self.assertAlmostEqual(main.calcular(2, "+", 3), 5.0, places=7)
        self.assertAlmostEqual(main.calcular(7, "-", 10), -3.0, places=7)
        self.assertAlmostEqual(main.calcular(4, "*", 2.5), 10.0, places=7)
        self.assertAlmostEqual(main.calcular(9, "/", 3), 3.0, places=7)

    def test_calcular_propaga_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            main.calcular(5, "/", 0)

    def test_formatear_resultado_sin_decimales_inutiles(self):
        self.assertEqual(main.formatear_resultado(10.0), "10")
        self.assertEqual(main.formatear_resultado(3.5), "3.5")

    def test_main_sin_excepcion_con_division_por_cero(self):
        # main captura el error: devuelve código 1 y no lanza nada al usuario.
        self.assertEqual(main.main(["5", "/", "0"]), 1)

    def test_main_sin_excepcion_con_operador_invalido(self):
        self.assertEqual(main.main(["2", "^", "3"]), 1)

    def test_main_sin_excepcion_con_numero_invalido(self):
        self.assertEqual(main.main(["a", "+", "1"]), 1)


class PruebasCorreccionInfNan(unittest.TestCase):
    """Corrección del desarrollador: parsear_numero rechaza inf/nan (math.isfinite).

    Refuerza CA-06: valores no finitos se tratan como números inválidos y
    main jamás deja escapar un traceback al usuario.
    """

    def test_parsear_numero_rechaza_inf(self):
        with self.assertRaises(ValueError):
            main.parsear_numero("inf")

    def test_parsear_numero_rechaza_nan(self):
        with self.assertRaises(ValueError):
            main.parsear_numero("nan")

    def test_parsear_numero_rechaza_variantes_de_inf_y_nan(self):
        for texto in ("-inf", "Infinity", "-Infinity", "NaN", "+inf"):
            with self.assertRaises(ValueError):
                main.parsear_numero(texto)

    def test_formatear_resultado_blindado_con_valores_no_finitos(self):
        # No debe lanzar excepción aunque reciba un valor no finito.
        self.assertEqual(main.formatear_resultado(float("inf")), "inf")
        self.assertEqual(main.formatear_resultado(float("-inf")), "-inf")
        self.assertEqual(main.formatear_resultado(float("nan")), "nan")

    def test_main_sin_excepcion_con_inf_como_operando(self):
        self.assertEqual(main.main(["inf", "+", "1"]), 1)

    def test_main_sin_excepcion_con_nan_como_operando(self):
        self.assertEqual(main.main(["nan", "/", "2"]), 1)

    def test_e2e_inf_suma_mensaje_y_sin_traceback(self):
        p = _ejecutar_main("inf", "+", "1")
        self.assertNotIn("Traceback", p.stderr)
        self.assertIn(MENSAJE_NO_NUMERO_INF, p.stdout)
        self.assertEqual(p.returncode, 1)

    def test_e2e_nan_division_mensaje_y_sin_traceback(self):
        p = _ejecutar_main("nan", "/", "2")
        self.assertNotIn("Traceback", p.stderr)
        self.assertIn(MENSAJE_NO_NUMERO_NAN, p.stdout)
        self.assertEqual(p.returncode, 1)


class PruebasExtremoAExtremo(unittest.TestCase):
    """CA-01..CA-06 vía subprocess: stdout numérico, stderr sin traceback."""

    def test_ca01_suma(self):
        p = _ejecutar_main("2", "+", "3")
        self.assertEqual(p.returncode, 0)
        self.assertNotIn("Traceback", p.stderr)
        self.assertAlmostEqual(float(p.stdout.strip()), 5.0, places=7)

    def test_ca02_resta(self):
        p = _ejecutar_main("7", "-", "10")
        self.assertEqual(p.returncode, 0)
        self.assertNotIn("Traceback", p.stderr)
        self.assertAlmostEqual(float(p.stdout.strip()), -3.0, places=7)

    def test_ca03_multiplicacion_con_decimal(self):
        p = _ejecutar_main("4", "*", "2.5")
        self.assertEqual(p.returncode, 0)
        self.assertNotIn("Traceback", p.stderr)
        self.assertAlmostEqual(float(p.stdout.strip()), 10.0, places=7)

    def test_ca04_division(self):
        p = _ejecutar_main("9", "/", "3")
        self.assertEqual(p.returncode, 0)
        self.assertNotIn("Traceback", p.stderr)
        self.assertAlmostEqual(float(p.stdout.strip()), 3.0, places=7)

    def test_ca05_division_por_cero_mensaje_y_sin_traceback(self):
        p = _ejecutar_main("5", "/", "0")
        self.assertNotIn("Traceback", p.stderr)
        self.assertIn(MENSAJE_DIV_CERO, p.stdout)
        self.assertEqual(p.returncode, 1)

    def test_ca06_operador_invalido_mensaje_y_sin_traceback(self):
        p = _ejecutar_main("2", "^", "3")
        self.assertNotIn("Traceback", p.stderr)
        self.assertIn(MENSAJE_OP_INVALIDO, p.stdout)
        self.assertEqual(p.returncode, 1)

    def test_ca06_valor_no_numerico_mensaje_y_sin_traceback(self):
        p = _ejecutar_main("a", "+", "1")
        self.assertNotIn("Traceback", p.stderr)
        self.assertIn(MENSAJE_NO_NUMERO, p.stdout)
        self.assertEqual(p.returncode, 1)


if __name__ == "__main__":
    unittest.main()
