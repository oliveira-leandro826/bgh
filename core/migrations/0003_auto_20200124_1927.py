# Generated by Django 2.2.3 on 2020-01-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200124_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='caminho',
            field=models.ImageField(upload_to='imagens/', verbose_name='caminho'),
        ),
    ]