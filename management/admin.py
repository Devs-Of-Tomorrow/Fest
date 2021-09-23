from django.contrib import admin
from management.models.participants import SignInUser, Participant, Parti

from .models.festdetails import Festevent, FestAccomodation, Sponsors


# Register your models here.

'''class AdminParticipant(admin.ModelAdmin):
    #list_display = ['participant']
'''


class AdminSignInUser(admin.ModelAdmin):
    list_display = ['first_name']


class AdminFestevent(admin.ModelAdmin):
    list_display = ['eventname']


class AdminParticipant(admin.ModelAdmin):
    list_display = ['first_name', 'event_name']

class AdminSponsors(admin.ModelAdmin):
    
     class Meta:
         model = Sponsors
         fields = '__all__'




admin.site.register(Participant, AdminParticipant)
admin.site.register(SignInUser, AdminSignInUser)
admin.site.register(Festevent, AdminFestevent)
admin.site.register(Parti)
admin.site.register(FestAccomodation)
admin.site.register(Sponsors, AdminSponsors)



