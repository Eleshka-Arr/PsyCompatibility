from django.db import models
from django.contrib.auth.models import User


class QuizType:
    SCORE = 1
    CHOICES = 2
    TEMPERAMENT = 3


class ScaleType:
    STABILITY = 1
    OPENED = 2


class Quiz(models.Model):
    TYPES = (
        (QuizType.SCORE, 'Score'),
        (QuizType.CHOICES, 'Choices'),
        (QuizType.TEMPERAMENT, 'Temperament')
    )
    title = models.CharField('Название теста', max_length=120, null=True)
    type = models.IntegerField(choices=TYPES, verbose_name='Тип теста', default=QuizType.CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class QuestionVariant(models.Model):
    TYPES = (
        (ScaleType.STABILITY, 'Стабильность'),
        (ScaleType.OPENED, 'Открытость')
    )
    content = models.TextField(verbose_name='Текст варианта вопроса')
    score = models.FloatField(verbose_name='Балл', null=True, blank=True)
    scale = models.IntegerField(verbose_name='Cтабильность - Открытость', null=True, blank=True, choices=TYPES)

    def __str__(self):
        return self.content


class Question(models.Model):
    title = models.CharField('Вопрос', max_length=254)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест', blank=True, null=True)
    variants = models.ManyToManyField(QuestionVariant, verbose_name='Варианты', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class ResultPattern(models.Model):
    description = models.CharField(max_length=250, verbose_name='Диагноз')
    variants = models.ManyToManyField(QuestionVariant, verbose_name='Варианты', blank=True)
    min_score = models.FloatField(verbose_name='Минимальный балл', null=True, blank=True)
    max_score = models.FloatField(verbose_name='Максимальный балл', null=True, blank=True)
    prefer_team_member = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name='Предпочитаемый тип участника команды')
    stability_score_from = models.FloatField(null=True, blank=True, verbose_name='Стабильность от')
    stability_score_to = models.FloatField(null=True, blank=True, verbose_name='Стабильность до')
    opened_score_from = models.FloatField(null=True, blank=True, verbose_name='Открытость от')
    opened_score_to = models.FloatField(null=True, blank=True, verbose_name='Открытость до')

    def __str__(self):
        return self.description


class Result(models.Model):
    pattern = models.ForeignKey(ResultPattern, on_delete=models.CASCADE, verbose_name='Паттерн', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест', blank=True, null=True)
    score = models.FloatField(verbose_name='Балл', null=True, blank=True)

    def __str__(self):
        if self.pattern is None:
            return 'Неизвестный диагноз'
        return self.pattern.description
