from django.urls import path

from pages.views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', signup_page, name='register'),
    path('login/', login_page, name='login'),
    path('contact_us/', contact_page, name='contact_us'),
    path('sentEmail/', sent_email, name='sent_email'),
    path('profile/', user_page, name='profile'),
    path('logout/', logout_page, name='logout'),
    path('settings/', setting_page, name='settings'),
    path('panel/', panel_page, name='panel'),
    path('new_coourse/', new_course, name='new_course')
]
