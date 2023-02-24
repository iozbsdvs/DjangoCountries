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


def get_country(request, id):
    countries = Country.objects.get(id=id)

    context = {
        "countries": countries,
    }

    return render(request, 'country-page.html', context)

