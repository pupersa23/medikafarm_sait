from django.shortcuts import render
from asgiref.sync import sync_to_async

from .models import Sale
from home.models import HomeTopInfo


SAIT_INFO = HomeTopInfo.objects.all()


@sync_to_async
def sale(request):
    template = 'sale/sale.html'
    info = SAIT_INFO
    sale = Sale.objects.all()
    context = {
        'info': info,
        'sale': sale,
    }
    return render(request, template, context)
