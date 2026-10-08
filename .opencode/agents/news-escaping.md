---
description: "Paso 12: probar el escapado automático. Guardar en el cuerpo de una noticia de prueba una etiqueta HTML, documentar qué muestra la página y por qué (autoescape convierte <, >, & y comillas en entidades). Mostrar el contraste con |safe solo en el shell o en la documentación, NUNCA en las plantillas del proyecto. Al terminar, eliminar la noticia de prueba para que queden solo las seis oficiales."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-escaping

## Objetivo
Verificar y documentar el escapado automático de Django en plantillas.

## Instrucciones
1. En el admin (`/admin/news/article/add/`), crear una **noticia de prueba** temporal:
   - Título: "Test Escaping"
   - Slug: "test-escaping"
   - Cuerpo: `<script>alert('xss')</script> <b>Negrita</b> & "comillas" <tag>`
   - Autor y categoría cualquiera.
   - Publicar.
2. Visitar `/news/article/test-escaping/` en el navegador.
3. **Observar y documentar**: el HTML se muestra **como texto plano** (entidades: `<script>alert('xss')</script> <b>Negrita</b> & "comillas" <tag>`). Django escapa automáticamente `<`, `>`, `&`, `'` y `"` en variables `{{ ... }}`.
4. **Contraste con `|safe`** (solo para documentación, **nunca en plantillas del proyecto**):
   - En shell: `python manage.py shell -c "from django.template import Template, Context; t = Template('{{ body|safe }}'); print(t.render(Context({'body': \"<b>hola</b>\"})))"` → muestra HTML renderizado.
   - Explicar: `|safe` desactiva el escapado; **peligroso** si el contenido viene de usuarios.
5. **Eliminar la noticia de prueba** desde el admin o shell para que solo queden las 6 oficiales.
6. Añadir una nota en la documentación final (paso 13) explicando esto.

## Reglas
- Código y comentarios en INGLÉS.
- **Nunca** usar `|safe` ni `{% autoescape off %}` en plantillas del proyecto.
- El escapado automático debe permanecer activo siempre.
- Seguir `docs/news-data-model-spec.md` como única fuente de verdad.