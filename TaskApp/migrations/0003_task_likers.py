# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TaskApp', '0002_auto_20170117_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='likers',
            field=models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
