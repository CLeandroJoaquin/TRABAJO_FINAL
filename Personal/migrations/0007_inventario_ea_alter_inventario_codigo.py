# Generated by Django 4.2.3 on 2023-08-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0006_alter_inventario_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='ea',
            field=models.CharField(default='ea', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventario',
            name='codigo',
            field=models.CharField(max_length=64),
        ),
    ]
