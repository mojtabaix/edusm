from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            if pass1 and pass2 and pass1 != pass2:
                error = form.error_messages['password_mismatch']
            else:
                error = form.error_messages['user_exists']

    return render(request, 'register-form.html', {error})


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
        email = EmailMessage(title, content, to=[email])
        email.send()
        # render(request, 'contact-us.html', {title, email, content})
        return redirect('home')
    return render(request, 'contact-us.html')


@login_required(login_url='login')
def user_page(request):
    return HttpResponse("user is logged in")
