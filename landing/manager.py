from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

# Custom User manager
class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		# Preprocessing user email
		if not email:
			raise ValueError(_('Users must have an email address'))
		email = self.normalize_email(email)
		# Creating the user 
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password, **extra_fields):
		# Setting super user and other flags
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		# Checking if super user and other flags are set
		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True.'))
		# Use the first function, and create that user
		return self.create_user(email, password, **extra_fields)
