from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('password')
        pwd2 = cleaned_data.get('password2')
        if pwd and pwd2 and pwd != pwd2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
