from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from quiz.models import Result

from news.models import Articles


def index(request):
    return render(request, 'MainApp/homePage.html')


def registration(request):
    return render(request, 'MainApp/registration.html')


def info(request):
    return render(request, 'MainApp/info.html')


def profile(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'MainApp/profile.html', context={'results': results})


def log(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    print(request.POST)
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    print(username, password)
    if username is None or password is None:
        return render(request, 'MainApp/login.html', locals())
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')


def reg_view(request):
    if not User.objects.filter(username=request.POST['login']).exists():
        username = request.POST['login']
        lastname = request.POST['last_name']
        firstname = request.POST['first_name']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password, last_name=lastname, first_name=firstname)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'MainApp/homePage.html')


def add_obzor(request):
    return render(request, 'MainApp/add_obzor.html')


def aobzor(request):
    if request.method == "POST":
        obzor = Obzor()
        obzor.title = request.POST.get("title")
        obzor.text = request.POST.get("text")
        obzor.checked = request.POST.get("checked")
        obzor.age_limit = request.POST.get("age_limit")
        obzor.date = timezone.now()
        obzor.save()
    return HttpResponseRedirect('/')


def add_article(request):
    return render(request, 'MainApp/add_article.html')


def addarticle(request):
    if request.method == "POST":
        article = Articles()
        article.title = request.POST.get("title")
        article.post = request.POST.get("text")
        article.adminchecked = request.POST.get("adminchecked")
        article.gender = request.POST.get("gender")
        article.date = timezone.now()
        article.save()
    return HttpResponseRedirect('/')


def exit(request):
    logout(request)
    return HttpResponseRedirect('/')


def del_article(request, id):
    try:
        article = Articles.objects.get(id=id)
        article.delete()
        return HttpResponseRedirect("/")
    except Articles.DoesNotExist:
        return HttpResponseNotFound("<h2>Article not found</h2>")
