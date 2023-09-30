from django.db import models

# Create your models here.
class Puzzle(models.Model):
    nounce   = models.PositiveIntegerField()
    solution = models.CharField(max_length=250)
    level    = models.PositiveIntegerField()
    data     = models.CharField(max_length=250)
    
    
    def __str__(self):
        return f'{self.data} level: {self.level}'