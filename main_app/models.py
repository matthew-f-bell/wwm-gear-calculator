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

class Weapons(models.Model):
    weapon_name = models.CharField(max_length=100)
    weapon_type = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['weapon_name', 'weapon_type']

    def __str__(self):
        return self.weapon_name
    
class Tank(models.Model):
    tank_title = models.CharField(max_length=100)
    tank_stats = models.ManyToManyField(Stats, related_name='tank_stats')
    tank_weapon = models.ManyToManyField(Weapons, related_name='tank_weapon')

    REQUIRED_FIELDS = ['tank_title', 'tank_stats', 'tank_weapon']

    def __str__(self):
        return self.tank_title
    
class DPS(models.Model):
    dps_title = models.CharField(max_length=100)
    dps_stats = models.ManyToManyField(Stats, related_name='dps_stats')
    dps_weapon = models.ManyToManyField(Weapons, related_name='dps_weapon')

    REQUIRED_FIELDS = ['dps_title', 'dps_stats', 'dps_weapon']

    def __str__(self):
        return self.dps_title
