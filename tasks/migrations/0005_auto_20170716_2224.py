# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20170716_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.NullBooleanField(),
        ),
    ]
