# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('cuit', models.CharField(max_length=256)),
                ('registration', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('dni', models.IntegerField()),
                ('cuit', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('cooperative', models.ForeignKey(to='recibos.Cooperative')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('partner', models.ForeignKey(to='recibos.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
