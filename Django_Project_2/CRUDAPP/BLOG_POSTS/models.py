from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    pages = models.IntegerField()

    def __str__(self):
        return self.name