from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, PasswordInput, TextInput

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

    # def clean(self):
    #     cleaned_data = super(CustomUserCreationForm, self).clean()
    #     password1 = cleaned_data.get("password")
    #     password2 = cleaned_data.get("confirm_password")
    #
    #     if password1 != password2:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)




