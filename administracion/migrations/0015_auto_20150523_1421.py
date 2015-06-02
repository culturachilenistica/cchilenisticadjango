# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0014_pregunta_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='fecha_creacion',
            field=models.DateTimeField(blank=True, null=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
