from django.urls import path

from pages.views import homepage, signup_page, login_page, contact_page, user_page, logout_page

urlpatterns = [
    path('', homepage, name='home'),
    path('register/', signup_page, name='register'),
    path('login/', login_page, name='login'),
    path('contact_us/', contact_page, name='contact_us'),
    path('profile/', user_page, name='profile'),
    path('logout/', logout_page, name='logout')
]
