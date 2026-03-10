from django.db import models

# Create your models here.
class Stats(models.Model):
    stat_name = models.CharField(max_length=100)
    stat_value = models.FloatField(default=0.0)
    max_stat_value = models.FloatField()
    stat_weight = models.FloatField()
    stat_rank = models.IntegerField(default=0)

    REQUIRED_FIELDS = ['stat_name', 'stat_value', 'max_stat_value', 'stat_weight']

    def __str__(self):
        return self.stat_name
    





















































































class Healer(models.Model):
    healer_title = models.CharField(max_length=100)
    healer_stats = models.ManyToManyField(Stats, related_name='healer_stats')
    healer_weapon = models.ManyToManyField(Weapons, related_name='healer_weapon')

    def __str__(self):
        return self.healer_title