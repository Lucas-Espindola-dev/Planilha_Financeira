# Generated by Django 4.2.4 on 2023-08-29 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planilha', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Despesas',
            new_name='Despesa',
        ),
        migrations.RenameModel(
            old_name='Receitas',
            new_name='Receita',
        ),
    ]
