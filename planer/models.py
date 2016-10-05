# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Plan(models.Model):
    user = models.ForeignKey(User, related_name='user')
    title = models.CharField(verbose_name="название", max_length=150)
    start_date = models.DateField(verbose_name="начало")
    end_date = models.DateField(verbose_name="конец")
    destination = models.TextField(verbose_name="куда")
    cash = models.IntegerField(verbose_name="наличные")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'план'
        verbose_name_plural = 'планы'