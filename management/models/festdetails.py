from django.db import models
from datetime import datetime


# from .participants import SignInUser
# Create your models here.


class Festevent(models.Model):
    eventname = models.CharField(
        max_length=255, default=None
    )
    image = models.ImageField(
        upload_to='uploads/events/event_logo', 
        default=None, blank=True
    )
    fees = models.CharField(
        max_length=4, default=None
    )
    eventdescription = models.TextField(
        max_length=1000, 
        default=None, null=True, blank=True
    )
    EVENT_TYPE_CHOICES = (
        ('Technical', 'Technical'),
        ('Non-technical', 'Non-Technical'),
        ("Cultural", "Cultural"), 
        ("Management", "Management")
    )
    event_type = models.CharField(
        max_length=50,
        blank = True, null = True,
        choices = EVENT_TYPE_CHOICES
    )
    
    VENUE_CHOICES =(
        ('Patkar College 😒', 'Patkar College 😒'),
        ('Bhavan\'s College 😌', 'Bhavan\'s College 😌'),
        ('Virtual', 'Virtual'),
        
    ) 
    venue = models.CharField(
        max_length=30,
        choices=VENUE_CHOICES,
        default='2', null=True
    )
    PARTICIPATION_TYPE_CHOICES = (
        ('👱🏻Individual', ' 👱🏻 Individual'),
        ('👨‍👩‍👦Team', '👨‍👩‍👦Team ')
    )
    participation_type = models.CharField(
        max_length=50,
        blank=True, null=True,
        choices=PARTICIPATION_TYPE_CHOICES
    )
    min_participants = models.IntegerField(
        default=1, null=True
    )
    max_participants = models.IntegerField(
        default=4,  null=True
    )
    prize = models.IntegerField(
        default=None, blank=True,
        null=True
    )
    EVENT_ON_DAY_CHOICE = (
        ('1', 'Day 1️⃣'),
        ('2', 'Day 2️⃣'),
        ('3', 'Day 3️⃣'),
        ('4', 'Day 4️⃣'),
        ('5', 'Day 5️⃣'),
        ('6', 'Day 6')
    )
    event_on_day = models.CharField(
        default='Choose Day', max_length=20,
        blank=True, choices=EVENT_ON_DAY_CHOICE
    )
    time = models.TimeField(
        default='12:00:00'
    )
    date = models.DateTimeField(
        default=datetime.now
    )
    
    COORDINATORS_CHOICES = (
        ('Amir', 'Amir'),
        ('Roshith', 'Roshith')
    )
    coordinators = models.CharField(
        max_length=50,
        blank=True, null=True, default=None,
        choices = COORDINATORS_CHOICES
    )
    contact_name1 = models.CharField(
        max_length=30, 
        default="", blank=True, null=True
    )
    contact_phone1 = models.CharField(
        max_length=12,
        blank=True , default=None, null=True
    )
    contact_email1 = models.EmailField(
        default="", blank=True 
    )
    contact_image1 = models.ImageField(
        upload_to='uploads/events/event_contact/', 
        blank=True , default=None, null = True
    )
    contact_name2 = models.CharField(
        max_length=30, default="", 
        blank=True, null=True
    )
    contact_phone2 = models.CharField(
        max_length=12,
        blank=True, default=None, null=True
    )
    contact_email2 = models.EmailField(
        default="", blank=True, null=True
    )
    contact_image2 = models.ImageField(
        upload_to='uploads/events/event_contact/', blank=True,
        default = None , null =True
    )
    sponsor1 = models.ImageField(upload_to='uploads/events/events_sponsors/', blank=True)
    sponsor2 = models.ImageField(upload_to='uploads/events/events_sponsors/', blank=True)
    sponsor3 = models.ImageField(upload_to='uploads/events/events_sponsors/', blank=True)
    sponsor4 = models.ImageField(upload_to='uploads/events/events_sponsors/', blank=True)
    sponsor5 = models.ImageField(upload_to='uploads/events/events_sponsors/', blank=True)
    one_liner = models.CharField(max_length=200, blank=True, null=True, default="")

    
    def __str__(self):
        return self.eventname

    @staticmethod
    def get_festival_by_id(ids):
        try:
            return Festevent.objects.get(id=ids)
        except:
            return False


    
class FestAccomodation(models.Model):
    day1 = models.BooleanField()
    day2 = models.BooleanField()
    day3 = models.BooleanField()
    day4 = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()


class Sponsors(models.Model):
    choice = (("1", "Title Sponsor"), ("2", "Online Media Sponsors"), ("3", "Normal Sponsor"), ("4", "Event Sponsor"))
    type = models.CharField(max_length=20, choices=choice, blank=True)
    name = models.CharField(max_length=30, default="", blank=True)
    name_shown = models.CharField(max_length=30, default="", blank=True)
    image = models.ImageField(upload_to='uploads/events/sponsors/', blank=True)
    url = models.URLField(default="",blank=True)

    class Meta:
        verbose_name_plural = "Sponsors"

    def __str__(self):
        return self.name
   
    

    # signinuser = models.ForeignKey(SignInUser, on_delete=models.CASCADE, default=None)



