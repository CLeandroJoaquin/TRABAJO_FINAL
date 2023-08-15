from datetime import datetime
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.utils import timezone
import datetime
# Create your models here.



class Personal(models.Model):
    nombre = models.CharField(max_length=230)
    numero_legajo = models.CharField(max_length=230)
    antiguedad = models.IntegerField(null=True)
    puesto = models.CharField(max_length=230, default='Sin puesto') 
    creador = models.ForeignKey(User, on_delete= models.CASCADE, related_name='personas_creadas', default=1)
    def __str__(self):
            return f"{self.nombre}, {self.puesto}"
    #,{self.numero_legajo},{self.antiguedad},

class Inventario(models.Model):
    codigo = models.CharField(max_length=64)
    unidades = models.CharField(max_length=230)
    ea=models.TextField(max_length=10)
    localizador = models.CharField(max_length=54)
    fecha = models.DateField()
    comentario=models.CharField(max_length=5000)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materiales_creados', default=1)
    

    
    def __str__(self):
         return f"{self.codigo},{self.unidades},{self.ea},{self.localizador},{self.fecha} ,{self.comentario}"
 
 #############################################
 #agregado de HISTORIAL DE MATERIALES   
class HistorialInventario(models.Model):
    material = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad_anterior = models.IntegerField()
    cantidad_nueva = models.IntegerField()
    fecha = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

################################################


class Ventas(models.Model):
    codigo_de_producto=models.CharField(max_length=230)
    unidades = models.IntegerField(null=True)
    vendedor = models.CharField(max_length=230)
    descripcion= models.TextField()
    codigo_cliente=models.CharField(max_length=50)
    fecha_venta = models.DateField(default=timezone.now)
    def __str__(self):
         return f"{self.codigo_de_producto}, {self.unidades},{self.vendedor},{self.descripcion},{self.codigo_cliente},{self.fecha_venta}"
    



