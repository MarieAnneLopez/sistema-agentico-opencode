# REQUISITOS — Calculadora de consola en Python 3

## Objetivo
Un usuario de PowerShell (Windows) podrá ejecutar una operación aritmética básica desde la línea de comandos con `python src/main.py <número> <operador> <número>` y ver el resultado impreso en consola.

## Alcance
- Cuatro operaciones: suma, resta, multiplicación y división.
- Entrada por argumentos de línea de comandos (formato: número, operador, número).
- Salida por consola: el resultado numérico o un mensaje de error claro.
- Pruebas automatizadas con `unittest` (biblioteca estándar).

## Fuera de alcance
- Interactivo / menú con bucle de preguntas.
- Operadores unarios, potencias, raíces, porcentajes u otras operaciones.
- Expresiones compuestas (p. ej. `2 + 3 * 4`), paréntesis o precedencia.
- Interfaz gráfica, historial, memoria o persistencia.
- Instalación de paquetes externos (pip) o cualquier uso de red.

## Requisitos funcionales

| ID | Requisito |
|----|-----------|
| RF-01 | Sumar dos números introducidos por consola y mostrar el resultado. |
| RF-02 | Restar dos números introducidos por consola y mostrar el resultado. |
| RF-03 | Multiplicar dos números introducidos por consola y mostrar el resultado. |
| RF-04 | Dividir dos números introducidos por consola y mostrar el resultado. |
| RF-05 | Al dividir entre cero, mostrar el mensaje "Error: no se puede dividir entre cero" y terminar sin lanzar excepción (sin traceback). |
| RF-06 | Ante un operador inválido o un valor que no sea número, mostrar un mensaje de error claro y terminar sin lanzar excepción. |
| RF-07 | Aceptar tanto enteros como decimales como operandos (p. ej. `4` y `2.5`). |

## Requisitos no funcionales

| ID | Requisito |
|----|-----------|
| RNF-01 | Sin dependencias externas: solo biblioteca estándar de Python. |
| RNF-02 | Sin acceso a red en ninguna parte del programa. |
| RNF-03 | Lenguaje: Python 3.13+ (verificado: 3.13.14). |
| RNF-04 | Ejecutable en PowerShell de Windows con un único comando `python src/main.py ...`. |
| RNF-05 | Las pruebas se ejecutan con un solo comando desde la raíz del proyecto (`python -m unittest ...`). |
| RNF-06 | Los resultados se comparan como números (numéricamente), no como texto, en los criterios de aceptación y las pruebas. |

## Criterios de aceptación

| ID | Criterio | Verificación |
|----|----------|--------------|
| CA-01 | Dado `python src/main.py 2 + 3`, cuando se ejecuta, entonces imprime `5` (numéricamente igual a 5). | Ejecución del comando + prueba unitaria de `sumar`. |
| CA-02 | Dado `python src/main.py 7 - 10`, cuando se ejecuta, entonces imprime `-3`. | Ejecución del comando + prueba unitaria de `restar`. |
| CA-03 | Dado `python src/main.py 4 * 2.5`, cuando se ejecuta, entonces imprime `10`. | Ejecución del comando + prueba unitaria de `multiplicar`. |
| CA-04 | Dado `python src/main.py 9 / 3`, cuando se ejecuta, entonces imprime `3`. | Ejecución del comando + prueba unitaria de `dividir`. |
| CA-05 | Dado `python src/main.py 5 / 0`, cuando se ejecuta, entonces imprime `Error: no se puede dividir entre cero` y no lanza excepción (no aparece traceback). | Ejecución del comando (código de salida normal, sin traceback) + prueba unitaria de `dividir`. |
| CA-06 | Dado `python src/main.py 2 ^ 3` o `python src/main.py a + 1`, cuando se ejecuta, entonces imprime un mensaje de error claro y no lanza excepción (no aparece traceback). | Ejecución del comando + pruebas unitarias de validación. |

## Supuestos
- S-01: El formato de invocación es exactamente `python src/main.py <número> <operador> <número>`; operadores válidos: `+`, `-`, `*`, `/`.
- S-02: Los resultados se comparan como números, no como texto (un resultado `10.0` satisface CA-03).
- S-03: La lógica de las operaciones vive en `src/calculadora.py` (una función por operación) y la entrada por consola en `src/main.py`.
- S-04: Python 3.13.14 ya está verificado en el entorno de destino; no se requiere compatibilidad con versiones anteriores.
- S-05: Los mensajes de error se muestran en español, coherentes con los CA.
- S-06: Con datos correctos el programa termina con código de salida 0; con datos inválidos el programa termina de forma controlada (sin traceback) tras imprimir el mensaje de error.
