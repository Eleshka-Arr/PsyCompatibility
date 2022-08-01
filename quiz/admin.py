from django.contrib import admin

from .models import Quiz, Question, QuestionVariant, Result, ResultPattern

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionVariant)
admin.site.register(Result)
admin.site.register(ResultPattern)
