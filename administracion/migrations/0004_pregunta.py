# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_delete_pregunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('alternativa_1', models.TextField()),
                ('alternativa_2', models.TextField()),
                ('alternativa_3', models.TextField()),
                ('alternativa_4', models.TextField()),
                ('alternativa_correcta', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
