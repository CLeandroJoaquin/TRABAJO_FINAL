# Generated by Django 4.2.3 on 2023-08-13 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Personal', '0010_ventas_codigo_cliente_ventas_fecha_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='fecha_venta',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='HistorialInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_anterior', models.IntegerField()),
                ('cantidad_nueva', models.IntegerField()),
                ('fecha', models.DateField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personal.inventario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
