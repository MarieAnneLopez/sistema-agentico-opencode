# DISEÑO — Calculadora de consola en Python 3

Deriva de `docs/REQUISITOS.md`. Léelo junto a este documento.

## Resumen
Calculadora de consola de dos operandos y un operador (`+ - * /`). Dos módulos en `src/`: `calculadora.py` concentra la lógica aritmética pura (testeable sin consola) y `main.py` se encarga de parsear argumentos, validar y presentar resultados o errores. Pruebas con `unittest` en `tests/`.

## Lenguaje y dependencias
- Lenguaje: Python 3.13+ (verificado 3.13.14). Solo biblioteca estándar (`sys`, `unittest`). Cero dependencias externas, cero acceso a red (RNF-01, RNF-02, RNF-03).
- Pruebas: `unittest` con descubrimiento desde la raíz.

## Módulos

### Módulo `src/calculadora.py`
Propósito: lógica aritmética pura. No imprime ni lee de consola (permite probar CA-01..CA-06 sin subprocess).

| Función (firma exacta) | Descripción | Errores |
|---|---|---|
| `def sumar(a: float, b: float) -> float` | Devuelve `a + b`. | Ninguno. |
| `def restar(a: float, b: float) -> float` | Devuelve `a - b`. | Ninguno. |
| `def multiplicar(a: float, b: float) -> float` | Devuelve `a * b`. | Ninguno. |
| `def dividir(a: float, b: float) -> float` | Devuelve `a / b`. | Lanza `ZeroDivisionError` cuando `b == 0` (excepción interna controlada; la lanza la propia función con `raise ZeroDivisionError`, no se apoya en el error implícito de Python). |

Excepción interna: se reutiliza `ZeroDivisionError` de la biblioteca estándar como señal de "división por cero". `calculadora.py` la lanza; `main.py` la captura. Las pruebas de `dividir` usan `assertRaises(ZeroDivisionError)` (CA-05, parte unitaria).

### Módulo `src/main.py`
Propósito: entrada por consola (parseo, validación, presentación). Solo este módulo imprime.

| Función (firma exacta) | Descripción | Errores que maneja |
|---|---|---|
| `def parsear_numero(texto: str) -> float` | Convierte un argumento a `float` (acepta enteros y decimales: `2`, `2.5`, `-3`). | Lanza `ValueError` si no es numérico. |
| `def validar_operador(texto: str) -> str` | Devuelve el operador si es uno de `+ - * /`. | Lanza `ValueError` si es inválido. |
| `def calcular(a: float, operador: str, b: float) -> float` | Selecciona la función de `calculadora` mediante un diccionario `{'+': sumar, '-': restar, '*': multiplicar, '/': dividir}` y la aplica. | Propaga `ZeroDivisionError` de `dividir`. |
| `def formatear_resultado(valor: float) -> str` | Devuelve el número como texto sin decimales inútiles (`10.0` → `"10"`, `3.5` → `"3.5"`). | Ninguno. |
| `def main(argv: list[str]) -> int` | Orquesta todo y devuelve el código de salida. Ver flujo abajo. | Captura todas las condiciones de error; nunca deja escapar un traceback. |

`main(argv)` también se invoca sin argumentos al final del archivo: `if __name__ == "__main__": raise SystemExit(main(sys.argv[1:]))`.

## Formato de mensajes de error (RNF coherente con CA-05 y CA-06)

| Situación | Mensaje exacto (stdout) | Código de salida |
|---|---|---|
| División por cero | `Error: no se puede dividir entre cero` | `1` |
| Operador inválido | `Error: operador inválido: '<op>'. Operadores válidos: + - * /` | `1` |
| Valor no numérico | `Error: '<valor>' no es un número válido` | `1` |
| Número de argumentos distinto de 3 | `Error: uso esperado: python src/main.py <numero> <operador> <numero>` | `1` |

Todos los mensajes empiezan por `Error:` (prefijo estable para las pruebas), se imprimen en stdout y **nunca** producen traceback (RF-05, RF-06). El código `0` se reserva para resultados correctos.

## Flujo de datos (extremo a extremo)
1. PowerShell ejecuta `python src/main.py 7 / 2`; el SO entrega `argv = ["7", "/", "2"]`.
2. `main` verifica que hay exactamente 3 argumentos; si no, imprime el mensaje de uso y devuelve `1`.
3. `main` llama `parsear_numero(argv[0])` y `parsear_numero(argv[2])`; si alguno lanza `ValueError`, imprime `Error: '<valor>' no es un número válido` y devuelve `1`.
4. `main` llama `validar_operador(argv[1])`; si lanza `ValueError`, imprime el mensaje de operador inválido y devuelve `1`.
5. `main` llama `calcular(a, operador, b)`; esta selecciona la función del diccionario y la invoca.
6. Si `calcular` propaga `ZeroDivisionError`, `main` lo captura, imprime `Error: no se puede dividir entre cero` y devuelve `1`.
7. En caso exitoso, `main` llama `formatear_resultado(resultado)`, imprime la cadena por stdout y devuelve `0`.

## Estructura de carpetas
```
AGENTES IA/
├── docs/
│   ├── REQUISITOS.md      ← este proyecto: requisitos y CA
│   └── DISENO.md          ← este documento
├── src/
│   ├── calculadora.py     ← lógica: sumar, restar, multiplicar, dividir
│   └── main.py            ← consola: parseo, validación, impresión
└── tests/
    ├── __init__.py        ← hace el paquete descubrible por unittest
    └── calculadora_test.py ← pruebas de CA-01..CA-06
```
Cada archivo de prueba añade `src/` al path para poder importar:
`sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))`.

Comando único de pruebas desde la raíz (RNF-05):
```
python -m unittest discover -s tests -t .
```

## Decisiones

| Decisión | Alternativa descartada | Motivo |
|---|---|---|
| `dividir` lanza `ZeroDivisionError` y `main` la captura (señal de error por excepción interna controlada). | Devolver una cadena de mensaje de error desde `calculadora`. | El tipo de retorno queda siempre `float` (contrato limpio y testeable con `assertRaises`); mezclar números y texto en el mismo retorno obliga a quien llama a adivinar el tipo y rompe CA-01..CA-04. |
| Validación y presentación en `main.py`; aritmética en `calculadora.py`. | Un único archivo con todo. | Permite probar la lógica sin subprocess y la consola sin repetir aritmética; separación mínima, sin sobre-ingeniería. |
| Diccionario `{operador: función}` en `calcular`. | Cadena de `if/elif`. | Extensible (añadir un operador = una entrada) y hace trivial probar que cada operador llama a su función. |
| Salida formateada sin `.0` innecesario (`10`, no `10.0`). | Imprimir el `float` crudo (`repr`). | CA-03 pide `10`; al compararse numéricamente ambas formas valen, pero la salida limpia es más usable en consola. |
| Mensajes de error en stdout con código de salida `1`, sin traceback. | Imprimir errores en stderr o dejar que la excepción suba. | CA-05/CA-06 exigen "no lanza excepción": capturar y devolver `1` cumple literalmente el criterio y sigue siendo detectable por PowerShell. |
| Solo biblioteca estándar. | `argparse`, `click` o similar. | RNF-01: sin dependencias; el formato de argumentos es fijo y simple, `sys.argv` basta. |

## Trazabilidad RF a módulo

| RF | Módulo / función | Prueba (CA) |
|---|---|---|
| RF-01 | `calculadora.sumar`, `main.calcular` | CA-01 |
| RF-02 | `calculadora.restar`, `main.calcular` | CA-02 |
| RF-03 | `calculadora.multiplicar`, `main.calcular` | CA-03 |
| RF-04 | `calculadora.dividir`, `main.calcular` | CA-04 |
| RF-05 | `calculadora.dividir` (lanza), `main.main` (captura e imprime) | CA-05 |
| RF-06 | `main.parsear_numero`, `main.validar_operador`, `main.main` | CA-06 |
| RF-07 | `main.parsear_numero` (acepta `float`), `calculadora.*` | CA-03 (decimales) |
| RNF-01/02/03 | Todo el proyecto (sin imports externos, sin red) | Revisión de imports en pruebas |
| RNF-04/05 | `main.main`, estructura `tests/` | Ejecución de los comandos documentados |
| RNF-06 | `tests/` comparan con `assertEqual`/`assertAlmostEqual` numéricos | Todas |
