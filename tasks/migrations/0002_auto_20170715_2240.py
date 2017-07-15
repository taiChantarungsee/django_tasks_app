# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
