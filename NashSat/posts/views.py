from django.shortcuts import render
from .models import Posts
# from django.http import HttpResponse


# Create your views here.
def index(request, page=1):
    # return HttpResponse('Hello from Posts')
    posts = Posts.objects.all()
    posts = posts[::-1]
    posts = posts[(page-1)*10:page*10]
    context = {
        'title': 'Latest Posts',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def page(request, page=1):

    posts = Posts.objects.all()
    posts = posts[::-1]
    posts = posts[(page-1)*10:page*10]
    context = {
        'title': 'Latest Posts',
        'posts': posts,
    }

    return render(request, 'posts/page.html', context)
