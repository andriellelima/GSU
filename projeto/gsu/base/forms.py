from django import forms
from .models import Sugestao


class SugestaoForm(forms.ModelForm):

    titulo = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}), strip=False, empty_value='Sem contato')
    descricao = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = Sugestao
        fields = ('titulo', 'email', 'descricao')
        