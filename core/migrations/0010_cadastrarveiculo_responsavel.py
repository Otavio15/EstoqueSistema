# Generated by Django 3.1.5 on 2021-02-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210204_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrarveiculo',
            name='responsavel',
            field=models.CharField(default='', max_length=50, verbose_name='Responsável do veículo'),
            preserve_default=False,
        ),
    ]
