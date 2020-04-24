from django.contrib import admin

from django.contrib.auth.models import User

# Register your models here.

from .models import Tweet,TweetUser

admin.site.register(Tweet)

admin.site.register(TweetUser)
