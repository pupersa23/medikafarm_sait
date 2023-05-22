from asgiref.sync import sync_to_async
from django.shortcuts import render

from home.models import HomeTopInfo

from .models import Sale

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
