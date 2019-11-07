from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
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
            user.student.first_name = form.cleaned_data['first_name']
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
        # print(request.POST)
        form = LoginForm(request.POST)
        print(form)
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
        form = LoginForm()
    return render(request, 'login_form.html', {'form': form})
def contactPage(request):
    if request.POST:
        title = request.POST.get('title')
        email = request.POST.get('email')
        content = request.POST.get('text')
        render(request, 'contact-us.html', {title,email,content})
        return redirect('home')
    return render(request, 'contact-us.html')

