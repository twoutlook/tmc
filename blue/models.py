from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField('Name',max_length=32,unique=True)
    group= models.CharField('Group',max_length=32)
    def __str__(self):
        return self.name
      
class Task(models.Model):
    task_id = models.IntegerField(unique=True)
    event_id = models.IntegerField()
    department= models.CharField(max_length=32,default='---')
    work_no = models.IntegerField()
    work_name= models.CharField(max_length=32,default='---')
    status= models.CharField(max_length=32,default='---')
    
    # start_time = models.DateTimeField(blank=True,null=True)
    # end_time = models.DateTimeField(blank=True,null=True)
    description= models.CharField(max_length=100,blank=True,null=True)
    reason= models.CharField(max_length=100,blank=True,null=True)
    improvement= models.CharField(max_length=100,blank=True,null=True)
    deal_type= models.CharField(max_length=32,blank=True,null=True)
    
    def __str__(self):
        return str(self.task_id)
     
      