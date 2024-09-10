from django.urls import path
from . import consumers

# Websocket route for AI chat connectivity
websocket_url_patterns=[path('ws/ai/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
						]
