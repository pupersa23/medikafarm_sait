from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from knigki.models import Knigki
from posts.models import Post
from profi.models import Pereodik, Predsmena, Predvaritelnie, Psixushka
from sale.models import Sale
from services.models import Analisi, Fluromobil, Rentgen, UltraSound
from spravki.models import (Bassein, Bolnichnij, Gibdd, Gims, Gstayna, Gsy,
                            Spravka086_1, Spravka095_1, Travel)

from .forms import ContactDoctorForm
from .models import HomeBord, HomeDoctor, HomePriceCorp, HomeTopInfo, HomeDocuments

SAIT_INFO = HomeTopInfo.objects.all()


def index(request):
    template = 'home/home.html'
    info = SAIT_INFO
    posts = Post.objects.filter().order_by('-pub_date')[:4]
    board = HomeBord.objects.all()
    price = HomePriceCorp.objects.all()
    doctor = HomeDoctor.objects.all()
    sale = Sale.objects.all()
    if request.method == 'POST':
        form = ContactDoctorForm(request.POST or None)
        if form.is_valid():
            subject = "Заявка с главное страницы"
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
        'sale': sale,
        'posts': posts,
    }
    return render(request, template, context)


def konfiden(request):
    template = 'home/konfiden.html'
    info = SAIT_INFO
    context = {
        'info': info,
    }
    return render(request, template, context)


def documents(request):
    template = 'home/documents.html'
    info = SAIT_INFO
    documents = HomeDocuments.objects.all()
    context = {
        'info': info,
        'documents': documents,
    }
    return render(request, template, context)


def contact(request):
    template = 'home/contact.html'
    info = SAIT_INFO
    context = {
        'info': info,
    }
    return render(request, template, context)


def price(request):
    template = 'home/price.html'
    info = SAIT_INFO
    price_uzi = UltraSound.objects.all()
    price_rentgen = Rentgen.objects.all()
    price_fluromobil = Fluromobil.objects.all()
    price_analisi = Analisi.objects.all()
    price_predvar = Predvaritelnie.objects.all()
    price_periodic = Pereodik.objects.all()
    price_psix = Psixushka.objects.all()
    price_predreis = Predsmena.objects.all()
    price_gibdd = Gibdd.objects.all()
    price_gims = Gims.objects.all()
    price_gstayna = Gstayna.objects.all()
    price_gsy = Gsy.objects.all()
    price_086 = Spravka086_1.objects.all()
    price_095 = Spravka095_1.objects.all()
    price_sport = Bassein.objects.all()
    price_travel = Travel.objects.all()
    price_bolnic = Bolnichnij.objects.all()
    price_knig_all = Knigki.objects.filter(choice='all')
    price_kni_med = Knigki.objects.filter(choice='medik')
    context = {
        'info': info,
        'price_uzi': price_uzi,
        'price_rentgen': price_rentgen,
        'price_fluromobil': price_fluromobil,
        'price_analisi': price_analisi,
        'price_predvar': price_predvar,
        'price_periodic': price_periodic,
        'price_psix': price_psix,
        'price_predreis': price_predreis,
        'price_gibdd': price_gibdd,
        'price_gims': price_gims,
        'price_gstayna': price_gstayna,
        'price_gsy': price_gsy,
        'price_086': price_086,
        'price_095': price_095,
        'price_sport': price_sport,
        'price_travel': price_travel,
        'price_bolnic': price_bolnic,
        'price_knig_all': price_knig_all,
        'price_kni_med': price_kni_med,
    }
    return render(request, template, context)
