# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Details(models.Model):
    db_table = 'currencies'
    name = models.CharField(max_length=200,  default="NA")
    country = models.IntegerField(null=True)
    currency_symbol = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=1, null=False)

#    def __str__(self):
#        return self.username

#class Migration(migrations.Migration):

#    initial = True#

#    dependencies = [    ]

#    operations = [
#        migrations.CreateModel(
#            name='Currencies',
#            fields=[
#                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                ('currency', models.CharField(max_length=200)),
#                ('currency_symbol', models.CharField(max_length=200)),
#                ('currency_symbol', models.CharField(max_length=200)),
#                ('is_active', models.IntegerField(default=1)),
#            ],
#        ),
        #migrations.CreateModel(
        #    name='Question',
        #    fields=[
        #        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #        ('question_text', models.CharField(max_length=200)),
        #        ('pub_date', models.DateTimeField(verbose_name='date published')),
        #    ],
        #),
        #migrations.AddField(
        #    model_name='choice',
        #    name='question',
        #    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        #),
#    ]