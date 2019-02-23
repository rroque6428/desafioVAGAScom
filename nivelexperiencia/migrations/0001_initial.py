# Generated by Django 2.0.4 on 2019-02-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NivelExperiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('nivel', models.IntegerField()),
            ],
            options={
                'ordering': ('nivel',),
                'verbose_name': 'Nivel de Experiência',
            },
        ),
    ]