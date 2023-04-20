from django.shortcuts import render

from .models import HomeTopInfo


def index(request):
    template = 'home/home.html'
    info = HomeTopInfo.objects.all()
    context = {
        'info': info,
    }
    return render(request, template, context)
