
# Club


# Person
- 任何入必需屬於某個club, 有可能是 member or guest
  - 這個人在這 club 雖然是 geust，但是在別的 club 可能是 member
  - 先有一個供每個 club 各自運行的領域，跨 club 的關係先不在這階段實現。

# Role
- 

# Meeting
- Club
- Date
- Person
- Role 
  - possible for one person to take multiple roles




```
class Person(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE,default=1)
    
    name = models.CharField(max_length=32) # allow same shortname
    fullname = models.CharField(max_length=100) # but not fullname
    is_member = models.BooleanField('Is Member ', default=False)
    member_since = models.DateField('Member Since', null=True, blank=True)
    note = models.CharField(max_length=100, null=True, blank=True) # but not fullname
```   
