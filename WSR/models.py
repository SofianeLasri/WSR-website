import datetime

from django.db import models

class Saison(models.Model):
    nom = models.CharField(max_length=100)
    annee = models.PositiveIntegerField(verbose_name="Année")

    def __str__(self):
        return self.nom


class Pilote(models.Model):
    nom = models.CharField(max_length=100)
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE, verbose_name="Véhicule")

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100, verbose_name="Modèle")
    annee_fabrication = models.PositiveIntegerField(verbose_name="Année de fabrication")

    def __str__(self):
        return f"{self.marque} {self.modele}"


class Course(models.Model):
    class TypeCourse(models.TextChoices):
        INVITATION = "invitation"
        CHAMPIONNAT = "championnat"
        COURSE_SIMPLE = "course_simple"

    nom = models.CharField(max_length=100)
    circuit = models.CharField(max_length=100)
    saison = models.ForeignKey(Saison, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course_images', verbose_name="Image d'illustration")
    type = models.CharField(max_length=100, choices=TypeCourse.choices, default=TypeCourse.COURSE_SIMPLE)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Resultat(models.Model):
    pilote = models.ForeignKey(Pilote, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    position_arrivee = models.PositiveIntegerField(verbose_name="Position à l'arrivée")
    position_depart = models.PositiveIntegerField(verbose_name="Position de départ")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.pilote} - {self.course}"


class Participation(models.Model):
    saison = models.ForeignKey(Saison, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pilotes = models.ManyToManyField(Pilote)

    def __str__(self):
        return f"{self.saison} - {self.course}"
