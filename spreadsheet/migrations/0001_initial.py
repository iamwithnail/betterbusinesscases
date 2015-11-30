# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workbooks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workbook_name', models.CharField(max_length=30)),
                ('sheet_name', models.CharField(max_length=30)),
                ('data', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
