# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 13:05
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('nome_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome')),
                ('abreviacao', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='movimentacaoestoque',
            name='data_informada',
            field=models.DateField(verbose_name='Data compra'),
        ),
        migrations.AddField(
            model_name='movimentacaoestoque',
            name='medida',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estoque.UnidadeMedida'),
            preserve_default=False,
        ),
    ]
