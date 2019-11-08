from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from pages.forms import SignUpForm


def homepage(request):
    # for user in User.objects.filter(is_active=True):
    #     logout(request)
    return render(request, 'base1.html')


def signup_page(request):
    error = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.student.last_name = form.cleaned_data['last_name']
            user.student.first_name = form.cleaned_data['first_name']
            user.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1 and pass2 and pass1 != pass2:
                error = form.error_messages['password_mismatch']
            else:
                error = 'نام کاربری شما در سیستم موجود است'


    return render(request, 'register-form.html', {'error': error})


def login_page(request):
    if request.POST:
        # print(request.POST)
        form = AuthenticationForm(data=request.POST)
        # print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_form.html', {'error': 'login form isnt valid'})
    else:
        # print("request not post")
        form = AuthenticationForm()
    return render(request, 'login_form.html', {'form': form})


def contact_page(request):
    if request.POST:
        title = request.POST.get('title')
        email = request.POST.get('email')
        content = request.POST.get('text')
        if len(content) < 10 or len(content)>250 :
            return render(request, 'contact-us.html', {'error': 'form isnt valid'})
        if email is None or title is None:
            return render(request, 'contact-us.html', {'error': 'form isnt valid'})
        email = EmailMessage(title, email + "  "+content, to=['webe19lopers@gmail.com'])
        email.send()


        return redirect('sent_email')
    return render(request, 'contact-us.html')


def sent_email(request):
    return render(request, 'files/emailSent.html')


@login_required(login_url='login')
def user_page(request):
    return render(request, 'user-profile.html', {'first_name': request.user.first_name, 'user_name': request.user.username, 'last_name': request.user.last_name})


def logout_page(request):
    for user in User.objects.filter(is_active=True):
        logout(request)
    return redirect('home')


def setting_page(request):
    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if first_name:
             request.user.last_name = last_name
        if last_name:
             request.user.first_name = first_name
        redirect('profile')
    return render(request, 'setting.html')


def panel_page(request):
    return render(request, 'panel.html')


def new_course(request):
    if request.POST:
       department=request.POST.get("depratment")
    return render(request, 'make_new_course.html')
