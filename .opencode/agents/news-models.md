---
description: "Paso 3: declarar Author, Category y Article según el spec, con Meta y __str__. Justificar cada relación antes de escribirla. Generar y aplicar migraciones, y confirmar que el superusuario existente sigue funcionando (reutilizarlo, no crear otro)."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-models

## Instrucciones

Declarar los modelos en `news/models.py` según `docs/news-data-model-spec.md`:

### Author
- `first_name`: CharField(max_length=100)
- `last_name`: CharField(max_length=100)
- `bio`: TextField(blank=True)
- `photo`: ImageField(upload_to="authors/", blank=True, null=True)
- Meta: `ordering = ["last_name", "first_name"]`
- `__str__`: return f"{self.first_name} {self.last_name}"

### Category
- `name`: CharField(max_length=100, unique=True)
- `slug`: SlugField(max_length=100, unique=True)
- `description`: TextField(blank=True)
- Meta: `ordering = ["name"]`, `verbose_name_plural = "categories"`
- `__str__`: return self.name

### Article
- `title`: CharField(max_length=200)
- `slug`: SlugField(max_length=200, unique=True)
- `summary`: TextField()
- `body`: TextField()
- `featured_image`: ImageField(upload_to="articles/", blank=True, null=True)
- `published_at`: DateTimeField(default=timezone.now)
- `author`: ForeignKey(Author, on_delete=PROTECT, related_name="articles")
  - **Justificación**: PROTECT evita borrar un autor que tenga artículos publicados
- `categories`: ManyToManyField(Category, related_name="articles", blank=True)
  - **Justificación**: Un artículo puede tener múltiples categorías y viceversa
- Meta: `ordering = ["-published_at"]`
- `__str__`: return self.title

### Pasos posteriores
1. `python manage.py makemigrations news`
2. `python manage.py migrate`
3. Verificar superusuario existente: `python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())"` - NO crear otro

## Reglas

- Código y comentarios en INGLÉS
- Justificar cada relación ANTES de escribirla
- Seguir exactamente el spec