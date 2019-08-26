from django import forms
from exames.models import Exames
from django.contrib.auth.forms import ExamesCreationForm

class ExamesCreateForm(UserCreationForm):
    class Meta:
        model = Exames
        fields = ['medico','paciente','sintomas','diagnostico','medicamento','cpf','rg']