# Generated by Django 4.2.2 on 2023-06-12 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WSR', '0015_alter_race_circuit_alter_race_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='vehicles', verbose_name="Image d'illustration"),
        ),
        migrations.AlterField(
            model_name='driver',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WSR.vehicle', verbose_name='Véhicule'),
        ),
        migrations.AlterField(
            model_name='race',
            name='finishing_position',
            field=models.PositiveIntegerField(verbose_name="Position d'arrivée"),
        ),
        migrations.AlterField(
            model_name='race',
            name='image',
            field=models.ImageField(upload_to='race_images', verbose_name="Image d'illustration"),
        ),
        migrations.AlterField(
            model_name='result',
            name='finishing_position',
            field=models.PositiveIntegerField(verbose_name="Position d'arrivée"),
        ),
        migrations.AlterField(
            model_name='result',
            name='starting_position',
            field=models.PositiveIntegerField(verbose_name='Position de départ'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fabrication_year',
            field=models.PositiveIntegerField(verbose_name='Année de fabrication'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=100, verbose_name='Modèle'),
        ),
    ]