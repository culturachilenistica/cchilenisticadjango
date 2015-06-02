# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_pregunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='texto_pregunta',
            field=models.TextField(null=True),
        ),
    ]
