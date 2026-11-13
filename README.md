# Sistema agéntico para OpenCode

## Propósito
Sistema multiagente para OpenCode que lleva una idea de programa desde los
requisitos hasta el código probado y revisado: 1 agente orquestador y
3 subagentes (diseñador, desarrollador, probador), apoyados en 6 skills.

## Arquitectura
| Agente | Rol | Skills | Entrada | Salida |
|---|---|---|---|---|
| orquestador | Coordina, delega e informa | handoff-entre-agentes, analisis-de-requisitos (paso 5) | Petición del usuario | Informe con evidencia |
| disenador | Requisitos y diseño | analisis-de-requisitos, diseno-de-software, handoff-entre-agentes | Orden de delegación | docs/REQUISITOS.md, docs/DISENO.md |
| desarrollador | Implementa y corrige | escritura-de-codigo, handoff-entre-agentes | Diseño y fallos reportados | Código en src/ |
| probador | Prueba y revisa | pruebas-y-verificacion, revision-de-codigo, handoff-entre-agentes | Código y requisitos | Pruebas en tests/ y veredicto |

## Flujo de trabajo
1. El orquestador aclara la petición con como máximo 3 preguntas al usuario.
2. El orquestador delega en `disenador`: docs/REQUISITOS.md y docs/DISENO.md.
3. El orquestador delega en `desarrollador`: implementación en src/.
4. El orquestador delega en `probador`: pruebas en tests/, ejecución y revisión.
5. Si hay fallos o veredicto RECHAZADO, el fallo vuelve a `desarrollador`.
   Máximo 3 ciclos de corrección.
6. El orquestador informa al usuario con evidencia real.

## Estructura de carpetas
- `.opencode/agents/` — los 4 agentes en markdown con frontmatter.
- `.opencode/skills/<nombre>/SKILL.md` — las 6 skills.
- `docs/` — REQUISITOS.md y DISENO.md (los crea el diseñador al trabajar).
- `src/` — código fuente (lo crea el desarrollador al trabajar).
- `tests/` — pruebas (las crea el probador al trabajar).

## Cómo usarlo
1. Abre OpenCode en la raíz de este repositorio.
2. Selecciona el agente `orquestador`.
3. Pide tu programa, por ejemplo: "Quiero un programa que cuente las líneas
   de los archivos .txt de una carpeta y muestre un resumen".

## Limitaciones
Usa el modelo gratuito disponible, sin garantía de disponibilidad ni de
rendimiento constante. La calidad depende del modelo activo en cada sesión.
