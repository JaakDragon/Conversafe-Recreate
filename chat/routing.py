from django.urls import path
from . import consumers

# Websocket route for chat connectivity
websocket_url_patterns=[path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
						]
