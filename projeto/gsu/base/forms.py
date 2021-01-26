from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *
from django.forms import modelformset_factory
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class SugestaoForm(forms.ModelForm):
    titulo = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}), strip=False, empty_value='Sem contato')
    descricao = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Sugestao
        fields = ('titulo', 'email', 'descricao')


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'nome','cpf')
        widgets = {
             'password': forms.PasswordInput()
        }
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class UsuarioChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label= ("Senha"),
    help_text= ("<a href=\"../password/\">Clique aqui para alterar a senha</a>."))

    class Meta:
        fields = ('username', 'password', 'nome','cpf')
        model = Usuario