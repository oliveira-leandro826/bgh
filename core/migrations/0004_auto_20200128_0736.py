# Generated by Django 2.2.3 on 2020-01-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200124_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acesso',
            name='imagem',
        ),
        migrations.AddField(
            model_name='acesso',
            name='imagem',
            field=models.OneToOneField(default=1, on_delete='cascade', to='core.Imagem'),
        ),
    ]
