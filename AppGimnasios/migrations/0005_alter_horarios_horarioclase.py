# Generated by Django 4.0.4 on 2022-06-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGimnasios', '0004_alter_horarios_horarioclase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios',
            name='horarioClase',
            field=models.TimeField(),
        ),
    ]