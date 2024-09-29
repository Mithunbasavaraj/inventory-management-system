from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True,default="")
    quantity = models.PositiveIntegerField(blank=True,default="")

    def __str__(self):
      return self.name