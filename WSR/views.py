import markdown
from django.shortcuts import render

from WSR.models import *


# Create your views here.
def home(request):
    three_last_races = Race.objects.order_by('-date')[:3]
    last_race = three_last_races[0]
    last_race_season = last_race.season.name
    last_race_results = Result.objects.filter(race=last_race)

    for race_result in last_race_results:
        race_result.driver_name = race_result.driver.name
        if race_result.finishing_position == 1:
            race_result.pos_string = "1ère"
        else:
            race_result.pos_string = str(race_result.finishing_position) + "ème"

    last_race_details = {
        'race': last_race,
        'season_name': last_race_season,
        'results': last_race_results
    }

    second_frame_races = []

    for race in three_last_races[1:3]:
        pos_string = "1er" if race.finishing_position == 1 else str(race.finishing_position) + "ème"
        race.pos_string = pos_string
        second_frame_races.append(race)

    six_last_articles = Article.objects.order_by('-publication_date')[:6]

    for article in six_last_articles:
        article.summary = ' '.join(article.content.split()[:14]) + '...'

    three_last_races_results = []

    for race in three_last_races:
        results = Result.objects.filter(race=race)
        race_results = {
            'race': race,
            'results': results
        }

        for result in results:
            result.driver_name = result.driver.name
            result.vehicle_brand = result.driver.vehicle.brand
            result.vehicle_model = result.driver.vehicle.model

        three_last_races_results.append(race_results)

    return render(
        request,
        'home.html',
        {
            "last_race_details": last_race_details,
            "second_frame_races": second_frame_races,
            "six_last_articles": six_last_articles,
            "three_last_races_results": three_last_races_results
        }
    )


def articles(request):
    articles = Article.objects.order_by('-publication_date').all()
    for article in articles:
        article.summary = ' '.join(article.content.split()[:14]) + '...'

    return render(
        request,
        'articles.html',
        {
            "articles": articles
        }
    )


def view_article(request, id):
    article = Article.objects.get(id=id)
    md = markdown.Markdown()
    article.content = md.convert(article.content)
    return render(
        request,
        'article.html',
        {
            "article": article
        }
    )


def races_types(request):
    epreuves = RaceType.objects.all()
    md = markdown.Markdown()

    for epreuve in epreuves:
        epreuve.description = md.convert(epreuve.description)

    return render(
        request,
        'race-types.html',
        {
            'epreuves': epreuves
        }
    )


def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(
        request,
        'vehicles.html',
        {
            'vehicles': vehicles
        }
    )


def seasons(request):
    return None
