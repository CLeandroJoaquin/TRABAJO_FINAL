from django.contrib import admin

# Register your models here.
from  .models import Personal, Ventas, Inventario
from django.contrib import admin
from perfiles.models import Avatar

admin.site.register(Personal)
admin.site.register(Ventas)
admin.site.register(Inventario)
admin.site.register(Avatar)

