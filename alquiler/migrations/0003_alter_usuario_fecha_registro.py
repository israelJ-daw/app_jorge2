# Generated by Django 5.1.5 on 2025-01-20 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquiler', '0002_rename_usaurio_usuario_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_registro',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime.now),
        ),
    ]
