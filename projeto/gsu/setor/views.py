from django.shortcuts import render
from .models import Servico, Setor, Diretoria
from django.db.models import Q




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


def setores (request):
    setor = Setor.objects.all()
    return render(request,"list_setores.html", {"setores": setor})