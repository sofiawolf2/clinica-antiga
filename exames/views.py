from django.shortcuts import render
from exames.models import Exames
from django.views.generic import ListView
from django.urls import reverse_lazy
from exames.forms import ExamesCreateForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
# LoginRequiredMixin é uma condição pra so fazer o que quer se estiver logado antes

# Create your views here.
class ExamesListView(ListView):
    model = Exames
    context_object_name = 'exames' #o que vamos chamar no for do html
    template_name = 'exames/verexames.html'
    ordering = ['-created_at']

class ExamesCreateView(LoginRequiredMixin , generic.CreateView):
    model = Exames
    form_class = ExamesCreateForm
    template_name = 'exames/criarexames.html'
    success_url = reverse_lazy('exames:ver_exames')

class ExamesUpdateView(LoginRequiredMixin ,generic.UpdateView):
    model = Exames
    fields = ['medico','paciente','sintomas','diagnostico','medicamento','cpf','rg']
    template_name = 'exames/editarexames.html'
    success_url = reverse_lazy('exames:ver_exames')

class ExamesDeletView(LoginRequiredMixin ,generic.DeleteView):
    model = Exames
    context_object_name = 'exames'
    template_name = 'exames/deletarexames.html'
    success_url = reverse_lazy('exames:ver_exames')