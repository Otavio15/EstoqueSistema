# Generated by Django 3.1.5 on 2021-02-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210204_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrarproduto',
            name='marca',
            field=models.CharField(default='', max_length=50, verbose_name='Marca'),
            preserve_default=False,
        ),
    ]
