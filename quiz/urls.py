from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz'),
    path('stress', views.stress, name='stress'),
    path('profession', views.profession, name='profession'),
    path('<int:quiz_id>', views.view_quiz, name='view_quiz'),
    path('submit-quiz/<int:quiz_id>', views.submit_quiz, name='submit_quiz')
]