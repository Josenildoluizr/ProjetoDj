# Generated by Django 3.1.3 on 2020-11-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestoreventos', '0005_auto_20201103_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateTimeField(default='2020-11-04'),
        ),
    ]
