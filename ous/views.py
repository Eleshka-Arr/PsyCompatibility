from django.shortcuts import render
from ous.models import Ous
# Create your views here.
def post(request, id):
    post = Ous.objects.get(pk=id)
    return render(request, 'ous/post.html', {'post': post})
