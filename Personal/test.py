from django.test import TestCase
from django.contrib.auth.models import User
from Personal.models import Personal
from .models import Inventario


class PersonalTests(TestCase):
   """En esta clase van todas las pruebas del modelo Curso."""

   def test_creacion_personal(self):
       # caso uso esperado
       self.user = User.objects.create_user(username="egp1020", email='javed@javed.com', password='my_secret')
       persona = Personal(nombre="Nombre", puesto="Puesto", creador=self.user)
       persona.save()

       # Compruebo que la personal fue creado y la data fue guardad correctamente
       self.assertEqual(Personal.objects.count(), 1)
       self.assertEqual(persona.nombre, "Nombre")
       self.assertEqual(persona.puesto, "Puesto")

   def test_persona_str(self):
       self.user = User.objects.create_user(username="egp1020", email='javed@javed.com', password='my_secret')
       persona = Personal(nombre="Leandro", puesto="Jefe", creador=self.user)
       persona.save()

       # Compruebo el str funciona como se dese
       self.assertEqual(persona.__str__(), "Leandro, Jefe")



class InventarioTests(TestCase):
#prueba de modulo de materiales
    def test_creacion_Inventario(self):
         self.user = User.objects.create_user(username="egp1020", email='javed@javed.com', password='my_secret')
         inventario = Inventario(codigo="Codigo", unidades="Unidades", ea= 'Ea', localizador= 'Localizador', comentario='Comentario', creador=self.user)
         inventario.save()

         self.assertEqual(Inventario.objects.count(), 1)
         self.assertEqual(inventario.codigo, "Codigo")
         self.assertEqual(inventario.unidades, "Unidades")
         self.assertEqual(inventario.ea,'Ea')
         self.assertEqual(inventario.localizador,'Localizador')
         self.assertEqual(inventario.comentario,'Comentario')

    import difflib

def test_inventario_str(self):
    self.user = User.objects.create_user(username="egp1020", email='javed@javed.com', password='my_secret')
    inventario = Inventario(codigo="egp1020", unidades='10000', ea='ea', localizador='500-999', comentario='SC', creador=self.user)
    inventario.save()

    # Compruebo el str funciona como se dese
    expected_str = f"egp1020, 10000, ea, 500-999, SC, {self.user.username}"
    actual_str = inventario.__str__()

    print("Expected:", expected_str)
    print("Actual  :", actual_str)

    # Compara las cadenas y muestra las diferencias
    differences = list(difflib.ndiff(expected_str, actual_str))
    for diff in differences:
        print(diff)

    # Comprueba si las cadenas son iguales
    self.assertEqual(actual_str, expected_str)