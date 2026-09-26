---
description: "Generate and apply migrations, create superuser if needed"
mode: subagent
tools:
  bash: true
  read: true
---

# movies-migrations

## Objetivo
Paso 3: Generar y aplicar migraciones, y crear el superusuario del proyecto (si no existe ya uno de la semana anterior, reutilizarlo).

## Instrucciones

### 1. Verificar migraciones existentes
```bash
python manage.py showmigrations
```
Comprobar si ya hay migraciones de `movies` (no debería haberlas en este paso).

### 2. Generar migraciones
```bash
python manage.py makemigrations movies
```
- Verificar que se crea `movies/migrations/0001_initial.py`.
- Leer el archivo generado para confirmar que coincide con la spec.

### 3. Aplicar migraciones
```bash
python manage.py migrate
```
- Confirmar que se aplican sin errores.
- Verificar tablas creadas en BD (opcional: `python manage.py dbshell` + `.schema movies_*`).

### 4. Superusuario
Comprobar si ya existe superusuario de la semana anterior:
```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())"
```

**Si NO existe**: crear uno nuevo:
```bash
python manage.py createsuperuser
# Seguir prompts: username, email, password
```

**Si YA existe**: reutilizarlo, **no crear otro**. Documentar credenciales usadas (sin escribir password en código).

### 5. Verificar modelos en shell
```bash
python manage.py shell -c "
from movies.models import Genre, Person, Movie, Rating
print('Genre:', Genre._meta.fields)
print('Person:', Person._meta.fields)
print('Movie:', Movie._meta.fields)
print('Rating:', Rating._meta.fields)
"
```

## Reglas obligatorias
- **No modificar** la app `library` ni sus migraciones.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Seguir exactamente `docs/movies-data-model-spec.md`.
- Si `makemigrations` detecta cambios en `library`, **parar y preguntar**.
- Ante duda, **preguntar al usuario**.