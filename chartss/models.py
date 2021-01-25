from django.db import models

# Create your models here.

  
class City(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()
  
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'myapp'