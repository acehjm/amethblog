# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oneblog', '0003_auto_20150526_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('time_submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip', models.IPAddressField()),
                ('post', models.ForeignKey(to='oneblog.Article')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
