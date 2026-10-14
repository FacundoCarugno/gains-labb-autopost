# gains-labb-autopost

Publica a las **19:00 (America/Argentina/Buenos_Aires)** el Reel del dia de @gains.labb desde GitHub Actions (no necesita tu PC).

- `schedule.json`: calendario + registro persistente (estado, IDs de Instagram, comentario, errores, reintentos). Dias 8-12 cargados (14-18/10/2026).
- `autopost/publish.py`: logica (1 Reel por fecha, no avanza si falla, no duplica, no sustituye videos). `autopost/igapi.py`: cliente de la API oficial de Instagram.
- `videos/`: los MP4. El video de cada dia sale del campo `video` de su fila en `schedule.json`.
- `tests/run_tests.py`: 17 pruebas contra un servidor Meta simulado (no publica nada real).
- `engine/`: motor de generacion de videos (solo para crear nuevos dias; agregar el dia en `schedule.json` y su MP4 en `videos/`).

## Puesta en marcha (una sola vez)
**A. Meta (Instagram con Instagram Login, gratis)**
1. Cuenta @gains.labb como *Profesional* (Creador).
2. developers.facebook.com -> Crear app (tipo Business) -> agregar producto **Instagram** -> "API setup with Instagram login".
3. Agregar tu cuenta como Instagram Tester (App roles) y aceptar la invitacion en Instagram. Permisos: `instagram_business_basic`, `instagram_business_content_publish`, `instagram_business_manage_comments`.
4. En la misma pantalla "Generate token" para @gains.labb. Copiar el **token** y el **Instagram user ID**. (Dura 60 dias: renovar cada ~50.)

**B. GitHub (repo PUBLICO, gratis)**
1. Crear repo publico `gains-labb-autopost` y subir esta carpeta.
2. Settings -> Secrets and variables -> Actions: `IG_ACCESS_TOKEN`, `IG_USER_ID`.
3. Settings -> Pages -> Source: *Deploy from a branch* -> `main` / root. Settings -> Actions -> General -> Workflow permissions: *Read and write*.
4. Actions -> "Validar configuracion" -> Run workflow (comprueba token sin publicar).

## Comprobar que funciona
Actions -> "Publicar Reel diario" (cada corrida), `schedule.json` (`publish_status`, `ig_media_id`), `logs/publish.log`. Si falla se abre un Issue (llega email).
Limites honestos: la API **no permite fijar comentarios** (se publica el comentario, el fijado es manual); GitHub puede demorar los cron unos minutos (el workflow arranca 20 min antes y espera a las 19:00); tras 60 dias sin actividad GitHub pausa los cron (el bot commitea cada dia, asi que no ocurre).
