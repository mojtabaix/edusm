from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from pages.forms import SignUpForm, LoginForm


def homepage(request):
    return render(request, 'base1.html')
def signuppage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.student.last_name = form.cleaned_data['last_name']
            user.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'register-form.html')

def loginpage(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse('login page')
    else:
        form = LoginForm()
    return render(request, 'signup.html', {'form': form})