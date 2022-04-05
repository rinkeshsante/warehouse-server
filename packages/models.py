from django.db import models


class Package(models.Model):
    postal_code = models.IntegerField(unique=True)
    date_of_arrival = models.DateTimeField(auto_now_add=True)

    location_X = models.IntegerField()
    location_Y = models.IntegerField()

    # destination_X = models.IntegerField()
    # destination_Y = models.IntegerField()

    done_processing = models.BooleanField(False)

    def __str__(self) -> str:
        return f"{self.id}->{self.postal_code},{self.done_processing}"
