# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_auto_20150523_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='ruta_imagen',
            field=models.CharField(max_length=140, default=''),
        ),
    ]
