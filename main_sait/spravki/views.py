from django.shortcuts import render

from home.models import HomeTopInfo

from .models import (Bassein, Gibdd, Gims, Gstayna, Gsy, Spravka086_1,
                     Spravka095_1)

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


def spravki_086(request):
    template = 'spravki/spravki_086.html'
    info = SAIT_INFO
    price = Spravka086_1.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def student_095(request):
    template = 'spravki/student_095.html'
    info = SAIT_INFO
    price = Spravka095_1.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def bassein(request):
    template = 'spravki/bassein.html'
    info = SAIT_INFO
    price = Bassein.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)
