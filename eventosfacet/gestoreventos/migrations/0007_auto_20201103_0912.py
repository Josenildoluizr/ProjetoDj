# Generated by Django 3.1.3 on 2020-11-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestoreventos', '0006_auto_20201103_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(default=20201103),
        ),
    ]
