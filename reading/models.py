from django.db import models
import datetime

# Create your models here.
class Meeting(models.Model):
    name = models.CharField('Name',max_length=32)
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date1 = models.DateField('Date', default=datetime.date.today)
    note = models.CharField('Note',max_length=32,null=True,blank=True)
    
    class Meta:
        unique_together = ('name', 'date1')
