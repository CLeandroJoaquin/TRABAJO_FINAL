from django.shortcuts import render
from Personal.models import Personal, Ventas, Inventario
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Personal.forms import PersonalFormulario 
from django.db.models import Q
from Personal.forms import InventarioFormulario
from Personal.forms import VentaFormulario
from .models import HistorialInventario
from datetime import datetime
from datetime import date 

# Create your views here.
@login_required
def lista_personal(request):
    
    contexto = {
            "personal": Personal.objects.all(),
    }
    http_response = render(
            request=request,
            template_name='Personal/lista_personal.html',
            context=contexto,
        )
    return http_response

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response



def crear_personal_version1(request):
   if request.method == "POST":
       data = request.POST
       personal = Personal(nombre=data['nombre'], numero_legajo=data['numero_legajo'])
       personal.save()
       url_exitosa = reverse('lista_personal')
       return redirect(url_exitosa)
   else:  # GET
       return render(
           request=request,
           template_name='Personal/formulario_crear_persona_a_mano.html',
       )




def crear_personal(request):
   if request.method == "POST":
       formulario = PersonalFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           numero_legajo = data["numero_legajo"]
           antiguedad= data["antiguedad"]  # lo crean solo en RAM
           puesto=data["puesto"]
           personal = Personal(nombre=nombre, numero_legajo=numero_legajo, antiguedad=antiguedad, puesto=puesto)
           personal.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_personal')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = PersonalFormulario()
   http_response = render(
       request=request,
       template_name='Personal/formulario_persona.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_personal(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       nombre = Personal.objects.filter(nombre__contains=busqueda)
       
       
       #nombre = Personal.objects.filter(
        #   Q(nombre__contains=busqueda) | Q(puesto__contains=busqueda) | Q(numero_legajo__contains=busqueda) | Q(antiguedad__contains=busqueda)
       #)
       contexto = {
           "personal": nombre,
       }
       http_response = render(
           request=request,
           template_name='Personal/lista_personal.html',
           context=contexto,
       )
       return http_response




def eliminar_personal(request, id):
   persona = Personal.objects.get(id=id)
   if request.method == "POST":
       #borra la persona
       persona.delete()
       #redirecciona a la url exitosa
       url_exitosa = reverse('lista_personal')
       return redirect(url_exitosa)


def editar_personal(request, id):
   persona = Personal.objects.get(id=id)
   if request.method == "POST":
       formulario = PersonalFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           persona.nombre = data['nombre']
           persona.numero_legajo = data['numero_legajo']
           persona.antiguedad=data['antiguedad']
           persona.puesto=data['puesto']
           persona.save()
           url_exitosa = reverse('lista_personal')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': persona.nombre,
           'numero_legajo': persona.numero_legajo,
           'antiguedad':persona.antiguedad,
           'puesto':persona.puesto,
           
       }
       formulario = PersonalFormulario(initial=inicial)
   return render(
       request=request,
       template_name='Personal/formulario_persona.html',
       context={'formulario': formulario},
   )

       

#DEFINICION DE CODIGO PARA INVENTARIOS....DAR DE ALTA MATERIAL, EDITAR, Y ELIMINAR


def lista_material(request):
    
    contexto = {
            "material": Inventario.objects.all(),
    }
    http_response = render(
            request=request,
            template_name='Personal/lista_material.html',
            context=contexto,
        )
    return http_response



def crear_material(request):
   if request.method == "POST":
       formulario = InventarioFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           codigo = data["codigo"]
           unidades = data["unidades"]
           ea=data["ea"]
           localizador= data["localizador"]  # lo crean solo en RAM
           fecha=data["fecha"]
           comentario= data['comentario']
           creador = request.user
          
           inventario = Inventario(codigo=codigo, unidades=unidades, ea=ea, localizador=localizador, fecha=fecha, comentario=comentario, creador=creador)
           inventario.save()  # Lo guardan en la Base de datos
           #######################################################
           #### CAMPO HISTORIAL DE INVENTARIO###################

           HistorialInventario.objects.create(
                material=inventario,
                cantidad_anterior=0,  # Puede ser 0 si es una creación inicial
                cantidad_nueva=inventario.unidades,
                fecha=date.today(),
                usuario=request.user,
            )
           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('crear_material')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = InventarioFormulario()
       http_response = render(
       request=request,
       template_name='Personal/formulario_inventario.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_material(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       codigo = Inventario.objects.filter(codigo__contains=busqueda)
       
       
       #nombre = Personal.objects.filter(
        #   Q(nombre__contains=busqueda) | Q(puesto__contains=busqueda) | Q(numero_legajo__contains=busqueda) | Q(antiguedad__contains=busqueda)
       #)
       contexto = {
           "material": codigo,
       }
       http_response = render(
           request=request,
           template_name='Personal/lista_material.html',
           context=contexto,
       )
       return http_response




def eliminar_material(request, id):
   material = Inventario.objects.get(id=id)
   if request.method == "POST":
       #borra la persona
       material.delete()
       #redirecciona a la url exitosa
       url_exitosa = reverse('lista_material')
       return redirect(url_exitosa)

def editar_material(request, id):
    material = Inventario.objects.get(id=id)
    if request.method == "POST":
        formulario = InventarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            material.codigo = data['codigo']
            material.unidades = data['unidades']
            material.ea = data['ea']
            material.localizador = data['localizador']
            material.fecha = data['fecha']
            material.comentario = data['comentario']


            if not material.creador:
                material.creador = request.user

            material.save()

#################################################################
###### AGREGADO DE CAMPO HISTORIAL DE MATERIALES#################
            HistorialInventario.objects.create(
                material=material,
                cantidad_anterior=material.unidades,  # Cantidad anterior antes de la edición
                cantidad_nueva=data['unidades'],
                fecha=date.today(),
                usuario=request.user,
            )

################################################################
            url_exitosa = reverse('lista_material')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'codigo': material.codigo,
            'unidades': material.unidades,
            'ea':material.ea,
            'localizador': material.localizador,
            'fecha':material.fecha,
            'comentario': material.comentario,
        }
        formulario = InventarioFormulario(initial=inicial)
    return render(
        request=request,
        template_name='Personal/formulario_inventario.html',  # Corrección en el nombre de la plantilla
        context={'formulario': formulario},
    )

############################# AGREGADO DE HISTORIAL DE MATERIALES######################   

def ver_historial_inventario(request, id):
    material = Inventario.objects.get(id=id)
    historial = HistorialInventario.objects.filter(material=material).order_by('-fecha')

    contexto = {
        'material': material,
        'historial': historial,
    }
    return render(
        request=request,
        template_name='Personal/ver_historial_inventario.html',
        context=contexto,
    )
#######################################################################################




######################################################################################
#DEFINICION DE CODIGOS DE VENTAS

def lista_ventas(request):
    
    contexto = {
            "ventas": Ventas.objects.all(),
    }
    http_response = render(
            request=request,
            template_name='Personal/lista_ventas.html',
            context=contexto,
        )
    return http_response


def crear_venta(request):
   if request.method == "POST":
       formulario = VentaFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           codigo_de_producto = data["codigo_de_producto"]
           unidades = data["unidades"]
           vendedor = data["vendedor"]
           descripcion = data["descripcion"]
           codigo_cliente = data["codigo_cliente"]
           fecha_venta = data["fecha_venta"]
           

           ventas = Ventas(codigo_de_producto=codigo_de_producto, unidades=unidades, vendedor=vendedor, descripcion=descripcion, codigo_cliente=codigo_cliente, fecha_venta=fecha_venta)
           ventas.save()

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('crear_venta')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = VentaFormulario()
       http_response = render(
       request=request,
       template_name='Personal/formulario_ventas.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_venta(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       codigo = Ventas.objects.filter(codigo__contains=busqueda)
       
       
       #nombre = Personal.objects.filter(
        #   Q(nombre__contains=busqueda) | Q(puesto__contains=busqueda) | Q(numero_legajo__contains=busqueda) | Q(antiguedad__contains=busqueda)
       #)
       contexto = {
           "venta": codigo,
       }
       http_response = render(
           request=request,
           template_name='Personal/lista_ventas.html',
           context=contexto,
       )
       return http_response




def eliminar_venta(request, id):
   venta = Ventas.objects.get(id=id)
   if request.method == "POST":
       
       venta.delete()
       #redirecciona a la url exitosa
       url_exitosa = reverse('lista_ventas')
       return redirect(url_exitosa)

def editar_venta(request, id):
    venta = Ventas.objects.get(id=id)
    if request.method == "POST":
        formulario = VentaFormulario(request.POST)




        if formulario.is_valid():
            data = formulario.cleaned_data
            venta.codigo_de_producto= data['codigo_de_producto']
            venta.unidades=data['unidades']
            venta.vendedor = data['vendedor']
            venta.descripcion = data['descripcion']
            venta.codigo_cliente = data['codigo_cliente']
            venta.fecha_venta = data['fecha_venta']
            

           

            venta.save()
            url_exitosa = reverse('lista_ventas')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'codigo_de_producto': venta.codigo_de_producto,
            'unidades':venta.unidades,
            'vendedor': venta.vendedor,
            'descripcion':venta.descripcion,
            'codigo_cliente': venta.codigo_cliente,
            'fecha_venta': venta.fecha_venta,
        }
        formulario = VentaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='Personal/formulario_ventas.html',  # Corrección en el nombre de la plantilla
        context={'formulario': formulario},
    )
       