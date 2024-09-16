###  Libraries and stuff ############################################################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
# Some model objects
from landing import models
from .models import UserProfile,LearningSource
from landing.models import AUser
from friends.models import *
from notification.utils import * # For notifications
######################################################################

# Home/Dashboard page
@login_required(login_url="login")
def home(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/dashboard.html",context)

# Profile view
@login_required(login_url="login")
def profile(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/profile.html",context)

# A Specific profile -> Other user's profile
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

# Edit own profile
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
			user_profile.avatar.save(avatar_file.name, avatar_file)
		if displayName!=None:
			user_profile.display_name = displayName
		if shortDescription!=None:
			user_profile.short_bio = shortDescription
		if longDescription!=None:
			user_profile.long_bio = longDescription
		if gender!=None:
			user_profile.gender=gender.upper()

		user_profile.save()
		return render(request,'main/func/profile.html',context)

	return render(request,'main/edit/editProfile.html',context)

# Notifications page
@login_required(login_url="login")
def notifications(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/notifications.html",context)


# Friends page
@login_required(login_url="login")
def friends(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/friends.html",context)


# Feedback page
@login_required(login_url="login")
def feedback(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/feedback.html",context)


# Contacts page
@login_required(login_url="login")
def contact(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/contact.html",context)


# Events page
@login_required(login_url="login")
def events(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	context['learning_sources']=LearningSource.objects.all()
	return render(request,"main/func/events.html",context)


# Settings page
@login_required(login_url="login")
def settings(request):
	context={}
	user = AUser.objects.get(pk=request.user.pk)
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/settings.html",context)

# Quiz page
@login_required(login_url="login")
def startQuiz(request):
	context={}
	context['notifications_unread']=notifs(request.user)
	context['notifications_count']=notifCount(request.user)
	return render(request,"main/func/quiz.html",context)


# Logout function
def logOut(request):
	logout(request)
	return redirect("/login/")

