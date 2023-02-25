from django.db import models


class Languages(models.Model):
    language_names = models.TextField(max_length=1000)

    def __repr__(self):
        return f"Языки: {self.language_names}"


class Country(models.Model):
    country = models.CharField(max_length=100)
    language = models.ManyToManyField(to=Languages)

    def __repr__(self):
        return f"Страна: {self.country} | {self.language}"
