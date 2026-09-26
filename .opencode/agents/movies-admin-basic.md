---
description: "Register 4 models in admin.py with simple admin.site.register"
mode: subagent
tools:
  write: true
  edit: true
---

# movies-admin-basic

## Objetivo
Paso 4: Registrar los 4 modelos en `movies/admin.py` con `admin.site.register` simple (sin `ModelAdmin` todavía), y comprobar que las 4 operaciones CRUD funcionan sin haber escrito ninguna vista.

## Instrucciones

### 1. Escribir admin.py básico
En `movies/admin.py`:
```python
from django.contrib import admin
from .models import Genre, Person, Movie, Rating

admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Rating)
```

### 2. Verificar en Django Admin
- Iniciar servidor: `python manage.py runserver`
- Entrar a `http://127.0.0.1:8000/admin/` con superusuario.
- Confirmar que aparecen **4 secciones**: Genres, People, Movies, Ratings.

### 3. Probar CRUD completo (sin vistas propias)
Para **cada modelo**:
- **Create**: botón "Add" → rellenar campos → "Save" → verificar en lista.
- **Read**: lista muestra `__str__` correcto; detalle al hacer clic.
- **Update**: editar registro → cambiar campo → "Save" → verificar cambio.
- **Delete**: seleccionar → "Delete selected" → confirmar → verificar desaparición.

Casos específicos:
- **Genre**: crear "Action", "Drama", "Sci-Fi", "Comedy".
- **Person**: crear director y actor, con y sin foto.
- **Movie**: crear película con géneros (M2M), póster, sinopsis.
- **Rating**: crear valoración 1-10 en película existente, con comentario.

### 4. Verificar cascada (Rating → Movie)
- Crear película + 2-3 ratings.
- Borrar la película desde admin.
- Confirmar que **sus ratings también se borran** (CASCADE funcionando).

### 5. Verificar campos readonly automáticos
- `created_at` y `updated_at` en Movie: no editables en formulario (auto_now_add/auto_now).
- `created_at` en Rating: no editable.

## Reglas obligatorias
- **No usar** `ModelAdmin` todavía (solo `admin.site.register`).
- **No modificar** `library/admin.py`.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Seguir exactamente `docs/movies-data-model-spec.md` (nombres de modelos/campos).
- Ante duda, **preguntar al usuario**.