# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0008_pregunta_alternativa_correcta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='title',
            field=models.CharField(default='Pregunta sin Titulo', max_length=200),
            preserve_default=False,
        ),
    ]
