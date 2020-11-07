# Generated by Django 3.1.3 on 2020-11-02 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestoreventos', '0002_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcionario', models.CharField(max_length=100)),
                ('matricula', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('curso_vinculado', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.curso')),
            ],
        ),
    ]