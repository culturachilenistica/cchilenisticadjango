# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_remove_pregunta_alternativa_correcta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_2',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_3',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_4',
            field=models.CharField(max_length=500),
        ),
    ]
