# Basic modules for django forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms


# User Creation form
class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = AUser
		fields = ('username','email','password')

# User Updation/Change form
class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = AUser
		fields = ('username','email','password')

# User form
class UserForm(forms.ModelForm):
	name=forms.CharField(max_length=20)
	email=forms.EmailField()
	password=forms.CharField(max_length=100,min_length=8)
	# password1=None
	# password2=None
	class Meta:
		model= AUser
		fields=('name','email','password')

	def get_user_info(self):
		return {
			'username': self.data['name'],
			'password': self.data['password'],
			'email': self.data['email']
		}
	def save(self,commit=True):
		userInfo=self.get_user_info()
		user=AUser.objects.create_user(userInfo['email'].lower(),userInfo['password'],username=userInfo['username'])
		user.set_password(userInfo['password'])
		user.is_active=False
		if commit:
			user.save()
			return user
		else:
			return user

