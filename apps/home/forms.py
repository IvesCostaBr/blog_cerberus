from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, 
    label="Username",
    widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    
    photo = forms.FileField(
        label="Photo",
        widget=forms.FileInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.EmailField(max_length=70,
    widget=forms.EmailInput(attrs={'class': 'form-control',
    'placeholder':'Digite seu melhor E-Mail.:'})
    )
    password1 = forms.CharField(max_length=30,
    label="Password",
    widget=forms.PasswordInput(
        attrs={'class': 'form-control',
        'placeholder':'Crie uma senha.:'}
    ))
    password2 = forms.CharField(max_length=30,
    label="",
    widget=forms.PasswordInput(
        attrs={'class': 'form-control',
        'placeholder':'Confirme sua senha.:'}
    ))



    def cleanPassword(self):
        if not self.password1 == self.password2:
            return forms.ValidationError('As senhas digitadas não conferem')
        return self.password1

    def cleanUserName(self):
        if User.objects.filter(username=self.username).exists():
            return forms.ValidationError('Username já em uso! Tente Outro.')
        return self.username

    def cleanEmail(self):
        if User.objects.filter(email=self.email).exists():
            return forms.ValidationError('Email já em uso!Tente outro.')
        return self.email
