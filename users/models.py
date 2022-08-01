from django.db import models
from quiz.models import ResultPattern
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название роли')
    patterns = models.ManyToManyField(ResultPattern, verbose_name='Паттерны', blank=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Роль')

    def __str__(self):
        return f'{self.user.username}:{self.role.name}'


class Command(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название команды')
    user_roles = models.ManyToManyField(UserRole, verbose_name='Роли пользователей', blank=True)

    def __str__(self):
        return self.title
