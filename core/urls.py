from django.urls import path
from users import views as user_views
from pracs import views as prac_views

app_name = "core"

urlpatterns = [path("", user_views.main_views, name="home")]

