# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('texto_pregunta', models.TextField(null=True)),
                ('alternativa_1', models.CharField(max_length=500)),
                ('alternativa_2', models.CharField(max_length=500)),
                ('alternativa_3', models.CharField(max_length=500)),
                ('alternativa_4', models.CharField(max_length=500)),
                ('alternativa_correcta', models.PositiveSmallIntegerField(default=1, choices=[(1, 'Alternativa 1'), (2, 'Alternativa 2'), (3, 'Alternativa 3'), (4, 'Alternativa 4')])),
                ('fecha_creacion', models.DateTimeField(null=True, editable=False, default=django.utils.timezone.now, blank=True)),
            ],
        ),
    ]
