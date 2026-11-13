# PLAN DE PRUEBAS — Calculadora de consola

Deriva de `docs/REQUISITOS.md` (CA-01..CA-06) y `docs/DISENO.md` (firmas).

Comando único de pruebas desde la raíz del proyecto:

```
python -m unittest discover -s tests -t .
```

## Tabla de casos

| CA | Caso de prueba | Tipo | Nivel |
|----|----------------|------|-------|
| CA-01 | `sumar(2, 3) == 5.0` | Normal | Unitario |
| CA-01 | `python src/main.py 2 + 3` → stdout numéricamente 5, exit 0 | Normal | Extremo a extremo (subprocess) |
| CA-02 | `restar(7, 10) == -3.0` | Normal | Unitario |
| CA-02 | `python src/main.py 7 - 10` → stdout numéricamente -3, exit 0 | Normal | E2E |
| CA-03 | `multiplicar(4, 2.5) == 10.0` (decimales, RF-07) | Normal | Unitario |
| CA-03 | `python src/main.py 4 * 2.5` → stdout numéricamente 10, exit 0 | Normal | E2E |
| CA-04 | `dividir(9, 3) == 3.0` | Normal | Unitario |
| CA-04 | `python src/main.py 9 / 3` → stdout numéricamente 3, exit 0 | Normal | E2E |
| CA-05 | `dividir(5, 0)` lanza `ZeroDivisionError` | Error | Unitario |
| CA-05 | `python src/main.py 5 / 0` → stdout contiene el mensaje exacto, exit 1, stderr sin "Traceback" | Error | E2E |
| CA-06 | `validar_operador("^")` lanza `ValueError` | Error | Unitario |
| CA-06 | `parsear_numero("a")` lanza `ValueError` | Error | Unitario |
| CA-06 | `python src/main.py 2 ^ 3` → stdout con mensaje de operador inválido, stderr sin "Traceback" | Error | E2E |
| CA-06 | `python src/main.py a + 1` → stdout con mensaje de número inválido, stderr sin "Traceback" | Error | E2E |
| RNF-06 | Todas las comparaciones numéricas usan `assertAlmostEqual`/`float(stdout)` | — | Transversal |

Notas:
- Las comparaciones de resultados se hacen numéricamente (`assertAlmostEqual`, `float(stdout)`), no como texto (RNF-06, S-02).
- Las pruebas E2E usan `subprocess` con el mismo intérprete de Python (`sys.executable`), sin red ni dependencias externas.
- Cero tolerancia en unitarios (`places=7`): las operaciones exactas no deben degradarse.
