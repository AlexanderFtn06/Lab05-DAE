---
description: "Create editors group with add/change movie permissions but no delete, test user"
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# movies-permissions

## Objetivo
Paso 9: Crear un grupo "editores" con permisos `add_movie` y `change_movie` pero **sin** `delete_movie`, y un usuario de prueba dentro de ese grupo. Documentar, entrando con esa cuenta, qué opciones desaparecen del panel comparado con el superusuario.

## Instrucciones

### 1. Crear grupo y permisos via Django Admin
- Ir a `http://127.0.0.1:8000/admin/auth/group/` → "Add Group".
- Nombre: **editors**.
- Permisos → seleccionar:
  - `movies | movie | Can add movie` (`add_movie`)
  - `movies | movie | Can change movie` (`change_movie`)
  - `movies | movie | Can view movie` (`view_movie`) — *se añade automáticamente en Django 2.1+*
  - `movies | genre | Can view genre` (`view_genre`)
  - `movies | genre | Can add genre` (`add_genre`)
  - `movies | genre | Can change genre` (`change_genre`)
  - `movies | person | Can view person` (`view_person`)
  - `movies | person | Can add person` (`add_person`)
  - `movies | person | Can change person` (`change_person`)
  - `movies | rating | Can view rating` (`view_rating`)
  - `movies | rating | Can add rating` (`add_rating`)
  - `movies | rating | Can change rating` (`change_rating`)
- **NO seleccionar**: `delete_movie`, `delete_genre`, `delete_person`, `delete_rating`.
- Guardar.

### 2. Crear usuario de prueba
- Ir a `http://127.0.0.1:8000/admin/auth/user/` → "Add User".
- Username: `editor_test`
- Password: `editor12345` (o segura)
- Guardar → en permisos: **Groups** → añadir `editors`.
- **NO** marcar `is_staff` (se marca auto al asignar grupo con perms) ni `is_superuser`.
- Guardar.

### 3. Verificar permisos en shell (opcional)
```bash
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.get(username='editor_test')
print('Permisos:', [p.codename for p in u.user_permissions.all()])
print('Grupos:', [g.name for g in u.groups.all()])
for g in u.groups.all():
    print(f'  {g.name}:', [p.codename for p in g.permissions.all()])
"
```

### 4. Probar login como editor
- Cerrar sesión superusuario.
- Login con `editor_test` / `editor12345`.
- Ir a `http://127.0.0.1:8000/admin/`.

### 5. Documentar diferencias (captura mental o notas)
Comparar **Superusuario** vs **Editor**:

| Acción | Superusuario | Editor (grupo editors) |
|--------|--------------|------------------------|
| Ver lista Movies | ✅ | ✅ |
| Add Movie | ✅ | ✅ |
| Change Movie | ✅ | ✅ |
| **Delete Movie** | ✅ | ❌ (botón/action no aparece) |
| Ver/Add/Change Genre | ✅ | ✅ |
| **Delete Genre** | ✅ | ❌ |
| Ver/Add/Change Person | ✅ | ✅ |
| **Delete Person** | ✅ | ❌ |
| Ver/Add/Change Rating | ✅ | ✅ |
| **Delete Rating** | ✅ | ❌ |
| Inline Rating en Movie | ✅ (add/change/delete) | ✅ add/change, ❌ delete inline |
| Acceso a auth (Users/Groups) | ✅ | ❌ (no tiene perms) |

**Detalle clave**: En `MovieAdmin` con `RatingInline`, el editor **ve** el inline y puede **añadir/editar** ratings, pero **no puede borrar** ratings inline (falta `delete_rating`).

### 6. Verificar que no rompe nada
- Como editor: crear película, editarla, añadir rating inline → todo OK.
- Intentar borrar película → **no hay opción** (ni botón "Delete", ni action "Delete selected").
- Volver a superusuario → confirmar que todo sigue funcionando.

## Reglas obligatorias
- **No modificar** modelos ni admin de `library`.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Permisos asignados via **grupo** (no user_permissions directo).
- Documentar tabla comparativa para el entregable.
- Ante duda, **preguntar al usuario**.