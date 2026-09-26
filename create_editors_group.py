import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import Group, Permission, User

# Create editors group
editors_group, created = Group.objects.get_or_create(name='editors')
print(f'Group editors created: {created}')

# Get permissions (excluding delete permissions)
perms = Permission.objects.filter(
    content_type__app_label='movies'
).exclude(codename__startswith='delete_')

editors_group.permissions.set(perms)
print(f'Permissions assigned: {list(editors_group.permissions.values_list("codename", flat=True))}')

# Create test user
editor_user, created = User.objects.get_or_create(username='editor_test')
if created:
    editor_user.set_password('editor12345')
    editor_user.save()
    print('User editor_test created')
else:
    print('User editor_test already exists')

# Add user to group
editor_user.groups.add(editors_group)
editor_user.is_staff = True
editor_user.save()
print(f'User groups: {list(editor_user.groups.values_list("name", flat=True))}')
print(f'User is_staff: {editor_user.is_staff}')