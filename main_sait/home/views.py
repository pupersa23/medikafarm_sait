from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .models import HomeTopInfo, HomeBord, HomePriceCorp, HomeDoctor
from .forms import ContactDoctorForm


def index(request):
    template = 'home/home.html'
    info = HomeTopInfo.objects.all()
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
                          'ryazanov745@gmail.com',
                          ['ryazanov745@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return HttpResponse()

    form = ContactDoctorForm()
    context = {
        'info': info,
        'board': board,
        'price': price,
        'doctor': doctor,
        'form': form,
    }
    return render(request, template, context)
