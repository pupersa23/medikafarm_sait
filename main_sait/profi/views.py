from asgiref.sync import sync_to_async
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from home.models import HomeTopInfo
from sale.models import Sale

from .forms import ContactCompanyForm
from .models import Pereodik, Predsmena, Predvaritelnie, Psixushka

SAIT_INFO = HomeTopInfo.objects.all()


def send_email(subject, redir, form, request):
    subject = subject
    body = {
        'first_name': form.cleaned_data['first_name'],
        'email_address': form.cleaned_data['email_address'],
        'phone_number': form.cleaned_data['phone_number'],
        'title': form.cleaned_data['title'],
        'message': form.cleaned_data['message'],
    }
    message = "\n".join(body.values())
    try:
        send_mail(
            subject, message,
            body['email_address'],
            ['ryazanov745@gmail.com']
        )
        messages.success(request, 'Сообщение отправлено')
    except Exception:
        messages.error(request, 'Сообщение не отправлено')
    return redirect(redir)


@sync_to_async
def predvaritelnie(request):
    template = 'profi/predvaritelnie.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='profi:predvaritelnie')
    price_men = Predvaritelnie.objects.get(choice='men')
    price_woman = Predvaritelnie.objects.get(choice='woman')
    price_company = Predvaritelnie.objects.get(choice='corporat')
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
        if form.is_valid():
            subject = "Заявка с страницы предварительные профосмотры"
            redir = 'profi:predvaritelnie'
            email = send_email(subject, redir, form, request)
            return email

    form = ContactCompanyForm()
    context = {
        'info': info,
        'form': form,
        'price_men': price_men,
        'price_woman': price_woman,
        'price_company': price_company,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def pereodicheskiy(request):
    template = 'profi/pereodicheskiy.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='profi:pereodicheskiy')
    price_men = Pereodik.objects.get(choice='men')
    price_woman = Pereodik.objects.get(choice='woman')
    price_viesd = Pereodik.objects.get(choice='corporat')
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
        if form.is_valid():
            subject = "Заявка с страницы периодические профосмотры"
            redir = 'profi:pereodicheskiy'
            email = send_email(subject, redir, form, request)
            return email

    form = ContactCompanyForm()
    context = {
        'info': info,
        'form': form,
        'price_men': price_men,
        'price_woman': price_woman,
        'price_viesd': price_viesd,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def vneocherednoy(request):
    template = 'profi/vneocherednoy.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='profi:vneocherednoy')
    price_men = Pereodik.objects.get(choice='men')
    price_woman = Pereodik.objects.get(choice='woman')
    price_viesd = Pereodik.objects.get(choice='corporat')
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
        if form.is_valid():
            subject = "Заявка с страницы внеочередные профосмотры"
            redir = 'profi:vneocherednoy'
            email = send_email(subject, redir, form, request)
            return email

    form = ContactCompanyForm()
    context = {
        'info': info,
        'form': form,
        'price_men': price_men,
        'price_woman': price_woman,
        'price_viesd': price_viesd,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def psihiatricheskoe(request):
    template = 'profi/psihiatricheskoe.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='profi:psihiatricheskoe')
    price_uliza = Psixushka.objects.get(choice='all')
    price_company = Psixushka.objects.get(choice='corporat')
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
        if form.is_valid():
            subject = "Заявка с страницы психиатрическое освидетельстваоание"
            redir = 'profi:psihiatricheskoe'
            email = send_email(subject, redir, form, request)
            return email

    form = ContactCompanyForm()
    context = {
        'info': info,
        'form': form,
        'price_uliza': price_uliza,
        'price_company': price_company,
        'sale_info': sale_info,
    }
    return render(request, template, context)


@sync_to_async
def predsmenniy(request):
    template = 'profi/predsmenniy.html'
    info = SAIT_INFO
    sale_info = Sale.objects.filter(choice='profi:predsmenniy')
    price_uliza = Predsmena.objects.get(choice='all')
    price_company = Predsmena.objects.get(choice='corporat')
    if request.method == 'POST':
        form = ContactCompanyForm(request.POST or None,
                                  request.FILES or None)
        if form.is_valid():
            subject = "Заявка с страницы предрейсовые профосмотры"
            redir = 'profi:predsmenniy'
            email = send_email(subject, redir, form, request)
            return email

    form = ContactCompanyForm()
    context = {
        'info': info,
        'form': form,
        'price_uliza': price_uliza,
        'price_company': price_company,
        'sale_info': sale_info,
    }
    return render(request, template, context)
