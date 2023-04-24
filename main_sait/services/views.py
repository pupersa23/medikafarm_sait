from django.shortcuts import render


from .models import UltraSound
from home.models import HomeTopInfo


def ultrasound(request):
    template = 'services/ultrasound.html'
    info = HomeTopInfo.objects.all()
    price = UltraSound.objects.all()
    context = {
        'info': info,
        'price': price,
    }
    return render(request, template, context)
