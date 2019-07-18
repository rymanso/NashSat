from django.shortcuts import render
from .models import Posts
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Posts')

    posts = Posts.objects.all()
    posts = posts[::-1]
    posts = posts[0:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)
