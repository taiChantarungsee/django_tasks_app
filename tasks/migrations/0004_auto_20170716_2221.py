# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
