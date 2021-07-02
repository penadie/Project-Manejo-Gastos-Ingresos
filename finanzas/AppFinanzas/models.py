from django.db import models
from django.forms import ModelForm, TextInput, Textarea
# Create your models here.



#-------------------------------------- GASTOS ------------------------------------




class TipoG(models.Model):
    tipog = models.CharField(max_length=200, unique=True)
    usuarioid= models.IntegerField(null=True)
    class Meta:
        db_table: "tipog"
    def __str__(self):
        return u'{0}'.format(self.tipog)

class Gastos(models.Model):
    descripcion = models.CharField(max_length=500)
    monto = models.IntegerField()
    fecha = models.DateField(max_length=12)
    tipog = models.ForeignKey(TipoG, on_delete=models.CASCADE)
    usuarioId= models.IntegerField(null=True)
    class Meta:
        db_table: "gastos"






#------------------------------------ INGRESOS --------------------------------------




class TipoIng(models.Model):
    tipoing = models.CharField(max_length=200, unique=True)
    usuarioId= models.IntegerField(null=True)
    class Meta:
        db_table: "tipoing"
    def __str__(self):
        return u'{0}'.format(self.tipoing)



class Ingresos(models.Model):
    descripcion = models.CharField(max_length=500)
    monto = models.IntegerField()
    fecha = models.DateField(max_length=12)
    tipoing = models.ForeignKey(TipoIng, on_delete=models.CASCADE)
    usuarioId= models.IntegerField(null=True)
    class Meta:
        db_table: "ingresos"

