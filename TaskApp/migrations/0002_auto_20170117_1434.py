# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_desc',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='task',
            name='doc',
        ),
    ]
