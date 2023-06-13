# Generated by Django 4.2.2 on 2023-06-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WSR', '0017_racetype_alter_race_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racetype',
            name='font_awesome_icon',
        ),
        migrations.AddField(
            model_name='racetype',
            name='icon',
            field=models.ImageField(blank=True, default='', upload_to='racetypes', verbose_name="Logo d'illustration"),
        ),
    ]
