"""twitter2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#PYTHON VERSION: 3.8.1
#DJANGO VERSION: 3.0.3
#PILLOW VERSION: 7.0.0 (i think)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #basic url setup, will include more pages for each user, to add a post, etc
    path('', include ('twitterapp.urls')),
    #"When I loaded up your server, I put in localhost:8000 and got a 404 page not found error. That root address should lead somewhere."
    #hm i didn't change any of this but when i put in localhost:8000 it displayed a page with "Hello, world. You're at the twitterapp index." for me, weird
    path('twitterapp/', include('twitterapp.urls')),
    path('admin/', admin.site.urls),
]
