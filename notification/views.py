from django.shortcuts import render
from django.http import HttpResponse
from notification.utils import deleteNotif as delNotif

# Deletes a particular notification given its id
def deleteNotif(request):
	if request.method == 'POST':
		notification_id = request.POST.get('notification_id')
		try:
			delNotif(request.user,notification_id)
			return HttpResponse("Success")
		except Exception as E:
			print(E)
			return HttpResponse("Notification not found")
	else:
		return HttpResponse("Not allowed", status=405)
