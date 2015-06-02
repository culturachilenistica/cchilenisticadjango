# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0010_auto_20150523_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='title',
        ),
    ]
