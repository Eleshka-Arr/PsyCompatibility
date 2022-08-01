from django.db.models import Sum

from quiz.models import QuestionVariant, ResultPattern, ScaleType


def get_score_result_pattern(variants: list):
    score = sum(QuestionVariant.objects.get(id=variant).score or 0 for variant in variants)
    result_pattern = ResultPattern.objects.filter(
        variants__in=variants, max_score__gte=score, min_score__lte=score).distinct()
    return score, result_pattern[0] if result_pattern.exists() else None


def get_choices_result_pattern(variants: list):
    result_pattern = ResultPattern.objects.filter(variants__in=variants)
    return result_pattern[0] if result_pattern.exists() else None


def get_temperament_result_pattern(variants: list):
    stability_score = QuestionVariant.objects.filter(id__in=variants, scale=ScaleType.STABILITY).aggregate(
        score=Sum('score'))['score'] or 0
    opened_score = QuestionVariant.objects.filter(id__in=variants, scale=ScaleType.OPENED).aggregate(
        score=Sum('score'))['score'] or 0

    result_pattern = ResultPattern.objects.filter(
        stability_score_from__lte=stability_score,
        stability_score_to__gte=stability_score,
        opened_score_from__lte=opened_score,
        opened_score_to__gte=opened_score,
    )
    return result_pattern[0] if result_pattern.exists() else None
