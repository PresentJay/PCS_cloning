from django.shortcuts import render
from django.views import View
from classes import models as class_models
from pracs import models as prac_models
from . import models

# Create your views here.


def login(request):
    pass


def main_views(request):

    all_classes = class_models.Class.objects.all()
    all_pracs = prac_models.Prac.objects.all()

    return render(
        request, "home.html", context={"classes": all_classes, "pracs": all_pracs}
    )

