from django.db import models



class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    weight = models.FloatField(default=0)

    def __str__(self):
        return self.vin

