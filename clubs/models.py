from django.db import models
import datetime

class Club(models.Model):
    name = models.CharField(max_length=32,unique=True)
    fullname = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Person(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=32) # allow same shortname
    lastname = models.CharField(max_length=32,default='---') # allow same shortname
    firstname = models.CharField(max_length=32,default='---') # allow same shortname
    member_type = models.CharField(max_length=32,default='---') # allow same shortname
    fullname = models.CharField(max_length=100) # but not fullname
    is_member = models.BooleanField('Is Member ', default=False)
    member_num = models.CharField(max_length=32,default='---') # allow same shortname
    email = models.EmailField(max_length=70,null=True,blank=True)
    phone = models.CharField(max_length=11,default='---') # allow same shortname
    member_since = models.DateField('Member Since', null=True, blank=True)
    note = models.CharField(max_length=100, null=True, blank=True) # but not fullname
    officer = models.CharField(max_length=20, null=True, blank=True) # but not fullname
    sponsor_mentor = models.CharField(max_length=10, null=True, blank=True) # but not fullname
    teamleader = models.CharField(max_length=10, null=True, blank=True) # but not fullname
    teamnote = models.CharField(max_length=100, null=True, blank=True) # but not fullname
    
    def __str__(self):
        if self.is_member:
            return self.name +" *"+" ["+self.club.name +"]"
        return self.name +" ["+self.club.name +"]"
                
    class Meta:
        ordering=['club','name']
        unique_together = ( 'club','name')
      

class Role(models.Model):
    name = models.CharField(max_length=32,unique=True) 
    fullname = models.CharField(max_length=100,unique=True) 
    def __str__(self):
        return self.name



class ClubDate(models.Model):
    date1 = models.DateField('Meeting Date', default=datetime.date.today)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    note = models.CharField(default='---',max_length=32)
    
    class Meta:
        unique_together = ( 'date1','club')
      
# https://stackoverflow.com/questions/11508744/django-models-filter-by-foreignkey
class Meeting(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    persontxt = models.CharField('Name',max_length=32,null=True,blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date1 = models.DateField('Date', default=datetime.date.today)
    role2 = models.ForeignKey(Role, on_delete=models.CASCADE,verbose_name='Role') # NOTE: default is 12 ---
    
    class Meta:
        unique_together = ('person', 'date1','role2')
       
        # verbose_name ="Meeting V2"
        # verbose_name_plural ="Meeting V2"



class Best(models.Model):
    BEST_CHOICES = [
        ('tt', 'tt'),
        # ('Guest', 'Guest'),
    ]
    date1 = models.DateField()
    title = models.CharField(choices=BEST_CHOICES,default='tt',max_length=32)
    name = models.CharField(max_length=32)
    class Meta:
        unique_together = ( 'date1','title')
       
        verbose_name ="Meeting Best"
        verbose_name_plural ="Meeting Best"
