from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.


def login(request):
    pass


def main_views(request):
    # all_classes = models.Class.objects.all()
    # all_pracs = models.Prac.objects.all()

    return render(
        request, "home.html" #, context={"classes": all_classes, "pracs": all_pracs}
    )

