---
description: "Paso 12: probar el escapado automático. Guardar en el cuerpo de una noticia de prueba una etiqueta HTML, documentar qué muestra la página y por qué (autoescape convierte <, >, & y comillas en entidades). Mostrar el contraste con |safe solo en el shell o en la documentación, NUNCA en las plantillas del proyecto. Al terminar, eliminar la noticia de prueba para que queden solo las seis oficiales."
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# news-escaping

## Instrucciones

### 1. Crear noticia de prueba (via admin o shell)
- Título: "Test Escaping"
- Slug: "test-escaping"
- Body: `<script>alert('xss')</script> <b>Bold</b> & "quotes" <tag>`
- Publicar

### 2. Verificar en el navegador
- Ir a `/news/article/test-escaping/`
- **Observar**: El HTML se muestra como **texto plano** (entidades: `<script>alert('xss')</script> <b>Bold</b> & "quotes" <tag>`)
- **Por qué**: Django autoescape convierte `<`, `>`, `&`, `'`, `"` en entidades HTML automáticamente en `{{ variable }}`

### 3. Contraste con `|safe` (SOLO en shell/documentación, NUNCA en plantillas)
```bash
python manage.py shell -c "
from django.template import Template, Context
t = Template('{{ body|safe }}')
print(t.render(Context({'body': '<b>Hola</b> <script>alert(1)</script>'})))
"
```
- Resultado: HTML renderizado (negrita + script ejecutable)
- **Explicar**: `|safe` desactiva autoescape - PELIGROSO si contenido viene de usuarios

### 4. Limpiar
- Eliminar noticia de prueba ("Test Escaping")
- Quedar solo las 6 oficiales

### 5. Documentar
- Qué se ve en la página
- Por qué (autoescape activo)
- Contraste con `|safe` solo en docs

## Reglas

- NUNCA usar `|safe` ni `{% autoescape off %}` en plantillas del proyecto
- Autoescape DEBE permanecer activo
- Código y comentarios en INGLÉS
- Explicación para usuario en ESPAÑOL