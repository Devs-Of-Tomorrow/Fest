from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import TimeField
from .festdetails import Festevent
from django.utils import timezone
from django_extensions.db import fields as extension_fields
from .festdetails import FestAccomodation
from datetime import datetime
# ohmydoggaming@gmail.com

# Create your models here.


class SignInUser(models.Model):
    GENDER_CHOICE = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other')
    )
    first_name = models.CharField(
        max_length=250, default=None
    )
    last_name = models.CharField(
        max_length=250, default=None
    )
    gender = models.CharField(
        max_length=10, default=None,
        blank=True, null=True,
        choices=GENDER_CHOICE
    )
    phone = models.CharField(
        max_length=11, default=None
    )
    email = models.EmailField(
        default=None
    )
    UNIVERSITY_CHOICES = (
        ('mu', 'Mumbai University'),
        ('gtu', 'Gujarat Technological University'),
        ('marwadi', 'Marwadi University'),
        ('atmiya', 'Atmiya University'),
        ('rk', 'RK University'),
        ('others', 'Others')
    )
    universitiy = models.CharField(
        max_length=50,
        blank=True, null=True,
        choices=UNIVERSITY_CHOICES
    ) 
    college = models.CharField(
        max_length=10,
        blank=True, null=True
    )
    password = models.CharField(
        max_length=254, default=None
    )
    profile_image = models.ImageField(
        upload_to='uploads/events/profile_images/', blank=True,
        default = 'uploads/events/profile_images/dummy_boy2.png' , null =True
    )
    date_joined = models.DateTimeField( default=datetime.now())
  
    Terms_and_Conditions = models.BooleanField(
        null=True
    )

    def __str__(self):
        return self.first_name

    def register(self):
        self.save()

    def IsExists(self):
        if SignInUser.objects.filter(email=self.email):
            return True

        return False

    @staticmethod
    def get_signinuser_by_email(email):
        try:
            return SignInUser.objects.get(email=email)
        except:
            return False


class Participant(models.Model):

   

    first_name = models.CharField(
        max_length=250, default=None
    )
    last_name = models.CharField(
        max_length=250, default=None
    )
    phone = models.CharField(
        max_length=11, default=None
    )
    email = models.EmailField(
        default=None
    )
    password = models.CharField(
        max_length=254, default=None
    )
    event_name = models.ForeignKey(
        Festevent, on_delete=models.CASCADE, 
        default=None, blank=True,
        related_name="event"
    )
    participation_code = extension_fields.RandomCharField(
        length=7,
        lowercase=True,
        unique=True
    ) 
    UNIVERSITY_CHOICES = (
        ('mu', 'Mumbai University'),
        ('gtu', 'Gujarat Technological University'),
        ('marwadi', 'Marwadi University'),
        ('atmiya', 'Atmiya University'),
        ('rk', 'RK University'),
        ('others', 'Others')
    )
    universitiy = models.CharField(
        max_length=50,
        blank=True, null=True,
        choices=UNIVERSITY_CHOICES
    ) 
   
    enrolment_number = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    college = models.CharField(
        max_length=10,
        blank=True, null=True
    )
    profile_image = models.ImageField(
        upload_to='uploads/events/profile_images/', blank=True,
        default = None , null =True
    )
    participated = models.BooleanField( null=True)
    winner = models.BooleanField(
        null=True
    )
    place_secured = models.IntegerField(
        blank=True, null=True
    )

    def __str__(self):
        return "{} - {}".format(self.first_name, self.event_name)

    def register(self):
        self.save()

    @staticmethod
    def get_participant_by_email(email):
        try:
            return Participant.objects.filter(email=email)
        except:
            return False

    @staticmethod
    def get_participant_by_id(ids):
        try:
            return Participant.objects.get(id=ids)
        except:
            return False



class Parti(models.Model):
    participated_user = models.ManyToManyField(FestAccomodation, default=None)
    event_participated = models.ManyToManyField(Festevent)


    
    

