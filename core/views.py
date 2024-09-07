from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from landing import models
from .models import UserProfile
from landing.models import AUser
from friends.models import *
# from notifications.signals import notify
from notification.utils import *

@login_required(login_url="login")
def home(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/dashboard.html",context)

@login_required(login_url="login")
def profile(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/profile.html",context)

@login_required(login_url="login")
def profileSpecific(request,username):
	context={}
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	context['isFriend']=False
	context['friendRequestPending']=False

	otherUser=AUser.objects.get(username=username)
	userFriendList=FriendList.objects.get(user=request.user)

	if userFriendList.isFriend(otherUser):
		context['isFriend']=True
	elif FriendRequest.objects.filter(sender=request.user, receiver=otherUser, isActive=True):
		context['friendRequestPending']=True
	try:
		context['profile']=UserProfile.objects.get(user_url=username)
	except Exception as e:
		print(e)
		
	return render(request,"main/func/profileSpecific.html",context)

@login_required(login_url="login")
def editProfile(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)

	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)

	if request.method=="POST":
		displayName=request.POST.get("display_name")
		shortDescription=request.POST.get("short_bio")
		longDescription=request.POST.get("long_bio")
		gender=request.POST.get("gender")
		user_profile = UserProfile.objects.get(user=user)

		if request.FILES.get('avatar'):
			avatar_file = request.FILES['avatar']
			# print("avatar fetched, about to change")
			user_profile.avatar.save(avatar_file.name, avatar_file)
		if displayName!=None:
			# print("Changed display name")
			user_profile.display_name = displayName
		if shortDescription!=None:
			# print("Changed short bio")
			user_profile.short_bio = shortDescription
		if longDescription!=None:
			# print("changed long bio")
			user_profile.long_bio = longDescription
		if gender!=None:
			user_profile.gender=gender.upper()

		user_profile.save()
		return render(request,'main/func/profile.html',context)

	

	return render(request,'main/edit/editProfile.html',context)
@login_required(login_url="login")
def notifications(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/notifications.html",context)


@login_required(login_url="login")
def friends(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/friends.html",context)


@login_required(login_url="login")
def feedback(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/feedback.html",context)


@login_required(login_url="login")
def contact(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/contact.html",context)


@login_required(login_url="login")
def events(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/events.html",context)



@login_required(login_url="login")
def settings(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/settings.html",context)

@login_required(login_url="login")
def startQuiz(request):
	context={}
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/quiz.html",context)


def logOut(request):
	logout(request)
	return redirect("/login/")

# 
