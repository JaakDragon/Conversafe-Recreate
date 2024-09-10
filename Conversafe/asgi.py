"""
ASGI config for Conversafe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
########## Libraries and Stuff ################################################
import os # For Environment variable access
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing  # For Normal chatting (websockets) routes
import AIChat.routing # For AI chatting (websockets) routes
from django.core.asgi import get_asgi_application
###########################################################################

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Conversafe.settings')

application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	'websocket':AuthMiddlewareStack(
		URLRouter(
			chat.routing.websocket_url_patterns +
			AIChat.routing.websocket_url_patterns
			
			)
		)
})
