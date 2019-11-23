from django.shortcuts import render, redirect
from .models import Servico, Setor, Diretoria
from django.db.models import Q



def setor_servicos(request, setor_id):
    template_name = 'setor_servicos.html'
    setor = Setor.objects.get(pk=setor_id)
    servico_list = Servico.objects.filter(setor__id=setor_id)
    diretoria_list = Diretoria.objects.filter(setor_id = setor_id)
    context = {'servico_list':servico_list, 'setor': setor, 'diretoria_list': diretoria_list}
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
            Q(tipo__contains=search) |
            Q(descricao__contains=search) |
            Q(setor__nome__contains=search)
        )
        template_name='home_search.html'
        context={'servico_list': servico_list}
        return render(request, template_name, context)
    return render(request, template_name, context)


def setores (request):
    setor = Setor.objects.all()
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
            Q(tipo__contains=search) |
            Q(descricao__contains=search) |
            Q(setor__nome__contains=search)
        )
        template_name='home_search.html'
        context={'servico_list': servico_list}
        return render(request, template_name, context)
    return render(request,"list_setores.html", {"setores": setor})