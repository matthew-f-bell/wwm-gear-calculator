from django.db import models

# Create your models here.
class Stats(models.Model):
    stat_name = models.CharField(max_length=100)
    stat_value = models.FloatField()
    max_stat_value = models.FloatField()
    stat_weight = models.FloatField()

    REQUIRED_FIELDS = ['stat_name', 'stat_value', 'max_stat_value', 'stat_weight']

    def __str__(self):
        return self.stat_name