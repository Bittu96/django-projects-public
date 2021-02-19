from django.db import models
from . import literals


class Thing (models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    stat_one = models.CharField(max_length=2, default=literals.STAT_ONE_CHOICE_NOT_SPECIFIED)
    stat_two = models.CharField(max_length=1, default=literals.STAT_TWO_CHOICE_NOT_SPECIFIED)

    def __str__(self):
        return self.code

class Item (models.Model):
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    rating = models.CharField(max_length=3)
    score = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
