# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0011_remove_pregunta_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
