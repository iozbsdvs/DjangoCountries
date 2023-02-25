from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

from MainApp.models import Country, Languages


def welcome(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()

    context = {
        "countries": countries
    }

    return render(request, 'countries-list.html', context)


def languages_list(request):
    languages = Languages.objects.all()

    context = {
        "languages": languages
    }

    return render(request, 'languages-list.html', context)


def get_country(request, id):
    countries = Country.objects.get(id=id)
    language = Languages.objects.all()
    languages = language.filter(country=id)

    context = {
        "countries": countries,
        "languages": languages
    }

    return render(request, 'country-page.html', context)


def get_language(request, id):
    languages = Languages.objects.get(id=id)
    country_name = Country.objects.all()
    countries = country_name.filter(language=id)

    context = {
        "countries": countries,
        "languages": languages
    }

    return render(request, 'language-page.html', context)
