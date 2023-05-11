from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from home.models import HomeTopInfo

from .models import Predvaritelnie
from .forms import ContactCompanyForm

SAIT_INFO = HomeTopInfo.objects.all()


def predvaritelnie(request):
    template = 'profi/predvaritelnie.html'
    info = SAIT_INFO
    price_men = Predvaritelnie.objects.get(pk=1)
    price_woman = Predvaritelnie.objects.get(pk=2)
    price_company = Predvaritelnie.objects.get(pk=3)
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
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
                messages.success(request, 'Сообщение отправлено')
            except Exception:
                messages.error(request, 'Сообщение не отправлено')
            return redirect('profi:predvaritelnie')

    form = ContactCompanyForm()
    context = {
        'info': info,
        'form': form,
        'price_men': price_men,
        'price_woman': price_woman,
        'price_company': price_company,
    }
    return render(request, template, context)
