import datetime

from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(verbose_name="Year")

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name="Véhicule")

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, verbose_name="Modèle")
    fabrication_year = models.PositiveIntegerField(verbose_name="Année de fabrication")
    image = models.ImageField(upload_to='vehicles', default="", blank=True, verbose_name="Image d'illustration")

    def __str__(self):
        return f"{self.brand} {self.model}"


class Race(models.Model):
    class RaceType(models.TextChoices):
        CHAMPIONSHIP = "championship"
        SINGLE_RACE = "single_race"
        FACE_TO_FACE = "face_to_face"
        OVERTAKING = "overtaking"
        AGAINST_TIME = "against_time"
        ELIMINATION = "elimination"
        ENDURANCE = "endurance"
        TOUGE = "touge"
        CHECKPOINT = "checkpoint"
        DRIFT = "drift"

    class RaceParticipationType(models.TextChoices):
        INVITATION = "invitation"
        PARTICIPATION = "participation"

    class Locations(models.TextChoices):
        CALIFORIA = "Californie"
        CHICAGO = "Chicago"
        MIAMI = "Miami"
        PARIS = "Paris"
        BARCELONA = "Barcelone"
        COT = "Côte d'Azur"
        HONG_KONG= "Hong Kong"
        OKUTAMA = "Okutama"
        DUBAI = "Dubaï"
        YAS_MARINA = "Yas Marina"

    class Circuits(models.TextChoices):
        PACIFIC_WAY = "Pacfic Way"
        MARINA_CITY = "Marina City"
        ART_DECO = "Boucle Art Deco"
        OCEAN_DRIVE = "Ocean Drive"
        LAKE_SHORE_POINT = "Lake Shore Point"
        TROCADERO = "Le Trocadéro"
        FONTAINE = "Boucle de la fontaine"
        CORNICHE = "Route de la corniche"
        COLOMBE_BAY = "Baie de colombe"
        CHAMPS_ELYSEES = "Champs Elysées"
        VILLEFRANCHE = "Villefranche-sur-mer"
        LIVEROUTES = "Liveroutes"
        TURBIE = "La turbie"
        AP_LEI_CHAU = "Ap Lei Chau"
        TORRIS = "Route des Toriis"
        POK_FU_LAM = "Pok Fu Lam"
        SAKURA = "Col Sakura"
        ORRA_LOOP = "Boucle du quai Orra"
        HATTAN_WAY = "Voie Hattan"
        NAKHEEL = "Belvédère de Nakheel"
        CIRCUIT_GP = "Circuit GP"

    location = models.CharField(max_length=100, choices=Locations.choices)
    circuit = models.CharField(max_length=100, choices=Circuits.choices)
    finishing_position = models.PositiveIntegerField(verbose_name="Position d'arrivée")
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='race_images', verbose_name="Image d'illustration")
    type = models.CharField(max_length=100, choices=RaceType.choices, default=RaceType.SINGLE_RACE)
    participation_type = models.CharField(
        max_length=100,
        choices=RaceParticipationType.choices,
        default=RaceParticipationType.PARTICIPATION
    )
    name = models.CharField(max_length=100, default="", blank=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.participation_type + ' | ' + self.type + ' ' + self.name + ' - ' + self.location + ', ' + self.circuit


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Result(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    finishing_position = models.PositiveIntegerField(verbose_name="Position d'arrivée")
    starting_position = models.PositiveIntegerField(verbose_name="Position de départ")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.driver} - {self.race}"

