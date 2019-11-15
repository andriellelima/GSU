from django.shortcuts import render
from .models import Servico, Setor


# Create your views here.
def servico_list(request):
    template_name = 'produto_list.html'
    setor_list = Setor.objects.all()
    servico_list = Servico.objects.all()
    search = request.GET.get('search')
    if search:
        servico_list = servico_list.filter(descricao__icontains=search)
        setor_list = servico_list.objects.all()
    context = {'servicos': servico_list}
    return render(request, template_name, context)
