# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0012_pregunta_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='created_date',
        ),
    ]
