from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from home.models import HomeTopInfo

from .forms import ArendaFlgForm
from .models import Analisi, Fluromobil, Rentgen, UltraSound

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
    description = Fluromobil.objects.get(pk=1)
    if request.method == 'POST':
        form = ArendaFlgForm(request.POST or None)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'email_address': form.cleaned_data['email_address'],
                'phone_number': form.cleaned_data['phone_number'],
                'title': form.cleaned_data['title'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          body['email_address'],
                          ['ryazanov745@gmail.com'])
                messages.success(request, 'Заявка отправлено')
            except Exception:
                messages.error(request, 'Заявка не отправлено')
            return redirect('services:fluromobil')
    form = ArendaFlgForm()
    context = {
        'info': info,
        'price': price,
        'description': description,
        'form': form,
    }
    return render(request, template, context)
