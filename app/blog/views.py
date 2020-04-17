from django.shortcuts import render
from blog.models.posts import Post


def home(request):
    context = {
        'posts': Post.objects.filter(is_deleted=False)
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
