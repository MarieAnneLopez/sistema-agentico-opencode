---
name: escritura-de-codigo
description: Implementa en src/ el código fuente fiel a docs/DISENO.md, con funciones pequeñas, manejo de errores y documentación mínima. Usar cuando el diseño está listo y hay que programar, o cuando las pruebas reportan un fallo que corregir.
---
# Escritura de código

## Cuándo usar
Existe docs/DISENO.md y hay que implementar, o el probador reportó un fallo.

## Procedimiento
1. Lee docs/DISENO.md y docs/REQUISITOS.md. Implementa SOLO lo que el diseño define.
2. Crea un archivo por módulo, con los nombres y firmas exactos del diseño. Si una firma es inviable, no la cambies en silencio: repórtalo en el handoff.
3. Funciones de máximo 30 líneas, nombres descriptivos, sin código duplicado.
4. Valida entradas y maneja errores con mensajes claros. Nunca uses un `except` vacío ni silencies fallos.
5. Un docstring de una o dos líneas por función pública. Comentarios solo para explicar el porqué.
6. Si hay punto de entrada, créalo como src/main.py (o el equivalente del lenguaje elegido).
7. Antes de reportar, verifica que el código carga sin errores (por ejemplo `python -m py_compile` sobre cada archivo).
8. Ante un fallo reportado por el probador: reproduce, corrige la causa raíz con el cambio mínimo y vuelve a verificar.

## Formato de salida
Archivos en src/ y reporte con lista de archivos creados o modificados y resultado de la verificación.

## Checklist de calidad
- Cada módulo del diseño existe y coincide en firmas.
- No hay secretos, rutas absolutas ni dependencias que el diseño no declare.
- El código compila o carga sin errores.

## Errores comunes
Añadir funcionalidades no pedidas; corregir síntomas en vez de la causa; modificar las pruebas para que pasen.
