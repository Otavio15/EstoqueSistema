# Generated by Django 3.1.5 on 2021-02-04 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210204_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Produto')),
                ('imagem', models.ImageField(blank=True, upload_to='img', verbose_name='Imagem')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cadastrarproduto',
            name='fabricante_veiculo',
        ),
        migrations.AlterField(
            model_name='cadastrarproduto',
            name='marca_produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.marca'),
        ),
    ]