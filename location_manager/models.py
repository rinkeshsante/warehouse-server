from django.db import models


class LoactionManger(models.Model):
    postal_address = models.IntegerField(unique=True)

    location_X = models.IntegerField()
    location_Y = models.IntegerField()

    is_full = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.postal_address},{self.is_full}"
