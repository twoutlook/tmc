from django.db import models
import datetime
# class Data1(models.Model):
#     date1 = models.DateField()
#     place = models.CharField(max_length=100)
#     worker = models.CharField(max_length=100)
#     thing = models.CharField(max_length=100)

class Data2(models.Model):
    ROLE_CHOICES = [
        ('Attendance', 'Attendance'),
        ('Ah-counter', 'Ah-counter'),
        ('GE', 'GE'),
        ('Grammarian', 'Grammarian'),
        ('IE', 'IE'),
        ('Speaker', 'Speaker'),
        ('TME', 'TME'),
        ('TT Speaker', 'TT Speaker'),
        ('TT Evaluator', 'TT Evaluator'),
        ('TT-master', 'TT-master'),
        ('Timer', 'Timer'),
    ]

    MEMBER_CHOICES = [
        ('Member', 'Member'),
        ('Guest', 'Guest'),
    ]

    name = models.CharField(max_length=32)
    member =  models.CharField( 'Member or Guest',choices=MEMBER_CHOICES,max_length=6)
    date1 = models.DateField('Meeting Date', default=datetime.date.today)
    role = models.CharField( 'Meeting Role', choices=ROLE_CHOICES,max_length=32)
    points = models.IntegerField(default=0)
    class Meta:
        unique_together = ('name', 'date1','member','role')
       
        verbose_name ="Meeting"
        verbose_name_plural ="Meeting"

class Club(models.Model):
    name = models.CharField(max_length=32,unique=True)
    fullname = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Person(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=32) # allow same shortname
    fullname = models.CharField(max_length=100) # but not fullname
    is_member = models.BooleanField('Is Member ', default=False)
    member_since = models.DateField('Member Since', null=True, blank=True)
    note = models.CharField(max_length=100, null=True, blank=True) # but not fullname
    
    def __str__(self):
        if self.is_member:
            return self.name +" *"+" ["+self.club.name +"]"
        return self.name +" ["+self.club.name +"]"
                
    class Meta:
        ordering=['-is_member','name']
        # unique_together = ( 'club','name')
      

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
      

class Meeting(models.Model):
   
    club = models.ForeignKey(Club, on_delete=models.CASCADE,default = 1)
    person = models.ForeignKey(Person, on_delete=models.CASCADE,default = 1)
    # name = models.CharField(max_length=32)
    # member =  models.CharField( 'Member or Guest',choices=MEMBER_CHOICES,max_length=6)
    date1 = models.DateField('Meeting Date', default=datetime.date.today)
    # role = models.CharField( 'Meeting Role', choices=ROLE_CHOICES,max_length=32)
    role2 = models.ForeignKey(Role, on_delete=models.CASCADE,default = 12) # NOTE: default is 12 ---
    # points = models.IntegerField(default=0)
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
