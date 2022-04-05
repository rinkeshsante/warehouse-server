from django.db import models


class Bot(models.Model):
    reg_id = models.CharField(primary_key=True, max_length=20)
    weight_capacity_in_Kg = models.FloatField()
    location_X = models.IntegerField()
    location_Y = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.reg_id}"
