# Generated by Django 2.0.4 on 2019-02-21 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nivelexperiencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=80)),
                ('descricao', models.TextField()),
                ('localizacao', models.CharField(max_length=1)),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nivelexperiencia.NivelExperiencia')),
            ],
        ),
    ]