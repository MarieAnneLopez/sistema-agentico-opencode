---
name: pruebas-y-verificacion
description: Diseña, escribe y ejecuta pruebas automatizadas a partir de los criterios de aceptación y reporta resultados pasa/falla con evidencia. Usar después de implementar código en src/.
---
# Pruebas y verificación

## Cuándo usar
Hay código en src/ y existen criterios de aceptación en docs/REQUISITOS.md.

## Procedimiento
1. Lee los CA de docs/REQUISITOS.md y las firmas de docs/DISENO.md.
2. Crea tests/PLAN_DE_PRUEBAS.md con una tabla: CA, caso de prueba, tipo (normal, límite, error).
3. Escribe pruebas en tests/ con el framework estándar del lenguaje (unittest en Python salvo que el diseño indique otro). Mínimo por función pública: un caso normal, uno límite y uno de error.
4. Ejecuta las pruebas con un solo comando y captura la salida completa.
5. Si una prueba falla, clasifica la causa: defecto del código, prueba mal escrita o requisito ambiguo. Corrige la prueba solo si está mal escrita; en cualquier otro caso reporta el fallo sin tocar src/.
6. Reporta con evidencia: comando ejecutado, totales (pasaron y fallaron) y el mensaje de error exacto de cada fallo.

## Formato de salida
tests/PLAN_DE_PRUEBAS.md, pruebas ejecutables en tests/ y reporte pasa/falla.

## Checklist de calidad
- Todo CA tiene al menos una prueba.
- Las pruebas son deterministas (sin red, sin azar, sin hora actual).
- El reporte incluye la salida real del comando, no un resumen de memoria.

## Errores comunes
Declarar "todo pasa" sin ejecutar; pruebas sin asserts; modificar src/ desde el rol de probador.
