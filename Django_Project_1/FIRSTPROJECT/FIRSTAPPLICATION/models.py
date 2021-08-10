from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    address=models.TextField(blank=True)

    def __str__(self):
        return self.name


