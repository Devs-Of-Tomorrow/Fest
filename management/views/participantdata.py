from management.models.participants import Participant, SignInUser
from django.shortcuts import render,redirect
from django.views import View
from management.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Participantdata(View):
    def post(self, request):
        return render(request, 'home.html')


def profile(request):
    user_email_from_session = request.session.get('email')
    user_id_from_session = request.session.get('user_id')

    signin_user_data = SignInUser.objects.filter(email=user_email_from_session).first()
    participant_data = Participant.objects.filter(email=user_email_from_session)

    participats_by_session_email_all = Participant.get_participant_by_email(user_email_from_session)

    participats_event_ids = []

    try:
            for i in participats_by_session_email_all:
                participats_event_ids.append(i.event_name.id)
                print('part', type(i.event_name.id), i.event_name.id)
    except:
            try:
                participats_event_ids = Participant.objects.all()
                print('aaaa',participats_event_ids)
                participats_event_ids = [participats_event_ids[0].event_name.id]
            except: participats_event_ids = []    

    abc = participats_by_session_email_all
    participats_event_ids.sort() 

   
    return render(request, 'profile.html')


