from django.urls import path

from audio_score.views import r_ping

urlpatterns = [
    path('ping', r_ping)
]
