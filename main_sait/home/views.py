from django.shortcuts import render

from .models import HomeTopInfo, HomeBord, HomePriceCorp, HomeDoctor


def index(request):
    template = 'home/home.html'
    info = HomeTopInfo.objects.all()
    board = HomeBord.objects.all()
    price = HomePriceCorp.objects.all()
    doctor = HomeDoctor.objects.all()
    context = {
        'info': info,
        'board': board,
        'price': price,
        'doctor': doctor,
    }
    return render(request, template, context)
