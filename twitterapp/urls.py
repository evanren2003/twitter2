from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #urls.py in twitter2 comes here
    #it calls views.py and uses the function index

    #u can post to a user page with the below
    path('post/<username>', views.usernameView, name = 'usernameView'),
    path('post/<username>/', views.usernameView, name = 'usernameView'), #make it for a specific user

    path('<int:id>', views.postView, name = 'postView'), #basic link to display just one tweet
    path('<int:id>/', views.postView, name = 'postView'),

    path('feed',views.feedView,name = 'feedView'), #display last 5 or so tweets
    path('feed/',views.feedView,name = 'feedView'),

    path('<username>', views.userView, name = 'userView'), #link to all the posts for one user
    path('<username>/', views.userView, name = 'userView'),
]
