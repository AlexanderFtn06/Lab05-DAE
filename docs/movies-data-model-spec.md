# Movies Data Model Specification (Lab 5)

**Única fuente de verdad** para todos los sub-agentes que trabajen en la app `movies`.  
Esta app es **independiente** de la app `library` existente; **no modificar** `library`.

---

## 1. Genre

| Campo | Tipo | Opciones |
|-------|------|----------|
| `name` | `CharField` | `max_length=100`, `unique=True` |

### Meta
- `ordering = ["name"]`

### `__str__`
```python
def __str__(self):
    return self.name
```

---

## 2. Person

| Campo | Tipo | Opciones |
|-------|------|----------|
| `first_name` | `CharField` | `max_length=100` |
| `last_name` | `CharField` | `max_length=100` |
| `role` | `CharField` | `max_length=20`, `choices=[("director", "Director"), ("actor", "Actor")]` |
| `photo` | `ImageField` | `upload_to="people/"`, `blank=True`, `null=True` |

### Meta
- `ordering = ["last_name", "first_name"]`

### `__str__`
```python
def __str__(self):
    return f"{self.first_name} {self.last_name}"
```

---

## 3. Movie

| Campo | Tipo | Opciones |
|-------|------|----------|
| `title` | `CharField` | `max_length=200` |
| `release_year` | `PositiveSmallIntegerField` | — |
| `synopsis` | `TextField` | `blank=True` |
| `poster` | `ImageField` | `upload_to="movies/"`, `blank=True`, `null=True` |
| `created_at` | `DateTimeField` | `auto_now_add=True` |
| `updated_at` | `DateTimeField` | `auto_now=True` |
| `genres` | `ManyToManyField` | `to="Genre"`, `related_name="movies"`, `blank=True` |

### Meta
- `ordering = ["-release_year", "title"]`

### `__str__`
```python
def __str__(self):
    return f"{self.title} ({self.release_year})"
```

---

## 4. Rating

| Campo | Tipo | Opciones |
|-------|------|----------|
| `movie` | `ForeignKey` | `to="Movie"`, `on_delete=models.CASCADE`, `related_name="ratings"` |
| `score` | `PositiveSmallIntegerField` | `validators=[MinValueValidator(1), MaxValueValidator(10)]` |
| `comment` | `TextField` | `blank=True` |
| `created_at` | `DateTimeField` | `auto_now_add=True` |

### Justificación de `on_delete=CASCADE`
> Una valoración (Rating) **no tiene sentido sin la película** a la que pertenece.  
> Al borrar la película, es correcto y consistente borrar en cascada sus valoraciones asociadas.  
> Esto difiere del laboratorio anterior donde se usó `PROTECT` para preservar integridad referencial en otro contexto.

### Meta
- `ordering = ["-created_at"]`

### `__str__`
```python
def __str__(self):
    return f"{self.movie} — {self.score}/10"
```

---

## 5. Restricciones y notas transversales

1. **Nombres de campos inmutables**: No cambiar ningún `field name` en pasos posteriores.
2. **Validaciones**: `score` en Rating **debe** validarse entre 1 y 10 (incluir validators en el modelo).
3. **Related names**:
   - `Genre.movies` → acceso inverso desde género a películas.
   - `Movie.ratings` → acceso inverso desde película a valoraciones.
4. **Upload paths**:
   - `Person.photo` → `people/`
   - `Movie.poster` → `movies/`
5. **Dependencias**: Requiere `Pillow` en `requirements.txt` para `ImageField`.
6. **Admin**: Registrar los 4 modelos en `movies/admin.py` con list_display útiles y search_fields.

---

## 6. Checklist de implementación (para sub-agentes)

- [ ] Crear app `movies` y añadir a `INSTALLED_APPS`.
- [ ] Declarar modelos exactamente como arriba en `movies/models.py`.
- [ ] Generar y aplicar migraciones (`makemigrations`, `migrate`).
- [ ] Registrar modelos en `movies/admin.py`.
- [ ] Configurar `MEDIA_URL` / `MEDIA_ROOT` en `settings.py` (si no existe) y servir media en desarrollo.
- [ ] Verificar en Django Admin: CRUD completo, filtros, búsquedas, inline para `Rating` en `MovieAdmin`.
- [ ] Probar cascade delete: borrar una `Movie` → sus `Rating` desaparecen.
- [ ] Documentar cualquier decisión de diseño en este archivo (append-only).

---

> **Nota**: Si algo no queda claro, **preguntar antes de improvisar**. Este documento es la especificación contractual.