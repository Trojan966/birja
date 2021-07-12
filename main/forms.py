from django import forms
from django.contrib.auth import get_user_model
from django.forms import CharField, TextInput

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    username = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean_username(self):
        username = self.cleaned_data['username']

        return username

    class Meta:
        model = User
        fields = ['username', 'password']