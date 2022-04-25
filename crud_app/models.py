from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    ci = models.IntegerField()
    age = models.IntegerField()
    sex = models.IntegerField()

    def __str__(self):
        return self.name
