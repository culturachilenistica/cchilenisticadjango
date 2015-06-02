# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_auto_20150523_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='fecha_creacion',
            field=models.DateTimeField(null=True, blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
