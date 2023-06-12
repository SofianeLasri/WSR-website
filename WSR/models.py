import datetime

from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(verbose_name="Year")

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name="Vehicle")

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100, verbose_name="Model")
    fabrication_year = models.PositiveIntegerField(verbose_name="Fabrication Year")

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

    class RaceParticipationType(models.TextChoices):
        INVITATION = "invitation"
        PARTICIPATION = "participation"

    location = models.CharField(max_length=100)
    circuit = models.CharField(max_length=100)
    finishing_position = models.PositiveIntegerField(verbose_name="Finishing Position")
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='race_images', verbose_name="Illustration Image")
    type = models.CharField(max_length=100, choices=RaceType.choices, default=RaceType.SINGLE_RACE)
    participation_type = models.CharField(
        max_length=100,
        choices=RaceParticipationType.choices,
        default=RaceParticipationType.PARTICIPATION
    )
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Result(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    finishing_position = models.PositiveIntegerField(verbose_name="Finishing Position")
    starting_position = models.PositiveIntegerField(verbose_name="Starting Position")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.driver} - {self.race}"


class Participation(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return f"{self.season} - {self.race}"

