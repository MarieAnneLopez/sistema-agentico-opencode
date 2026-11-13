---
name: diseno-de-software
description: Produce un diseño técnico a partir de los requisitos: módulos, interfaces, flujo de datos, estructura de carpetas y decisiones justificadas. Usar después de analisis-de-requisitos y antes de escribir código.
---
# Diseño de software

## Cuándo usar
Existe docs/REQUISITOS.md y todavía no hay código en src/.

## Procedimiento
1. Lee docs/REQUISITOS.md completo. No diseñes nada que no tenga un RF asociado.
2. Elige lenguaje y dependencias: prefiere la biblioteca estándar. Justifica cualquier dependencia externa.
3. Divide en módulos pequeños con una sola responsabilidad. Por módulo: nombre, propósito, funciones públicas con firma (parámetros y retorno) y errores que puede lanzar.
4. Describe el flujo de datos de extremo a extremo en pasos numerados.
5. Define la estructura de carpetas: src/ para código y tests/ para pruebas.
6. Registra decisiones con el formato "Decisión | Alternativa descartada | Motivo".
7. Traza cada RF a los módulos que lo cumplen (tabla de trazabilidad).

## Formato de salida
docs/DISENO.md con secciones: Resumen, Lenguaje y dependencias, Módulos, Flujo de datos, Estructura de carpetas, Decisiones, Trazabilidad RF a módulo.

## Checklist de calidad
- Todo RF aparece en la tabla de trazabilidad.
- Cada función pública tiene firma completa.
- No hay módulos sin uso ni funcionalidades extra.

## Errores comunes
Sobre-ingeniería (capas o patrones innecesarios); firmas ambiguas; diseño que ignora los RNF.
