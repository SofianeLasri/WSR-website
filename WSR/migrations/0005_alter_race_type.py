# Generated by Django 4.2.1 on 2023-06-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WSR', '0004_alter_race_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='type',
            field=models.CharField(choices=[('invitation', 'Invitation'), ('championship', 'Championship'), ('single_race', 'Single Race'), ('face_to_face', 'Face To Face'), ('overtaking', 'Overtaking'), ('against_time', 'Against Time'), ('elimination', 'Elimination')], default='single_race', max_length=100),
        ),
    ]
