from django import forms
from .models import Sugestao


class SugestaoForm(forms.ModelForm):

    titulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Sugestao
        fields = ('titulo', 'email', 'descricao',)
        