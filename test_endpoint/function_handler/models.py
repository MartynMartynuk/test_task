from django.db import models


class A(models.Model):
    value = models.FloatField()
    color = models.CharField(max_length=10)


class B(models.Model):
    function = models.CharField(max_length=10)
    value = models.FloatField()


class C(models.Model):
    value = models.JSONField()