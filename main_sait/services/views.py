from django.shortcuts import render


from .models import UltraSound, Rentgen, Analisi, Fluromobil
from home.models import HomeTopInfo


SAIT_INFO = HomeTopInfo.objects.all()


def ultrasound(request):
    template = 'services/ultrasound.html'
    info = SAIT_INFO
    price = UltraSound.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def rentgen(request):
    template = 'services/rentgen.html'
    info = SAIT_INFO
    price = Rentgen.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def analisi(request):
    template = 'services/analisi.html'
    info = SAIT_INFO
    file = Analisi.objects.all()
    context = {
        'info': info,
        'file': file,
    }
    return render(request, template, context)


def fluromobil(request):
    template = 'services/fluromobil.html'
    info = SAIT_INFO
    price = Fluromobil.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)
