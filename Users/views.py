from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.


class testView(View):
    def test(self, request):
        
        user = models.Users.objects.get()
