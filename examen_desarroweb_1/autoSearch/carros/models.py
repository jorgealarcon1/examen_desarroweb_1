# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
import os

# Create your models here.
class Car(models.Model):
    #relacion
    #user = models.ForeignKey(settings.AUTH_USER_MODEL)
    make = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    year = models.DateField(max_length=100)
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.make)
