# from django.shortcuts import HttpResponse
from json import dumps
from typing import Iterable, Iterator

from django.shortcuts import redirect, render, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from management.middlewares.auth import auth_middleware
from management.models.festdetails import Festevent
from management.models.participants import Participant
from management.models.participants import SignInUser
import random


class Vsitorhome(View):

    def get(self, request):
        festevent = Festevent.objects.all()

        if request.session.get('user_id'):
            return redirect('home')

        data = {
            'festevents': festevent,

        }

        return render(request, 'visitorhome.html', data)

    def post(self, request):
        festevent = Festevent.objects.all()

        if request.session.get('user_id'):
            return redirect('home')

        data = {
            'festevents': festevent,

        }

        return render(request, 'visitorhome.html', data)


class Home(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        register_id = request.POST.get('register')
        user_email_from_session = request.session.get('email')
        user_id_from_session = request.session.get('user_id')

        user = SignInUser.get_signinuser_by_email(user_email_from_session)
        festevent = Festevent.objects.all()
        participats_by_session_email_all = Participant.get_participant_by_email(user_email_from_session)

        participats_event_ids = []
        festival_event_ids = []
        pid_keys = []

        


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

        for j in  festevent:
            festival_event_ids.append(j.id)



        dict_participats_ids = {
             'dparticipats_ids': participats_event_ids,
             'dfestevent_ids': festival_event_ids
        }

        request.session['participats_event']  = dict_participats_ids

        #participats_event_ids = participats_event_ids.__add__(festival_event_ids)




        '''
         finding intersection between two lists
                  L1 = [2,3,4]
                  L2 = [1,2]
                  ans = [i for i in L1 if i in L2]
                  ans is [2]
                 
        
        '''

        print('pppppppp', abc, participats_event_ids, festival_event_ids)

        # festevent = Festevent.objects.filter(id=3)

        '''
        jsdata = [
            ["Laugh", "Cry"],
            ["Even", "Odd"],
            ["Hot", "Cold"],
            ["Light", "Dark"],
            ["Opposite", "Same"],
            ["Far", "Near"],
            ["Give", "Take"],
            ["Night", "Day"],
            ["Import", "Export"],
            ["Hard", "Easy"],
            ["Never", "Always"],
            ["Late", "Early"],
            ["Less", "More"],
            ["Male", "Female"],
            ["Happiness", "Sadness"],
            ["Fast", "Slow"],
            ["Old", "Young"],
            ["Boy", "Girl"],
            ["Up", "Down"],
            ["Left", "Right"],
            ["Rich", "Poor"],
            ["Love", "Hate"],
            ["Inside", "Outside"],
            ["Bad", "Good"],
            ["Short", "Tall"],
        ]
        jsdata = dumps(jsdata)
        '''

        data = {
            'festevents': festevent,
            'user_email_from_session': user_email_from_session,
            'user_id_from_session': user_id_from_session,
            'participats_event_idss': participats_event_ids,
            'abcs': abc,
            'user': user
            #'jsdatas': jsdata
        }

        return render(request, 'home.html', data)

    def post(self, request):

        register_id = request.POST.get('register')
        user_email_from_session = request.session.get('email')
        user_id_from_session = request.session.get('user_id')

        user = SignInUser.get_signinuser_by_email(user_email_from_session)
        festevent = Festevent.objects.all()
        event_name = Festevent.get_festival_by_id(register_id)
        participate = Participant.get_participant_by_email(user_email_from_session)
        # ch = Participant.objects.filter(event_name=register_id)
        # print('affffaffff', ch)

        if register_id:
            if user_id_from_session:
                reg = Participant(first_name=user.first_name,
                                  last_name=user.last_name,
                                  email=user.email,
                                  phone=user.phone,
                                  password=user.password,
                                  event_name=event_name
                                  )
                reg.register()
                return HttpResponse(' reg sucsess')

        # festevent = Festevent.objects.filter(id=3)

        data = {
            'festevents': festevent,
            'uemail': user_email_from_session,
            'id': user_id_from_session
        }

        return render(request, 'home.html', data)
