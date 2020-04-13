from django.contrib import admin

# Register your models here.

from .models import Tweet,TweetUser

admin.site.register(Tweet)

admin.site.register(TweetUser)
