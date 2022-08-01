from django.contrib import admin
from users.models import Role, Command, UserRole

admin.site.register(Role)
admin.site.register(Command)
admin.site.register(UserRole)
