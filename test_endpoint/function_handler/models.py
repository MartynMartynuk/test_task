from django.db import models


class A(models.Model):
    value = models.FloatField()
    color = models.CharField()


class B(models.Model):
    function = models.CharField()
    value = models.FloatField()


class C(models.Model):
    value = models.JSONField()