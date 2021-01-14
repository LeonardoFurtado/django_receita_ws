# Generated by Django 3.1.5 on 2021-01-14 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2021, 1, 14), verbose_name='Creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AddField(
            model_name='company',
            name='updated',
            field=models.DateField(auto_now_add=True, default=datetime.date(2021, 1, 14), verbose_name='Update date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2021, 1, 14), verbose_name='Creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AddField(
            model_name='service',
            name='updated',
            field=models.DateField(auto_now_add=True, default=datetime.date(2021, 1, 14), verbose_name='Update date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2021, 1, 14), verbose_name='Creation date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='updated',
            field=models.DateField(auto_now_add=True, default=datetime.date(2021, 1, 14), verbose_name='Update date'),
            preserve_default=False,
        ),
    ]
