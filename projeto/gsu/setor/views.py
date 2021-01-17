from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q



def setor_servicos(request, setor_id):
    template_name = 'setor_servicos.html'
    setor = Setor.objects.get(pk=setor_id)
    servico_list = Servico.objects.filter(setor__id=setor_id)
    context = {'servico_list':servico_list, 'setor': setor}
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
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
    return render(request, template_name, context)



def setores (request):
    setor = Setor.objects.all()
    search = request.GET.get('search')
    if search:
        servico_list = Servico.objects.filter(
            Q(titulo__contains=search) |
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
    return render(request,"list_setores.html", {"setores": setor})