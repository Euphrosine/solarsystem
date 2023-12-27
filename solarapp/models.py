from django.db import models


class SolarData(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    fixed = models.FloatField()
    tracking = models.FloatField()
    
    def __str__(self):
        return f"SolarData - {self.datetime}"