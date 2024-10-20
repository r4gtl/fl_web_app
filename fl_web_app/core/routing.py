# your_app_name/routing.py
from django.urls import path , re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/schede/$', consumers.SchedeConsumer.as_asgi()),
]