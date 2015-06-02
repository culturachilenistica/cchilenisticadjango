# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_remove_pregunta_created_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pregunta',
        ),
    ]
