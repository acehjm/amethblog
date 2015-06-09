# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneblog', '0007_auto_20150526_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
    ]
