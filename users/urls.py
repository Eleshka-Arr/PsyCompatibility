from django.urls import path
from users.views import view_commands, view_command, create_command_role, view_command_role, create_command, \
    delete_command, delete_command_user_role

urlpatterns = [
    path('commands/view', view_commands, name='view_commands'),
    path('commands/view/<int:command_id>', view_command, name='view_command'),
    path('commands/view/<int:command_id>/view-role/<int:role_id>', view_command_role, name='view_command_role'),
    path('commands/view/<int:command_id>/create-role/<int:role_id>', create_command_role, name='create_command_role'),
    path('commands/create', create_command, name='create_command'),
    path('commands/delete/<int:command_id>', delete_command, name='delete_command'),
    path('commands/view/<int:command_id>/delete-user-role/<int:user_role_id>', delete_command_user_role,
         name='delete_command_user_role')
]
