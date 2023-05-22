from asgiref.sync import sync_to_async
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from home.models import HomeTopInfo
from sale.models import Sale

from .forms import ContactCompanyForm
from .models import Knigki

SAIT_INFO = HomeTopInfo.objects.all()


@sync_to_async
def medknizhki(request):
    template = 'knigki/knigki.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='knigki:medknizhki')
    price_all = Knigki.objects.filter(choice='all')
    price_med = Knigki.objects.filter(choice='medik')
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
        if form.is_valid():
            subject = "Заявка с страницы медицинские книжки"
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
        'price_all': price_all,
        'price_med': price_med,
        'sale_info': sale_info,
    }
    return render(request, template, context)
