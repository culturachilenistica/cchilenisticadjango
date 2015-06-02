# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_auto_20150523_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='alternativa_correcta',
            field=models.PositiveSmallIntegerField(max_length=1, default=1, choices=[(1, 'Alternativa 1'), (2, 'Alternativa 2'), (3, 'Alternativa 3'), (4, 'Alternativa 4')]),
        ),
    ]
