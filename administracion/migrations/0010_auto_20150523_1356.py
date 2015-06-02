# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0009_pregunta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_correcta',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Alternativa 1'), (2, 'Alternativa 2'), (3, 'Alternativa 3'), (4, 'Alternativa 4')], default=1),
        ),
    ]
