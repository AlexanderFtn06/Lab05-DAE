---
description: "Load test data via admin: 10 movies, 4 genres, ratings on 5+ movies"
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# movies-admin-data

## Objetivo
Paso 8: Cargar datos de prueba desde el panel de administración: diez películas, cuatro géneros, y valoraciones en al menos cinco películas.

## Instrucciones

### 1. Acceder al admin
- `http://127.0.0.1:8000/admin/` con superusuario.

### 2. Crear 4 géneros (Genre)
Usar "Add Genre" → crear:
1. **Action**
2. **Drama**
3. **Science Fiction**
4. **Comedy**

Verificar en lista: 4 filas, `movie_count = 0`.

### 3. Crear personas (Person) - opcional pero recomendado
Crear al menos 4 personas (2 directores, 2 actores) para asociar luego si se desea:
- Christopher Nolan (director)
- Denis Villeneuve (director)
- Leonardo DiCaprio (actor)
- Amy Adams (actor)

(Opcional: subir fotos en `photo` para probar preview).

### 4. Crear 10 películas (Movie)
Usar "Add Movie" → crear estas 10 (título, año, sinopsis, póster opcional, géneros M2M):

| # | Título | Año | Géneros | Sinopsis breve |
|---|--------|-----|---------|----------------|
| 1 | Inception | 2010 | Action, Science Fiction | A thief who steals corporate secrets through dream-sharing technology. |
| 2 | The Dark Knight | 2008 | Action, Drama | Batman faces the Joker in a battle for Gotham's soul. |
| 3 | Interstellar | 2014 | Science Fiction, Drama | Explorers travel through a wormhole to save humanity. |
| 4 | Dune | 2021 | Science Fiction, Drama | Paul Atreides leads nomadic tribes on Arrakis. |
| 5 | The Grand Budapest Hotel | 2014 | Comedy, Drama | A legendary concierge and his protégé in a fictional European hotel. |
| 6 | Parasite | 2019 | Drama, Comedy | A poor family schemes to infiltrate a wealthy household. |
| 7 | Mad Max: Fury Road | 2015 | Action, Science Fiction | Max helps Furiosa escape a tyrant in a post-apocalyptic wasteland. |
| 8 | Arrival | 2016 | Science Fiction, Drama | Linguist deciphers alien language to prevent global war. |
| 9 | The Martian | 2015 | Science Fiction, Comedy | Astronaut stranded on Mars survives with ingenuity. |
| 10 | Knives Out | 2019 | Comedy, Drama | Detective investigates a wealthy patriarch's death. |

- Asignar géneros usando `filter_horizontal` (widget M2M).
- Subir pósters opcionales (carpeta `media/movies/`).

### 5. Crear valoraciones (Rating) en al menos 5 películas
Para cada película, añadir 2-3 ratings via **inline** en `MovieAdmin` (o directo en Rating admin):

| Película | Ratings (score, comment) |
|----------|--------------------------|
| Inception | 9, "Mind-bending masterpiece"; 8, "Complex but rewarding" |
| The Dark Knight | 10, "Best superhero film ever"; 9, "Heath Ledger is iconic" |
| Interstellar | 9, "Visual and emotional journey"; 7, "A bit long but beautiful" |
| Dune | 9, "Epic adaptation"; 8, "Stunning cinematography" |
| Parasite | 10, "Perfect thriller"; 9, "Sharp social commentary" |

(Otras 5 películas: añadir 1-2 ratings cada una).

### 6. Verificar datos
- En `MovieAdmin` lista: comprobar `genre_list` y `avg_rating` calculados.
- En `RatingAdmin`: ver todas las valoraciones con scores 1-10.
- Probar filtros: por género, por año, por score.
- Probar búsqueda: por título, por nombre de persona.

### 7. Documentar
Anotar credenciales usadas y captura mental de los datos para pasos posteriores.

## Reglas obligatorias
- **Solo** via panel de admin (Django Admin), **no** scripts ni fixtures.
- Scores entre 1-10 (validado por modelo).
- Código y comentarios en **INGLÉS**. Explicaciones al usuario en **ESPAÑOL**.
- Seguir `docs/movies-data-model-spec.md`.
- Ante duda, **preguntar al usuario**.