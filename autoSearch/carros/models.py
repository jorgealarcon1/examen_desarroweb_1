# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.
class Car(models.Model):
    #relacion
    make = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    year = models.DateField(auto_now_add = False)
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.make)
