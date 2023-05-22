from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404, render

from home.models import HomeTopInfo
from sale.models import Sale

from .models import (Bassein, Bolnichnij, Gibdd, Gims, Gstayna, Gsy,
                     Spravka086_1, Spravka095_1, Travel)

SAIT_INFO = HomeTopInfo.objects.all()


@sync_to_async
def gibdd(request):
    template = 'spravki/gibdd.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:gibdd')
    price = Gibdd.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def gims(request):
    template = 'spravki/gims.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:gims')
    price = Gims.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def gsy(request):
    template = 'spravki/gsy.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:gsy')
    price = Gsy.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def gstayna(request):
    template = 'spravki/gstayna.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:gstayna')
    price = Gstayna.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def spravki_086(request):
    template = 'spravki/spravki_086.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:spravki_086')
    price = Spravka086_1.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
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


@sync_to_async
def student_095(request):
    template = 'spravki/student_095.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:student_095')
    price = Spravka095_1.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def spravki_sport(request):
    template = 'spravki/spravki_sport.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:spravki_sport')
    price = Bassein.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
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


@sync_to_async
def spravki_travel(request):
    template = 'spravki/spravki_travel.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:spravki_travel')
    price = Travel.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
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


@sync_to_async
def bolnichnij(request):
    template = 'spravki/bolnichnij.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='spravki:bolnichnij')
    price = Bolnichnij.objects.all()
    context = {
        'info': info,
        'price': price,
        'sale_info': sale_info,
    }
    return render(request, template, context)
