# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0015_auto_20150523_1421'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pregunta',
        ),
    ]
