---
name: revision-de-codigo
description: Revisa en modo solo lectura el código de src/ contra el diseño y los requisitos, y emite hallazgos por severidad con ubicación exacta. Usar cuando las pruebas pasan y antes de dar el trabajo por terminado.
---
# Revisión de código

## Cuándo usar
Las pruebas pasan y falta una revisión final antes de entregar.

## Procedimiento
1. Lee docs/DISENO.md y los archivos de src/. NO modifiques ningún archivo.
2. Comprueba en este orden: (a) cumple los RF y CA; (b) coincide con las firmas del diseño; (c) validación de entradas y manejo de errores; (d) funciones largas o duplicadas; (e) secretos, rutas absolutas o dependencias no declaradas.
3. Por cada hallazgo registra: severidad (BLOQUEANTE, MEDIO o MENOR), archivo:línea, qué ocurre y el cambio sugerido en una frase.
4. Marca BLOQUEANTE solo si incumple un RF o CA, rompe una firma del diseño o introduce un riesgo de seguridad.
5. No reportes hallazgos que no puedas señalar en una línea concreta.

## Formato de salida
Lista de hallazgos ordenada por severidad y un veredicto final: APROBADO (sin bloqueantes) o RECHAZADO (con bloqueantes).

## Checklist de calidad
- Cada hallazgo tiene archivo:línea.
- El veredicto es coherente con los hallazgos.

## Errores comunes
Presentar opiniones de estilo como bloqueantes; reportar sin leer el archivo; editar código durante la revisión.
