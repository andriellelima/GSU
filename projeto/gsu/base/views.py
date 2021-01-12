from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.contrib import  messages
from gsu.setor.models import Setor, Servico
from django.db.models import Q
from .forms import SugestaoForm

# Create your views here.
def sugestao(request):
    form = SugestaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        return redirect('base:home')
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
            Q(tipo__contains=search) |
            Q(descricao__contains=search) |
            Q(setor__nome__contains=search) |
            Q(setor__descricao__contains=search)
        )
        if servico_list:
            print('asaasa')
            template_name='home_search.html'
            context={'servico_list': servico_list}
            return render(request, template_name, context)
        elif not servico_list:
            search_split = search.split()
            servico_list_split = []
            for split in search_split:
                servico = (Servico.objects.filter(
                    Q(titulo__contains=split) |
                    Q(tipo__contains=split) |
                    Q(descricao__contains=split) |
                    Q(setor__nome__contains=split) |
                    Q(setor__descricao__contains=split)
                ))
                if servico:
                    v = True
                    for ser in servico:
                        for s in servico_list_split:
                            if ser == s:
                                v = False
                        if v:
                            servico_list_split.append(ser)
            template_name = 'home_search.html'
            context = {'servico_list': servico_list_split}
            return render(request, template_name, context)
        template_name = 'home_search.html'
        context = {'servico_list': servico_list}
        return render(request, template_name, context)
    return render(request, 'sugestao.html', {'form':form})

def sobre(request):
    return render(request,'sobre.html')

def mapa(request):
    return render(request,'mapa.html')

def home(request):
    setor_list = Setor.objects.all()
    template_name='home.html'
    context={"setores":setor_list}
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
            Q(tipo__contains=search) |
            Q(descricao__contains=search) |
            Q(setor__nome__contains=search) |
            Q(setor__descricao__contains=search)
        )
        if servico_list:

            template_name = 'home_search.html'
            context = {'servico_list': servico_list}
            return render(request, template_name, context)
        elif not servico_list:
            search_split = search.split()
            servico_list_split = []
            for split in search_split:
                servico = (Servico.objects.filter(
                    Q(titulo__contains=split) |
                    Q(tipo__contains=split) |
                    Q(descricao__contains=split) |
                    Q(setor__nome__contains=split) |
                    Q(setor__descricao__contains=split)
                ))
                if servico:
                    v = True
                    for ser in servico:
                        for s in servico_list_split:
                            if ser == s:
                                v = False
                        if v:
                            servico_list_split.append(ser)
            template_name = 'home_search.html'
            context = {'servico_list': servico_list_split}
            return render(request, template_name, context)
        template_name = 'home_search.html'
        context = {'servico_list': servico_list}
        return render(request, template_name, context)
    return render(request,template_name, context)

def logar(request):
    if request.user.is_authenticated:
        return redirect('base:home')
    if request.method == 'POST':
        usuario = request.POST['usuario']
        #usuario = usuario.replace('.','').replace('-','')
        senha = request.POST['senha']
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('/admin')
            else:
                messages.error(request, 'Usuário inativo')
        else:
            messages.error(request, 'CPF ou senha inválidos!')
    return render(request, 'login.html', locals())


def sair(request):
    logout(request)
    return redirect('base:home')

def gerenciar(request):
    return redirect('/admin')