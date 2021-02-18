# Generated by Django 3.1.5 on 2021-02-16 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210216_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abastecimento',
            name='posto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.posto'),
        ),
        migrations.AlterField(
            model_name='abastecimento',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cadastrarveiculo'),
        ),
        migrations.AlterField(
            model_name='cadastrarproduto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria'),
        ),
        migrations.AlterField(
            model_name='cadastrarproduto',
            name='marca_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.marca'),
        ),
        migrations.AlterField(
            model_name='cadastrarproduto',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.produto'),
        ),
        migrations.AlterField(
            model_name='cadastrarproduto',
            name='unidade_de_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.unidademedida'),
        ),
        migrations.AlterField(
            model_name='manutencao',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.local', verbose_name='Local da manutenção'),
        ),
        migrations.AlterField(
            model_name='manutencao',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cadastrarveiculo'),
        ),
    ]
