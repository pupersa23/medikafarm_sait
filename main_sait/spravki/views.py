from django.shortcuts import get_object_or_404, render

from home.models import HomeTopInfo

from .models import (Bassein, Gibdd, Gims, Gstayna, Gsy, Spravka086_1,
                     Spravka095_1, Travel, Bolnichnij)

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


def spravki_086_datail(request, choice):
    if choice == 'na-dolzhnost-sudi':
        template = 'spravki/086y/sudija.html'
        info = SAIT_INFO
        price = get_object_or_404(Spravka086_1, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'dlya-raboty':
        template = 'spravki/086y/naraboty.html'
        info = SAIT_INFO
        price = get_object_or_404(Spravka086_1, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'dlya-postupleniya':
        template = 'spravki/086y/student.html'
        info = SAIT_INFO
        price = get_object_or_404(Spravka086_1, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'dlya-meditsinskikh-napravleniy':
        template = 'spravki/086y/meditsina.html'
        info = SAIT_INFO
        price = get_object_or_404(Spravka086_1, choice=choice)
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


def spravki_sport(request):
    template = 'spravki/spravki_sport.html'
    info = SAIT_INFO
    price = Bassein.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def spravki_sport_datail(request, choice):
    if choice == 'bassein':
        template = 'spravki/sport/bassein.html'
        info = SAIT_INFO
        price = get_object_or_404(Bassein, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'sport':
        template = 'spravki/sport/sport.html'
        info = SAIT_INFO
        price = get_object_or_404(Bassein, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'sapliv':
        template = 'spravki/sport/sapliv.html'
        info = SAIT_INFO
        price = get_object_or_404(Bassein, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'sabeg':
        template = 'spravki/sport/sabeg.html'
        info = SAIT_INFO
        price = get_object_or_404(Bassein, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)


def spravki_travel(request):
    template = 'spravki/spravki_travel.html'
    info = SAIT_INFO
    price = Travel.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)


def spravki_travel_datail(request, choice):
    if choice == 'sankarta':
        template = 'spravki/travel/sankarta.html'
        info = SAIT_INFO
        price = get_object_or_404(Travel, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'sanatoriy':
        template = 'spravki/travel/putevka.html'
        info = SAIT_INFO
        price = get_object_or_404(Travel, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)
    elif choice == 'sagranica':
        template = 'spravki/travel/sagranica.html'
        info = SAIT_INFO
        price = get_object_or_404(Travel, choice=choice)
        context = {
            'info': info,
            'price': price,
        }
        return render(request, template, context)


def bolnichnij(request):
    template = 'spravki/bolnichnij.html'
    info = SAIT_INFO
    price = Bolnichnij.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)
