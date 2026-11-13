---
name: analisis-de-requisitos
description: Convierte una idea vaga de programa en requisitos funcionales, no funcionales, supuestos y criterios de aceptación verificables. Usar al inicio de cualquier proyecto, antes de diseñar o programar.
---
# Análisis de requisitos

## Cuándo usar
Al recibir una petición nueva o ambigua, antes de diseñar.

## Procedimiento
1. Reformula el objetivo en una frase: "Un [usuario] podrá [acción] para [resultado]".
2. Lista requisitos funcionales numerados RF-01, RF-02... Cada uno con un solo verbo de acción.
3. Lista requisitos no funcionales relevantes (lenguaje, rendimiento, portabilidad, dependencias permitidas) como RNF-01...
4. Escribe criterios de aceptación CA-01... con el formato "Dado X, cuando Y, entonces Z". Deben poder verificarse con un comando o una prueba.
5. Anota supuestos explícitos. Si falta información crítica, haz como máximo 3 preguntas al usuario; si no responde, usa el supuesto más simple y regístralo.
6. Define lo que queda FUERA de alcance.

## Formato de salida
docs/REQUISITOS.md con secciones: Objetivo, Alcance, Fuera de alcance, RF, RNF, CA, Supuestos.

## Checklist de calidad
- Cada RF tiene al menos un CA.
- Ningún requisito usa palabras vagas ("rápido", "bonito") sin un número.
- Máximo 10 RF para un primer ciclo.

## Errores comunes
Mezclar requisitos con diseño; inventar requisitos que el usuario no pidió; criterios que no se pueden comprobar.
