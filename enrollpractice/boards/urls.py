from django.urls import path
from . import views
urlpatterns = [
    path("",views.waitBoard,name="waitBoard"),
    path("enrollBoard/",views.enrollBoard,name="enrollBoard"),
    path("enroll",views.enroll,name="enroll"),
    path("rankingBoard/",views.rankingBoard,name="rankingBoard"),
]
