# Generated by Django 4.2.16 on 2024-11-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='nome_completo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]