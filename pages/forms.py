from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from pages.models import Student


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=50, help_text='required', )
    email = forms.EmailField(max_length=300, help_text='activation code will be sent to this email.enter a valid email')
    first_name = forms.CharField(max_length=50, help_text='required')
    error_messages = {
        'password_mismatch': _("گذرواژه و تکرار گذرواژه یکسان نیستند"),
        'username_exists' : _('یوزرت تکراریه کاکو')
    }

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')

    # def is_valid(self):
    #     if User.objects.filter(username=self.cleaned_data['username']).exists():
    #         raise forms.ValidationError(_("نام کاربری شما در سیستم موجود است"))
    #     if not super().is_valid():
    #         return False




class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50)