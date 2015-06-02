# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_pregunta_texto_pregunta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='alternativa_correcta',
        ),
    ]
