from django.shortcuts import render
from .models import Servico, Setor, Diretoria
from django.db.models import Q

# Create your views here.
def proaes(request):
    return render(request, 'proaes.html')

def list_setor(request):
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
        template_name='home_search.html'
        context={'servico_list': servico_list}
        # setor_list = Setor.objects.filter()
    return render(request,template_name, context)


def servico_pesquisa(request):
    template_name = 'produto_list.html'
    servico_list = Servico.objects.all()
    search = request.GET.get('search')
    if search:
        servico_list = servico_list.filter(descricao__icontains=search)
    context = {'servicos': servico_list}
    return render(request, template_name, context)


def setor_servicos(request, setor_id):
    template_name = 'setor_servicos.html'
    setor = Setor.objects.get(pk=setor_id)
    servico_list = Servico.objects.filter(setor__id=setor_id)
    diretoria_list = Diretoria.objects.filter(setor_id = setor_id)
    context = {'servico_list':servico_list, 'setor': setor, 'diretoria_list': diretoria_list}
    return render(request, template_name, context)


