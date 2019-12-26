from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField('Name',max_length=32,unique=True)
    group= models.CharField('Group',max_length=32)
    def __str__(self):
        return self.name
      
class Market(models.Model):
    dt = models.DateField('Date')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    p1= models.DecimalField('Low Price',max_digits=5, decimal_places=2)
    p2= models.DecimalField('High Price',max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.flower.name
     
    class Meta:
        unique_together = ( 'dt','flower')
      