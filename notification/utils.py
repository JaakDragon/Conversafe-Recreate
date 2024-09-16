# Importing Notification Model
from .models import Notification

# Utility functions for usage in other apps
def notify(user,title,desc,url=""):
	a=Notification.objects.create(user=user,title=title,message=desc,url=url)
	a.save()

def deleteNotif(user,pid):
	notif=Notification.objects.get(uniqueID=pid,user=user)
	notif.delete()

def notifs(user):
	a=Notification.objects.filter(user=user,is_read=False)
	return a

def notifCount(user):
	unread=Notification.objects.filter(is_read=False,user=user).count()
	return unread
