from django.db import models

# Create your models here.

class CalendarEv(models.Model):
    date = models.DateField()
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    
    def __str__(self):
        return f"{self.year} {self.month} {self.day}"