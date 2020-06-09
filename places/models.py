from django.db import models


class Place(models.Model):
    title = models.CharField("Название экскурсии", max_length=200, db_index=True)
    description_short = models.CharField("Короткое описание", max_length=500)
    description_long = models.TextField("Длинное описание")
    longitude = models.DecimalField("Долгота", max_digits=16, decimal_places=14)
    latitude = models.DecimalField("Широта", max_digits=16, decimal_places=14)

    def __str__(self):
        return self.title
