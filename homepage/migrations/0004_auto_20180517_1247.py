# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20180517_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='AddressID',
            new_name='Address',
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='Username',
            field=models.EmailField(max_length=150),
        ),
    ]
