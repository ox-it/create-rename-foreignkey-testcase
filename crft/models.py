from django.db import models

class Star(models.Model):
    pass

class Planet(models.Model):
    star = models.ForeignKey(Star)

