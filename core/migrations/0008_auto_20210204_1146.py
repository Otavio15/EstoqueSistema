# Generated by Django 3.1.5 on 2021-02-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cadastrarproduto_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastrarproduto',
            name='marca',
        ),
        migrations.AddField(
            model_name='cadastrarproduto',
            name='marca_produto',
            field=models.CharField(default='', max_length=50, verbose_name='Marca do produto'),
            preserve_default=False,
        ),
    ]
