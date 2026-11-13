"""Entrada por consola de la calculadora: parseo, validación y presentación."""

import math
import sys

import calculadora


def _configurar_stdout() -> None:
    """Emite UTF-8 en stdout: sin efecto en consola interactiva y estable al capturar."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def parsear_numero(texto: str) -> float:
    """Convierte un argumento a float; lanza ValueError si no es numérico o finito."""
    numero = float(texto)
    if not math.isfinite(numero):
        raise ValueError(f"valor no finito: {texto!r}")
    return numero


def validar_operador(texto: str) -> str:
    """Devuelve el operador si es uno de + - * /; lanza ValueError si no."""
    if texto not in ("+", "-", "*", "/"):
        raise ValueError(f"operador inválido: {texto!r}")
    return texto


def calcular(a: float, operador: str, b: float) -> float:
    """Aplica la operación correspondiente y propaga ZeroDivisionError."""
    operaciones = {
        "+": calculadora.sumar,
        "-": calculadora.restar,
        "*": calculadora.multiplicar,
        "/": calculadora.dividir,
    }
    return operaciones[operador](a, b)


def formatear_resultado(valor: float) -> str:
    """Devuelve el número como texto sin decimales inútiles (10.0 -> '10')."""
    if math.isfinite(valor) and valor == int(valor):
        return str(int(valor))
    return str(valor)


def _no_es_numero(texto: str) -> bool:
    """Informa si un texto no puede convertirse a float."""
    try:
        parsear_numero(texto)
    except ValueError:
        return True
    return False


def _parsear_operandos(argv: list[str]) -> tuple[float, float]:
    """Convierte argv[0] y argv[2] a float; lanza ValueError si alguno falla."""
    return parsear_numero(argv[0]), parsear_numero(argv[2])


def _error_numero(argv: list[str]) -> None:
    """Imprime el mensaje de número inválido indicando el argumento fallido."""
    for texto in (argv[0], argv[2]):
        if _no_es_numero(texto):
            print(f"Error: '{texto}' no es un número válido")
            return


def main(argv: list[str]) -> int:
    """Orquesta parseo, validación y presentación; devuelve el código de salida."""
    _configurar_stdout()
    if len(argv) != 3:
        print("Error: uso esperado: python src/main.py <numero> <operador> <numero>")
        return 1
    try:
        a, b = _parsear_operandos(argv)
    except ValueError:
        _error_numero(argv)
        return 1
    try:
        operador = validar_operador(argv[1])
    except ValueError:
        print(
            "Error: operador inválido: "
            f"'{argv[1]}'. Operadores válidos: + - * /"
        )
        return 1
    try:
        resultado = calcular(a, operador, b)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
        return 1
    print(formatear_resultado(resultado))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
