from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, PasswordInput, TextInput, ModelForm

from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)

        widgets = {
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Hasło'
            }),

            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Powtórz hasło'
            }),
            'email': TextInput(attrs={'placeholder': "Email"}),

        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)

    widgets = {

        'email': TextInput(attrs={'placeholder': 'Email'}),
        'password': PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Hasło'
        })

    }

class UserLogInForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

        widgets = {

            'email': TextInput(attrs={'placeholder': 'email'}),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Hasło'
            })

        }


