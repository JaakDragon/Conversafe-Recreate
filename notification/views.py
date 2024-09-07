from django.shortcuts import render
# from notifications.signals import notify
from django.http import HttpResponse
from notification.utils import deleteNotif as delNotif
# from notifications.models import Notification
# Create your views here.

def deleteNotif(request):
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        try:
            # notification = Notification.objects.get(pk=notification_id)
            # notification.delete()
            delNotif(request.user,notification_id)
            return HttpResponse("Success")
        except Exception as E:
            print(E)
            return HttpResponse("Notification not found")
    else:
    	# pass
        return HttpResponse("Not allowed", status=405)
