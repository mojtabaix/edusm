from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pages.forms import SignUpForm


def homepage(request):
    return render(request, 'home.html')
def signuppage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.student2.last_name = form.cleaned_data.get('last_name')
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return HttpResponse("loged in")


    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

    return HttpResponse('signup page')
def loginpage(request):
    return HttpResponse('login page')