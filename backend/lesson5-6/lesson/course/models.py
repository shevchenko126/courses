from django.db import models


class Subject(models.Model):
    name = models.CharField(verbose_name="Имя")
