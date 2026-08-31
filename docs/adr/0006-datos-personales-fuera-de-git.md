# ADR-0006 · Los datos personales viven fuera de git

- **Estado:** aceptada
- **Fecha:** 2026-08-31

## Contexto

Para razonar sobre fiscalidad, altas y compatibilidades, finanzas-legal necesita conocer la situación administrativa de la persona fundadora: altas anteriores, trámites pendientes, prestaciones… En el prototipo estos datos estaban en `contexto.md`, versionado.

El repositorio es, además, portafolio: puede acabar siendo público. Y lo que entra en el historial de git es muy difícil de sacar de él.

## Decisión

1. Los datos personales y administrativos van en **`empresa/privado/`**, que está en `.gitignore` (salvo su `README.md`).
2. `contexto.md` solo recoge las **consecuencias** que el comité debe asumir («probablemente no aplica la tarifa plana ⚖️»), nunca el dato que las origina.
3. Los agentes pueden leer `empresa/privado/`, pero no escribir en él, y en los ficheros versionados escriben la consecuencia, no el dato (protocolo §10).
4. La persona fundadora mantiene en `empresa/privado/terminos-sensibles.txt` una lista de términos que nunca deben aparecer en ficheros versionados; una herramienta los busca antes de cada commit (ver ADR-0004).

## Alternativas consideradas

| Alternativa | Por qué no |
|---|---|
| Dejarlo en `contexto.md` y confiar en no publicar el repositorio | Un error lo publica para siempre |
| Cifrar los ficheros (git-crypt, sops) | Más herramientas y claves que gestionar para un solo usuario; los agentes no podrían leerlos sin pasos extra |
| No dar esos datos al comité | Finanzas-legal daría recomendaciones genéricas o equivocadas en lo que más consecuencias tiene |

## Consecuencias

- **Positivas:** el repositorio se puede hacer público sin revisar el historial; las recomendaciones fiscales siguen teniendo en cuenta la situación real.
- **Negativas y riesgos:**
  - Al clonar en otra máquina, `empresa/privado/` no está: hay que copiarlo a mano. El `README.md` de la carpeta explica qué ficheros esperar.
  - Un agente puede copiar un dato sensible en su ronda. → La regla del protocolo, más `pba.py privacidad` como red de seguridad.
- **Cómo sabremos si fue un error:** si el detector encuentra fugas en más de una reunión, la regla no basta y habrá que filtrar lo que leen los agentes.
