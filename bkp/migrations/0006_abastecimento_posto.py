# Generated by Django 3.1.5 on 2021-02-05 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210205_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Posto')),
                ('imagem', models.ImageField(blank=True, upload_to='img', verbose_name='Imagem')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Abastecimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(verbose_name='Data do abastecimento')),
                ('valor_litro', models.DecimalField(decimal_places=4, max_digits=100000, verbose_name='Valor por litro')),
                ('valor_total', models.DecimalField(decimal_places=4, max_digits=100000, verbose_name='Valor total do abastecimento')),
                ('imagem', models.ImageField(blank=True, upload_to='img', verbose_name='Imagem')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('posto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.posto')),
                ('veiculo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.cadastrarveiculo')),
            ],
        ),
    ]