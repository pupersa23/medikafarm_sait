from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactDoctorForm
from .models import HomeBord, HomeDoctor, HomePriceCorp, HomeTopInfo

SAIT_INFO = HomeTopInfo.objects.all()


def index(request):
    template = 'home/home.html'
    info = SAIT_INFO
    board = HomeBord.objects.all()
    price = HomePriceCorp.objects.all()
    doctor = HomeDoctor.objects.all()
    if request.method == 'POST':
        form = ContactDoctorForm(request.POST or None)
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
            return redirect('home:index')

    form = ContactDoctorForm()
    context = {
        'info': info,
        'board': board,
        'price': price,
        'doctor': doctor,
        'form': form,
    }
    return render(request, template, context)


def konfiden(request):
    template = 'home/konfiden.html'
    info = SAIT_INFO
    context = {
        'info': info,
    }
    return render(request, template, context)
