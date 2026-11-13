"""Lógica aritmética pura de la calculadora. No imprime ni lee de consola."""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de a y b."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de a por b."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Devuelve la división de a entre b; lanza ZeroDivisionError si b es cero."""
    if b == 0:
        raise ZeroDivisionError
    return a / b
