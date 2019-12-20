from django.db import models

# Create your models here.
class Ticket(models.Model):
    seq = models.IntegerField(default = 0)
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=11)
    clubtxt = models.CharField(max_length=100)
    club = models.CharField(max_length=100,default='---')
    note = models.CharField(max_length=100)
    feetxt = models.CharField(max_length=100)
    stattxt = models.CharField(max_length=100)
    dt = models.DateTimeField()
    def __str__(self):
        return self.name