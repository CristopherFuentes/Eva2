from django import forms
from pacientes.models import Paciente
import re

class FormPaciente(forms.ModelForm):
    class Meta: 
        model = Paciente
        fields = '__all__'

