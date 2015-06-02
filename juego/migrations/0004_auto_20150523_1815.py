# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0003_categoria_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id_partida', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_correctas', models.PositiveSmallIntegerField(default=0)),
                ('cantidad_incorrectas', models.PositiveSmallIntegerField(default=0)),
                ('cantidad_omitidas', models.PositiveSmallIntegerField(default=0)),
                ('puntaje_obtenido', models.IntegerField(default=0, editable=False)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Partida_Preguntas',
            fields=[
                ('id_partida_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('partida', models.ForeignKey(to='juego.Partida')),
            ],
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_1',
            field=models.CharField(default='Alternativa 1', max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_2',
            field=models.CharField(default='Alternativa 2', max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_3',
            field=models.CharField(default='Alternativa 3', max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='alternativa_4',
            field=models.CharField(default='Alternativa 4', max_length=500),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, editable=False),
        ),
        migrations.AddField(
            model_name='partida_preguntas',
            name='pregunta',
            field=models.ForeignKey(to='juego.Pregunta'),
        ),
    ]
