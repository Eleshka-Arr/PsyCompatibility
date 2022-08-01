from django.shortcuts import render, redirect

from quiz.models import Result, ResultPattern
from users.models import Command, Role, UserRole


def create_command(request):
    if request.method == "POST":
        Command.objects.create(title=request.POST.get("title"))
        return redirect('view_commands')
    return render(request, 'users/add_command.html')


def delete_command(request, command_id):
    command = Command.objects.get(id=command_id)
    if request.method == "POST":
        for user_role in command.user_roles.all():
            user_role.delete()
        command.delete()
        return redirect('view_commands')
    return render(request, 'users/delete_command.html', context={'command': command})


def view_commands(request):
    commands = Command.objects.all()
    return render(request, 'users/view_commands.html', context={'commands': commands})


def view_command(request, command_id):
    command = Command.objects.get(id=command_id)
    roles = Role.objects.all()
    return render(request, 'users/view_command.html', context={'command': command, 'roles': roles})


def view_command_role(request, command_id, role_id):
    role = Role.objects.get(id=role_id)
    command = Command.objects.get(id=command_id)
    users_already_in_use = [user_role.user for user_role in UserRole.objects.all()]

    team_lead = command.user_roles.filter(role__name='Руководитель проекта')
    if team_lead.exists():
        team_lead = team_lead[0]
        team_lead_patterns = ResultPattern.objects.filter(result__user=team_lead.user,
                                                          prefer_team_member__isnull=False)
        prefer_team_member = [team_lead_pattern.prefer_team_member for team_lead_pattern in team_lead_patterns]
        results = Result.objects.filter(pattern__in=[*role.patterns.all(), *prefer_team_member])
    else:
        results = Result.objects.filter(pattern__in=role.patterns.all())

    context = {
        'command': command,
        'role': role,
        'results': results.exclude(user__in=users_already_in_use).order_by('user')
    }
    return render(request, 'users/command_create_role.html', context=context)


def create_command_role(request, command_id, role_id):
    command = Command.objects.get(id=command_id)

    users = [int(value[0]) for name, value in dict(request.POST).items() if name.startswith('user')]
    for user_id in users:
        user_role = UserRole.objects.create(user_id=user_id, role_id=role_id)
        command.user_roles.add(user_role)
    return redirect('view_command', command_id=command_id)


def delete_command_user_role(request, command_id, user_role_id):
    command = Command.objects.get(id=command_id)
    user_role = UserRole.objects.get(id=user_role_id)
    if request.method == "POST":
        user_role.delete()
        return redirect('view_command', command_id=command_id)
    return render(request, 'users/delete_command_user_role.html', context={'command': command, 'user_role': user_role})
