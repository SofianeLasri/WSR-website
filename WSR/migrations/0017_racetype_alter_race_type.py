from django.db import migrations, models


def create_race_types(apps, schema_editor):
    Race = apps.get_model('WSR', 'Race')
    RaceType = apps.get_model('WSR', 'RaceType')

    race_types = set([race.type for race in Race.objects.all()])

    with schema_editor.connection.cursor() as cursor:
        for race_type in race_types:
            instance, created = RaceType.objects.get_or_create(name=race_type)
            if created:
                instance.description = "Description du type de course"
                instance.save()

            cursor.execute(
                "UPDATE WSR_race SET type = %s WHERE type = %s",
                [instance.id, race_type]
            )


class Migration(migrations.Migration):
    dependencies = [
        ('WSR', '0016_vehicle_image_alter_driver_vehicle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('font_awesome_icon', models.CharField(blank=True, default='', max_length=64)),
                ('image',
                 models.ImageField(blank=True, default='', upload_to='racetypes', verbose_name="Image d'illustration")),
            ],
        ),
        migrations.RunPython(create_race_types),
        migrations.AlterField(
            model_name='race',
            name='type',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='WSR.RaceType'),
        ),
    ]
