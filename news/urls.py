from django.urls import path, include
from django.views.generic import ListView, DetailView
from news.models import Articles
from . import views


urlpatterns = [
    path('',
    ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    template_name="news/articles.html")),
    path(r'<int:pk>', DetailView.as_view(model=Articles, template_name="news/article.html")),
path('<int:pk>/del_article/',views.del_article),

]
