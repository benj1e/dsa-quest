from django.urls import path
from .views import *

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("problem_list/", problem_list, name="problem_list"),
    path("problem_list/<str:name>", problem_detail, name="problem_detail"),
]
