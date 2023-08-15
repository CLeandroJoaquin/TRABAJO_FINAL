from django.urls import include, path
from . import views
from .views import inicio
urlpatterns = [
    path("",inicio, name="inicio"),
    path("personal/", views.lista_personal,name="Personal"),
    path("personal/crear-persona/", views.crear_personal, name="crear_personal"),
    path("personal", views.lista_personal, name="lista_personal"),
    path("buscar-persona/", views.buscar_personal, name="buscar_personal"),
    path('eliminar-persona/<int:id>/', views.eliminar_personal, name="eliminar_persona"),
    path("editar-curso/<int:id>/", views.editar_personal, name="editar_persona"),
    path("personal/crear-inventario/", views.crear_material, name="crear_material"),
    path("personal/lista-material/",views.lista_material, name="lista_material"),
    path("personal/buscar-material/", views.buscar_material, name="buscar_material"),
    path("personal/editar-material/<int:id>/", views.editar_material, name="editar_material"),
    path("personal/eliminar-material/<int:id>/", views.eliminar_material, name="eliminar_material"),

    path("personal/crear-venta/", views.crear_venta, name="crear_venta"),
    path("personal/lista-venta/",views.lista_ventas, name="lista_ventas"),
    path("personal/buscar-venta/", views.buscar_venta, name="buscar_venta"),
    path("personal/editar-venta/<int:id>/", views.editar_venta, name="editar_venta"),
    path("personal/eliminar-venta/<int:id>/", views.eliminar_venta, name="eliminar_venta"),
    path("personal/ver-historial-inventario/<int:id>/", views.ver_historial_inventario, name="ver_historial_inventario"),

]