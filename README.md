# Cinema Vault
## Autor
Alexander Faustino
Proyecto de laboratorio 5 ("Administrador con Django") del curso
**Desarrollo de Aplicaciones Empresariales**. Cinema Vault es un catálogo
de películas donde cualquier visitante —sin necesidad de iniciar
sesión— puede descubrir las mejor valoradas y filtrarlas por género,
mientras que el panel de administración permite gestionar el catálogo
con columnas, filtros, búsqueda y edición en línea de valoraciones.

## Descripción

La aplicación tiene dos capas claramente separadas:

- **Sitio público**: listado de películas ordenadas por valoración
  promedio, filtro por género, y una página de detalle por película con
  su sinopsis, géneros y todas sus reseñas individuales.
- **Panel de administración**: gestión completa del catálogo
  (películas, géneros, personas y valoraciones), con permisos
  diferenciados entre un superusuario y un grupo de "editores" con
  acceso restringido.

## Capacidades demostradas

Este proyecto cumple las tres capacidades del laboratorio 5:

1. **Configura el administrador de Django para gestionar un conjunto de
   modelos relacionados.** Los cuatro modelos (`Movie`, `Genre`,
   `Person`, `Rating`) están registrados en el admin, con sus relaciones
   operando ahí mismo: el género (muchos a muchos) se asigna con un
   selector horizontal, y las valoraciones (clave foránea) se dan de
   alta como bloque en línea dentro del propio formulario de la
   película. 
2. **Personaliza el listado, los filtros y la búsqueda de cada modelo
   con `ModelAdmin`.** El listado de películas muestra columnas útiles
   (título, año, géneros, valoración promedio), con filtro lateral por
   género y por año, y una barra de búsqueda por título y por nombre de
   persona.
3. **Administra el acceso al panel mediante usuarios, grupos y
   permisos.** Existe un grupo "editores" con permisos para agregar y
   modificar películas, pero sin permiso para eliminarlas; al entrar con
   una cuenta de ese grupo, desaparecen tanto el acceso a
   Usuarios/Grupos como el botón de eliminar.



## Modelo de datos

| Modelo | Relación | Descripción |
|---|---|---|
| `Genre` | — | Género cinematográfico (Acción, Comedia, Drama, Ciencia Ficción). |
| `Person` | — | Director o actor: nombre, rol, foto. |
| `Movie` | `ManyToManyField` → `Genre` | Película: título, año, sinopsis, póster, fecha de creación/modificación. |
| `Rating` | `ForeignKey` → `Movie` (CASCADE) | Valoración de 1 a 10 con comentario, asociada a una película. |

El esquema completo está en
[`docs/movies-data-model-spec.md`](docs/movies-data-model-spec.md).



## Metodología de desarrollo (OpenCode)

Este proyecto se desarrolló usando [OpenCode](https://opencode.ai), un
agente de código con IA, apoyado en **sub-agentes especializados**, cada
uno encargado de una parte específica del procedimiento:

| Sub-agente | Encargado de |
|---|---|
| `movies-project-structure` | Crear la app `movies` e instalar Pillow. |
| `movies-models` | Declarar los 4 modelos y sus relaciones. |
| `movies-migrations` | Generar y aplicar migraciones. |
| `movies-admin-basic` | Registro simple de los modelos en el admin. |
| `movies-admin-custom` | `ModelAdmin` personalizado, inline, campos de solo lectura. |
| `movies-admin-data` | Carga de datos de prueba. |
| `movies-permissions` | Grupo "editores" y control de permisos. |
| `movies-views` | Vistas públicas de listado, filtro por género y detalle. |
| `movies-documentation` | Evidencia del laboratorio. |

## Instalación y uso

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd Lab05-DAE

# 2. Crear y activar un entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear un superusuario para acceder al admin
python manage.py createsuperuser

# 6. Correr el servidor de desarrollo
python manage.py runserver
```

Luego abre:
- `http://127.0.0.1:8000/` — catálogo público de películas mejor valoradas
- `http://127.0.0.1:8000/genre/<slug>/` — recomendaciones filtradas por género
- `http://127.0.0.1:8000/<id>/` — detalle de una película
- `http://127.0.0.1:8000/admin/` — panel de administración

## Capturas de funcionamiento

### Panel de administración

**1. Sección MOVIES del admin con los 4 modelos listados**

<img width="1118" height="734" alt="01-admin-modelos-movies" src="https://github.com/user-attachments/assets/1aa5bbe0-fc72-4014-9bf9-dd826bbbd572" />

**2. Listado de películas en el admin, con columnas, filtros y búsqueda**

<img width="1920" height="962" alt="02-admin-movies-listado-filtros" src="https://github.com/user-attachments/assets/cccd558c-f6c8-425b-8a38-68d67976ac71" />

**3. Detalle de una película en el admin: valoraciones en línea y campos de auditoría de solo lectura**

<img width="1623" height="809" alt="03-admin-movie-detalle-inline-readonly" src="https://github.com/user-attachments/assets/c9f2a817-82f7-45ca-82ea-c32c80d8d71e" />

### Permisos por grupo

**4. Panel de administración visto por el superusuario, con acceso a Usuarios y Grupos**

<img width="1118" height="734" alt="04-admin-superusuario-panel" src="https://github.com/user-attachments/assets/07dd406e-1885-4160-95e8-707c738770ae" />

**5. Mismo panel visto por el usuario del grupo "editores", sin acceso a Usuarios/Grupos**

<img width="1920" height="554" alt="05-admin-editor-panel-restringido" src="https://github.com/user-attachments/assets/a505fea4-d4ac-4f3a-a8d1-3c968ca684b7" />

### Sitio público

<img width="1920" height="954" alt="image" src="https://github.com/user-attachments/assets/6232fe11-0ef6-4b39-bced-986973d4883c" />

<img width="1905" height="958" alt="image" src="https://github.com/user-attachments/assets/e84a05fb-3191-4711-9c66-1cfb0ee810f8" />

<img width="1810" height="941" alt="image" src="https://github.com/user-attachments/assets/d7e0be3f-1ac6-4ee9-9f29-7f9ecc64a8c8" />

