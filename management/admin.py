from django.contrib import admin
from management.models.participants import Participants
# Register your models here.


class AdminParticipant(admin.ModelAdmin):
    list_display = ['first_name']


admin.site.register(Participants, AdminParticipant)
