# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_categoria', models.CharField(default='General', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='texto_pregunta',
            field=models.TextField(null=True, default='No existe texto en el campo pregunta'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='categoria',
            field=models.ForeignKey(to='juego.Categoria', default=1),
        ),
    ]
