---
description: "Declare Movie, Genre, Person, Rating models per spec with Meta and __str__"
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# movies-models

## Objetivo
Paso 2: Declarar `Movie`, `Genre`, `Person` y `Rating` en `movies/models.py` siguiendo **exactamente** `docs/movies-data-model-spec.md`, con `Meta` y `__str__`. Antes de cada relación, justificar por qué es esa y no otra (M2M para géneros, FK con CASCADE para valoraciones).

## Instrucciones

### 1. Leer la especificación
Leer `docs/movies-data-model-spec.md` completo. **No inventar** campos ni nombres.

### 2. Escribir models.py
Crear `movies/models.py` con los 4 modelos en este orden: `Genre`, `Person`, `Movie`, `Rating`.

#### Genre
```python
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
```

#### Person
```python
class Person(models.Model):
    ROLE_CHOICES = [
        ("director", "Director"),
        ("actor", "Actor"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to="people/", blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

#### Movie
```python
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveSmallIntegerField()
    synopsis = models.TextField(blank=True)
    poster = models.ImageField(upload_to="movies/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField("Genre", related_name="movies", blank=True)

    class Meta:
        ordering = ["-release_year", "title"]

    def __str__(self):
        return f"{self.title} ({self.release_year})"
```

**Justificación M2M para géneros**: Una película puede tener múltiples géneros y un género pertenece a múltiples películas. Relación muchos-a-muchos bidireccional.

#### Rating
```python
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
    movie = models.ForeignKey(
        "Movie",
        on_delete=models.CASCADE,
        related_name="ratings"
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.movie} — {self.score}/10"
```

**Justificación FK con CASCADE**: Un `Rating` no tiene sentido sin su `Movie`. Al borrar la película, sus valoraciones pierden significado → `CASCADE` borra en cascada. Difiere del lab anterior donde se usó `PROTECT` para preservar integridad referencial en otro contexto.

### 3. Verificar
- Ejecutar `python manage.py check` para validar modelos.
- Confirmar que no hay errores de sintaxis ni referencias circulares.

## Reglas obligatorias
- **Nombres de campos inmutables**: no cambiar ningún `field name` respecto a la spec.
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Incluir `validators` en `score` (1-10).
- `related_name` exactos: `Genre.movies`, `Movie.ratings`.
- `upload_to`: `"people/"` y `"movies/"`.
- Ante ambigüedad, **preguntar al usuario** antes de improvisar.