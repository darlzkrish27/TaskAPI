# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=20)),
                ('task_desc', models.TextField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default=b'Images/None/No-img.jpg', upload_to=b'Images/')),
                ('doc', models.FileField(default=b'Doc/None/No-doc.pdf', upload_to=b'Doc/')),
            ],
        ),
    ]
