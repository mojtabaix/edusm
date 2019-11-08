from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from pages.decorators import superuser_required
from pages.forms import SignUpForm, new_course_form
from pages.models import Course


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
        if first_name != "":
             # print("in if")
             request.user.first_name = first_name
             # print(first_name)
             request.user.save()
             request.user.refresh_from_db()
             # print("user is saved")
        if last_name != "":
             request.user.last_name = last_name
             request.user.save()
             request.user.refresh_from_db()
        return redirect('profile')
    return render(request, 'setting.html')


def panel_page(request):
    return render(request, 'panel.html', {'is_admin': True})

# @user_passes_test(lambda u: u.is_superuser)

def new_course(request):
     if request.POST:
         form = new_course_form(request.POST, request.FILES)
         if form.is_valid():
             user = form.save()
             user.save()
             user.refresh_from_db()
             if request.POST.get('first_day') == '0':
                user.first_day = Course.Saturday
             if request.POST.get('first_day') == '1':
                user.first_day = Course.Sunday
             if request.POST.get('first_day') == '2':
                 user.first_day = Course.Monday
             if request.POST.get('first_day') == '3':
                 user.first_day = Course.Tuesday
             if request.POST.get('first_day') == '4':
                 user.first_day = Course.Wensday
             if request.POST.get('second_day') == '0':
                 user.second_day = Course.Saturday
             if request.POST.get('second_day') == '1':
                 user.second_day = Course.Sunday
             if request.POST.get('second_day') == '2':
                 user.second_day = Course.Monday
             if request.POST.get('second_day') == '3':
                 user.second_day = Course.Tuesday
             if request.POST.get('second_day') == '4':
                 user.second_day = Course.Wensday
             user.save()
             user.refresh_from_db()

         else:
             print(form.errors)
     return render(request, 'make_new_course.html')


def all_courses(request):
    courses = Course.objects.all()
    if request.POST:
        search = request.POST.get('search_query')
        courses = Course.objects.all().filter(department=search)
        return render(request, 'courses.html', {'search_results': courses})
    # print(courses)
    return render(request, 'courses.html', {'courses': courses})
