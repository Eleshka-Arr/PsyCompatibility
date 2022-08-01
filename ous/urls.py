from django.urls import path, include
from django.views.generic import ListView, DetailView
from ous.models import Ous
from . import views

urlpatterns = [
    path('',
    ListView.as_view(queryset=Ous.objects.all().order_by("post")[:5],
    template_name="ous/posts.html")),
    path(r'<int:pk>', DetailView.as_view(model=Ous, template_name="ous/posts.html")),
]
