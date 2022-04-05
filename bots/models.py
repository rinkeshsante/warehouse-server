from django.db import models


class Bot(models.Model):
    reg_id = models.CharField(max_length=20, default="NA")
    weight_capacity_in_Kg = models.FloatField()
    location_X = models.IntegerField()
    location_Y = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} {self.reg_id}"
