from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404, render

from home.models import HomeTopInfo

from .models import Post
from .utils import paginator

SAIT_INFO = HomeTopInfo.objects.all()


@sync_to_async
def posts_all(request):
    template = 'posts/posts_all.html'
    info = SAIT_INFO
    posts_all = Post.objects.all()
    page_obj = paginator(request, posts_all)
    context = {
        'info': info,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@sync_to_async
def post_detail(request, post_id):
    template = 'posts/posts_detail.html'
    info = SAIT_INFO
    posts = Post.objects.all()
    posts_detail = get_object_or_404(Post, pk=post_id)
    context = {
        'info': info,
        'posts': posts,
        'posts_detail': posts_detail,
    }
    return render(request, template, context)
