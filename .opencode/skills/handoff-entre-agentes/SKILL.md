---
name: handoff-entre-agentes
description: Define el formato estándar de las órdenes que el orquestador da a los subagentes y de los reportes que ellos devuelven, con evidencia y estado explícito. Usar siempre al delegar una tarea o al reportar resultados.
---
# Handoff entre agentes

## Cuándo usar
Cada vez que el orquestador delega una tarea o un subagente devuelve su resultado.

## Orden de delegación (orquestador a subagente)
Incluye siempre cinco campos: OBJETIVO (una frase), ENTRADAS (rutas que debe leer), SALIDAS (rutas que debe producir), RESTRICCIONES (qué no tocar) y CRITERIO DE TERMINADO (verificable).

## Reporte de vuelta (subagente a orquestador)
Incluye siempre: ESTADO (COMPLETADO, BLOQUEADO o FALLIDO), ARCHIVOS (creados o modificados), EVIDENCIA (comando ejecutado y salida real), PENDIENTES (lo que no se pudo hacer o verificar) y DECISIONES (cambios respecto al diseño, si los hubo).

## Reglas
1. Un subagente nunca declara COMPLETADO sin evidencia de un comando o de la lectura del archivo.
2. Si falta información, el subagente responde BLOQUEADO con una pregunta concreta; no adivina.
3. El orquestador no reescribe el trabajo de un subagente: lo devuelve con el fallo exacto.
4. Máximo 3 ciclos de corrección entre desarrollador y probador; después el orquestador informa al usuario el estado real.

## Errores comunes
Reportes sin rutas; "todo bien" sin evidencia; delegar varias tareas distintas en una sola orden.
