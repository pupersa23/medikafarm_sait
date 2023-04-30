from django.shortcuts import render

from .models import Gibdd, Gims, Gsy, Gstayna
from home.models import HomeTopInfo


SAIT_INFO = HomeTopInfo.objects.all()


def gibdd(request):
    template = 'spravki/gibdd.html'
    info = SAIT_INFO
    price = Gibdd.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def gims(request):
    template = 'spravki/gims.html'
    info = SAIT_INFO
    price = Gims.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def gsy(request):
    template = 'spravki/gsy.html'
    info = SAIT_INFO
    price = Gsy.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def gstayna(request):
    template = 'spravki/gstayna.html'
    info = SAIT_INFO
    price = Gstayna.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)
