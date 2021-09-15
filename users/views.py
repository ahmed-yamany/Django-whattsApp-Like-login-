from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistraitionForm, CodeForm
from .models import FamTamUser
from .utils import send_sms


@login_required(login_url='user_register')
def home(request):
    return render(request, 'base.html', {})


def register_or_login(request):
    context = {}
    try:
        phone_number = request.POST['phone_number']
    except:
        phone_number = '00000000000'
    if request.method == 'POST':
        form = RegistraitionForm(request.POST)

        if form.is_valid():
            form.save()
            phone_number = request.POST['phone_number']
            request.session['phone_number'] = phone_number
            messages.success(request, f'Account created for {phone_number}!')
            return redirect('verify_code')
        elif FamTamUser.objects.filter(phone_number=phone_number).exists():
            user = FamTamUser.objects.get(phone_number=phone_number)
            code = user.code
            # messages.info(request, 'You have an account')
            code.save()  # change user code when login

            request.session['phone_number'] = user.phone_number
            return redirect('verify_code')

            # send code message
        else:
            context['form'] = form
            # return redirect('user_register')




    else:
        form = RegistraitionForm()
        context['form'] = form

    context = {
        'form': form,
    }
    return render(request, 'users/register_or_login.html', context)


def verify_code(request):
    context = {}
    form = CodeForm(request.POST)
    phone_number = request.session.get('phone_number')
    if phone_number:
        user = FamTamUser.objects.get(phone_number=phone_number)
        code = user.code
        code_user = f'Hi you code \n {code}'

        if not request.POST:
            # send sms
            send_sms(code_user, f'2{user.phone_number}')

        if form.is_valid():
            sms = form.cleaned_data['code']
            print(str(code))
            if str(code) == str(sms):
                code.save()
                login(request, user)
                return redirect('home')

    return render(request, 'users/verify_code.html', context)


def log_out(request):
    logout(request)
    return redirect('home')
