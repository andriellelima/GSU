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
    return render(request, 'sugestao.html', {'form':form})


# def home(request):
#     setor_list = Setor.objects.all()
#     template_name='home.html'
#     context={"setores":setor_list}
#     search = request.GET.get('search')
#     if search:
#         servico_list = Servico.objects.filter(
#             Q(titulo__contains=search) |
#             Q(tipo__contains=search) |
#             Q(descricao__contains=search)
#         )
#         if len(servico_list) == 0:
#             busca = Q()
#             ignorar = ["a","de","para","e","o","quem","onde","que"]
#             for palavra in search.split(" "):
#                 print (palavra)
#                 if palavra.lower() in ignorar:
#                     busca = Q(titulo__contains=search) | Q(tipo__contains=search) | Q(descricao__contains=search)
#             servico_list = Servico.objects.filter(busca)
#             # print (busca)
#             # if len(busca) > 0:
#             #     servico_list = Servico.objects.filter(busca)
#             #     template_name = 'home_search.html'
#             #     context = {'servico_list': servico_list}
#             #     return render(request, template_name, context)
#             # else:
#                 # busca is None
#                 # servico_list = Servico.objects.filter(busca)
#                 # template_name = 'home_search.html'
#                 # context = {'servico_list': servico_list}
#                 # return render(request, template_name, context)
#
#
#     template_name = 'home_search.html'
#     context = {'servico_list': servico_list}
#     return render(request, template_name, context)

def home(request):
    setor_list = Setor.objects.all()
    template_name='home.html'
    context={"setores":setor_list}
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
            Q(tipo__contains=search) |
            Q(descricao__contains=search)
        )
        if len(servico_list) == 0:
            busca = Q()
            ignorar = ["a","de","para","e","o","quem","onde","que"]
            for palavra in search.split(" "):
                print (palavra)
                if palavra.lower() in ignorar:
                    busca = Q(titulo__contains=search) | Q(tipo__contains=search) | Q(descricao__contains=search)

            servico_list = Servico.objects.filter(busca)

        template_name='home_search.html'
        context={'servico_list': servico_list}
    return render(request,template_name, context)

def logar(request):
    if request.user.is_authenticated:
        return redirect('setor:setor')
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
                return redirect('setor:setor')
            else:
                messages.error(request, 'Usuário inativo')
        else:
            messages.error(request, 'CPF ou senha inválidos!')
    return render(request, 'login.html', locals())


# def logar(request):
#     if request.user.is_authenticated:
#         return redirect('core:index')
#     if request.method == 'POST':
#         usuario = request.POST['usuario']
#         usuario = usuario.replace('.', '').replace('-', '')
#         senha = request.POST['senha']
#         user = authenticate(username=usuario, password=senha)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 if request.GET.get('next'):
#                     return redirect(request.GET.get('next'))
#                 return redirect('core:index')
#             else:
#                 messages.error(request, 'Usuário inativo')
#         else:
#             messages.error(request, 'CPF ou senha inválidos!')
#     return render(request, 'login/login.html', locals())


def sair(request):
    logout(request)
    return redirect('logar')
