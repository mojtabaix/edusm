from django.urls import path

from pages.views import homepage, signuppage, loginpage

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', signuppage, name='register'),
    path('login/', loginpage, name='login'),
]