# Generated by Django 2.2.3 on 2020-01-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200128_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='especie',
            field=models.ForeignKey(on_delete='cascade', to='core.Especie'),
        ),
    ]