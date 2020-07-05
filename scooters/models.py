from django.db import models


class Scooter(models.Model):
    status = models.CharField(max_length=50, blank=False)
    current_speed = models.IntegerField(default=0)
    current_battery = models.IntegerField(default=100)
