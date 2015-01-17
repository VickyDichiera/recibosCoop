# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal',
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
        migrations.RemoveField(
            model_name='retiro',
            name='partner',
        ),
        migrations.DeleteModel(
            name='Retiro',
        ),
    ]
