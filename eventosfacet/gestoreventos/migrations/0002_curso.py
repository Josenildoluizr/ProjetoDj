# Generated by Django 3.1.3 on 2020-11-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestoreventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=100)),
                ('codigo_curso', models.IntegerField()),
            ],
        ),
    ]
