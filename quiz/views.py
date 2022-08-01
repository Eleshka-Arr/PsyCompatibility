from django.shortcuts import render

from quiz.models import Quiz, Question, Result, ResultPattern, QuizType
from quiz.utils import get_score_result_pattern, get_choices_result_pattern, get_temperament_result_pattern


def quiz_home(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz/quiz.html', context={'quizes': quizes})


def view_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz_id=quiz_id)
    return render(request, 'quiz/view_quiz.html', context={'quiz': quiz, 'questions': questions})


def submit_quiz(request, quiz_id):
    variants = [int(variant[0]) for question, variant in dict(request.POST).items() if question.isdigit()]

    quiz = Quiz.objects.get(id=quiz_id)
    if quiz.type == QuizType.SCORE:
        score, result_pattern = get_score_result_pattern(variants)
        result, _ = Result.objects.update_or_create(user=request.user, quiz_id=quiz_id,
                                                    defaults={'pattern': result_pattern, 'score': score})
    elif quiz.type == QuizType.TEMPERAMENT:
        result_pattern = get_temperament_result_pattern(variants)
        result, _ = Result.objects.update_or_create(user=request.user, quiz_id=quiz_id,
                                                    defaults={'pattern': result_pattern})
    else:
        result_pattern = get_choices_result_pattern(variants)
        result, _ = Result.objects.update_or_create(user=request.user, quiz_id=quiz_id,
                                                    defaults={'pattern': result_pattern})
    return render(request, 'quiz/quiz_result.html', context={'result': result})
