from django.shortcuts import render
from news.models import Articles

def post(request, id):
    post = Articles.objects.get(pk=id)
    return render(request, 'news/post.html', {'post': post})

def del_article(request, id):
    try:
        article = Articles.objects.get(id=id)
        article.delete()
        return HttpResponseRedirect("/")
    except Articles.DoesNotExist:
        return HttpResponseNotFound("<h2>Article not found</h2>")
