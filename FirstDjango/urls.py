from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('countries', views.countries_list, name='countries-list'),
    path('languages', views.languages_list, name='languages-list'),
    path('country-page/<int:id>', views.get_country, name='country-page'),
    path('language-page/<int:id>', views.get_language, name='language-page'),

]
