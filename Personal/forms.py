from django import forms
from datetime import date

class PersonalFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   numero_legajo = forms.IntegerField(required=True, max_value=50000)
   antiguedad= forms.IntegerField(required=True, max_value=200)
   puesto = forms.CharField(required=True, max_length=64)

class InventarioFormulario(forms.Form):
   codigo = forms.CharField(required=True, max_length=64)
   unidades = forms.IntegerField(required=True, max_value=50000)
   ea = forms.CharField(max_length=10)
   localizador= forms.CharField(required=True, max_length=200)
   fecha=forms.DateField(initial=date.today())
   comentario=forms.CharField(max_length=5000)
   
class VentaFormulario(forms.Form):
   codigo_de_producto=forms.CharField(max_length=230)
   unidades = forms.IntegerField(required=False)
   vendedor = forms.CharField(max_length=230)
   descripcion= forms.CharField(max_length=5000)
   codigo_cliente=forms.CharField(max_length=50)
   fecha_venta=forms.DateField(initial=date.today())
    