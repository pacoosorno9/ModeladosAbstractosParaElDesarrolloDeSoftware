# Generated by Django 5.1.1 on 2024-10-11 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rspuesta',
            new_name='Respuesta',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='text_respuesta',
            new_name='texto_respuesta',
        ),
    ]
