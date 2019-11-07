from django.urls import path

from pages.views import homepage, signuppage, loginpage, contactPage

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', signuppage, name='register'),
    path('login/', loginpage, name='login'),
    path('contact_us/', contactPage, name='contact_us')
]