
from django import forms
from django.db import models
from django.forms import fields
from AppFinanzas.models import Gastos, Ingresos, TipoG, TipoIng
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TipoGForm(forms.ModelForm):
    class Meta:
        model = TipoG
        fields = ['tipog', 'usuarioid']

class TipoIngForm(forms.ModelForm):
    class Meta:
        model = TipoIng
        fields= ['tipoing','usuarioId']

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = ['monto','fecha','descripcion','tipog', 'usuarioId']
        formfield_overrides = {
            models.DateTimeField: {
                'fecha': ('%m/%d/%Y')
            },
    }


class IngresosForm(forms.ModelForm):
    class Meta:
        model = Ingresos
        fields = ['monto','fecha','descripcion','tipoing', 'usuarioId']
        formfield_overrides = {
            models.DateTimeField: {
                'fecha': ('%m/%d/%Y')
            },
    }

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']