"""
Django settings for Conversafe project.

Generated by 'django-admin startproject' using Django 4.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

######################| Main Session Details|########################################
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('CONVERSAFE_SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []

# Session details
INTERNAL_IPS = [
	"127.0.0.1",
]
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 1440*60*15
PASSWORD_RESET_TIMEOUT_DAYS=1

######################| SMTP Info for emails|########################################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'emails.conversafe@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('CONVERSAFE_EMAIL_HOST_PASSWORD')


EXPIRE_AFTER = "1d"
MAX_RETRIES = 4
DEFAULT_FROM_EMAIL = 'noreply<no_reply@conversafe.com>'


# Email UI 
LOGIN_URL = "login"
HTML_MESSAGE_TEMPLATE = "auth/email/emailTemplates/emailTemplate.html"
VERIFICATION_SUCCESS_TEMPLATE = "auth/email/showInfo/verificationSuccessful.html"
VERIFICATION_FAILED_TEMPLATE = "auth/email/showInfo/verificationFailed.html"
REQUEST_NEW_EMAIL_TEMPLATE = "auth/email/resendEmail.html"
LINK_EXPIRED_TEMPLATE = 'auth/email/showInfo/expired.html'
NEW_EMAIL_SENT_TEMPLATE  = 'auth/email/showInfo/checkEmail.html'


######################| Other Django Settings|#######################################
INSTALLED_APPS = [
	'daphne',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Downloaded apps
	'verify_email.apps.VerifyEmailConfig', 
	# Created apps
	'AIChat',
	'chat',
	'friends',
	'core',
	'landing',
	'notification'    
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Conversafe.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR,"templates"], 
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

#### Configuring ASGI for Websockets ###################################3
WSGI_APPLICATION = 'Conversafe.wsgi.application'
ASGI_APPLICATION = 'Conversafe.asgi.application'

CHANNEL_LAYERS = {                                                
	"default": {                                                  
		"BACKEND": "channels.layers.InMemoryChannelLayer",        
	},                                                            
}   
#######################################################################

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]


######################| Internationalization |#######################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

######### FILE CONFIG ############################### 
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static/"]
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# DEFAULT MODEL 
AUTH_USER_MODEL = 'landing.AUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
