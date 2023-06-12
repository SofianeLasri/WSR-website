# Generated by Django 4.2.2 on 2023-06-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WSR', '0013_alter_race_circuit_alter_race_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='circuit',
            field=models.CharField(choices=[('Pacfic Way', 'Pacific Way'), ('Marina City', 'Marina City'), ('Boucle Art Deco', 'Art Deco'), ('Ocean Drive', 'Ocean Drive'), ('Lake Shore Point', 'Lake Shore Point'), ('Le Trocadéro', 'Trocadero'), ('Boucle de la fontaine', 'Fontaine'), ('Route de la corniche', 'Corniche'), ('Baie de colombe', 'Colombe Bay'), ('Champs Elysées', 'Champs Elysees'), ('Villefranche-sur-mer', 'Villefranche'), ('Liveroutes', 'Liveroutes'), ('La turbie', 'Turbie'), ('Ap Lei Chau', 'Ap Lei Chau'), ('Route des Toriis', 'Torris'), ('Pok Fu Lam', 'Pok Fu Lam'), ('Col Sakura', 'Sakura'), ('Boucle du quai Orra', 'Orra Loop'), ('Voie Hattan', 'Hattan Way'), ('Belvédère de Nakheel', 'Nakheel')], max_length=100),
        ),
    ]