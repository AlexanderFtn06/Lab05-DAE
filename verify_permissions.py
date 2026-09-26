import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client

User = get_user_model()

# Test login as editor
client = Client()
login_result = client.login(username='editor_test', password='editor12345')
print(f"Editor login: {login_result}")

# Check admin index page
response = client.get('/admin/')
print(f"Admin index status: {response.status_code}")
print(f"Admin index contains 'Movies': {'Movies' in response.content.decode()}")

# Check movie list page
response = client.get('/admin/movies/movie/')
print(f"Movie list status: {response.status_code}")

# Check if delete action is available
content = response.content.decode()
print(f"Movie list contains 'Delete selected': {'Delete selected' in content}")
print(f"Movie list contains 'Delete': {'Delete' in content and 'delete_selected' not in content}")

# Check add movie page
response = client.get('/admin/movies/movie/add/')
print(f"Add movie status: {response.status_code}")
print(f"Add movie accessible: {response.status_code == 200}")

# Check change movie page (need an existing movie)
from movies.models import Movie
movie = Movie.objects.first()
if movie:
    response = client.get(f'/admin/movies/movie/{movie.pk}/change/')
    print(f"Change movie status: {response.status_code}")
    print(f"Change movie accessible: {response.status_code == 200}")
    
    # Check if delete button is present
    content = response.content.decode()
    print(f"Change page contains 'Delete': {'Delete' in content}")

# Test login as superuser
admin_user = User.objects.filter(is_superuser=True).first()
if admin_user:
    client_admin = Client()
    # Can't easily test superuser login without password, but we know they have all perms
    print(f"\nSuperuser exists: {admin_user.username}")
    print(f"Superuser has all perms: {admin_user.has_perm('movies.delete_movie')}")

# Editor permissions check
editor = User.objects.get(username='editor_test')
print(f"\nEditor permissions:")
print(f"  has add_movie: {editor.has_perm('movies.add_movie')}")
print(f"  has change_movie: {editor.has_perm('movies.change_movie')}")
print(f"  has delete_movie: {editor.has_perm('movies.delete_movie')}")
print(f"  has view_movie: {editor.has_perm('movies.view_movie')}")
print(f"  has add_genre: {editor.has_perm('movies.add_genre')}")
print(f"  has change_genre: {editor.has_perm('movies.change_genre')}")
print(f"  has delete_genre: {editor.has_perm('movies.delete_genre')}")
print(f"  has add_person: {editor.has_perm('movies.add_person')}")
print(f"  has change_person: {editor.has_perm('movies.change_person')}")
print(f"  has delete_person: {editor.has_perm('movies.delete_person')}")
print(f"  has add_rating: {editor.has_perm('movies.add_rating')}")
print(f"  has change_rating: {editor.has_perm('movies.change_rating')}")
print(f"  has delete_rating: {editor.has_perm('movies.delete_rating')}")
print(f"  has view_rating: {editor.has_perm('movies.view_rating')}")