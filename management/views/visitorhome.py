# from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View


class Vsitorhome(View):

    def get(self, request):
        return HttpResponse("hi visitor")
