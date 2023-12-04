from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birthDay = models.DateField()
    
    def __str__(self):
        return f"{self.name} {self.username}"