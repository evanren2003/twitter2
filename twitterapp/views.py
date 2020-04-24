from django.shortcuts import get_object_or_404, render
from django.template import loader

from django.http import HttpResponse

from .models import Tweet

from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

import pprint

#MAKE THE OTHER VIEWS DISPLAY LIKES

def index(request): #code from the video
    if request.POST:
        if 'inputUsername' in request.POST.keys():
            user = authenticate(username=request.POST['inputUsername'],password=request.POST['inputPassword'])
            if user is not None:
                login(request,user)
        elif 'logout' in request.POST.keys():
            logout(request)
    # if request.user.is_authenticated:
    #     loggedIn = True
    # else:
    #     loggedIn = False
    loggedIn = request.user.is_authenticated #i think this works

    template = loader.get_template('twitterapp/index.html')
    allTweets = Tweet.objects.order_by('-pub_date') #use this to edit your other view (timeline)

    print(User.objects.all())
    print()

    for user in User.objects.all():
        print(vars(user))
    print()

    for tweet in allTweets:

        print(vars(tweet))
        print()

        poster = User.objects.filter(username = tweet.tweetuser.user.username)[0]
        print(vars(poster))
        print()
        # poster = tweet.tweetuser.user
        tweet.firstName = poster.first_name
        tweet.lastName = poster.last_name

    context = {
        'allTweets':allTweets,
        'loggedIn':loggedIn,
        'user': request.user,
    }

    return HttpResponse(template.render(context,request))

def postView(request,id):
    #passes the tweet info into detail.html and which displays the tweet at http://localhost:8000/twitterapp/id
    post = get_object_or_404(Tweet, pk=id)
    poster = User.objects.filter(username = post.userPosted)[0]
    post.firstName = poster.first_name
    post.lastName = poster.last_name
    return render(request, 'twitterapp/detail.html', {'post': post})

def feedView(request):
    #to do:change it to make only followed people
    allTweets = Tweet.objects.order_by('-pubDate')[:10]
    counter = 0
    for tweet in allTweets:
        poster = User.objects.filter(username = post.userPosted)[0]
        tweet.firstName = poster.first_name
        tweet.lastName = poster.last_name
        counter = counter + 1 #im not sure if += 1 works oops xD
    if (counter == 0):
        template = loader.get_template('twitterapp/emptyfeed.html')
        context = {}
        return HttpResponse(template.render(context,request))
    else:
        context = {
            'allTweets':allTweets,
            'user': request.user, #is this one even necessary
        }
        template = loader.get_template('twitterapp/feedList.html')
        return HttpResponse(template.render(context, request))

#to do: modify the below view, and customize the pages (show likes)
#to do: modify tweets so that people can add replies
#to do: add profile picture to each user
#@myself to do list is in the comment above
#
#
#
#
#
# blank space for visibility

#this is weird, http://localhost:8000/twitterapp takes me to "blank page" aka emptypage.html
#is it somehow calling userView?

def userView(request, username):
    print("running userView")
    #need to replace once auth.user is integrated
    #try this with actual user data and a different for loop

    #replace with other code
    tweetList = []
    listCounter = 0
    counter = 1
    while True:
        try:
            post = Tweet.objects.get(pk=counter)
            if (str(post.username) == username): #just check if the strings are equal (error if two users have the same username?)
                tweetList.append(post)
                listCounter += 1
            counter += 1
        except Tweet.DoesNotExist:
            break
    if (listCounter == 0):
        return render(request, 'twitterapp/emptypage.html')
    else:
        return render(request, 'twitterapp/detailList.html', {'list': tweetList, 'username':username})

def usernameView(request, username):
    if request.POST:
        newTweet = Tweet(
            tweet_text = request.POST['newPostText'],
            user = request.POST['userPosting'],
            pub_date = timezone.now(),
            )
        newTweet.save()
    try:
        userInfo = User.objects.filter(username=username)[0]
    except:
        template = loader.get_template('posts/emptyusername.html')
        context = {
            'username': username,
            }
        return HttpResponse(template.render(context, request))

    myTweets = Tweet.objects.filter(userPosted = username)
    latestTweets = myTweets.order_by('-pubDate')[:5]
    template = loader.get_template('posts/usernamePage.html')
    context = {
        'latestPosts': latestTweets,
        'username': userInfo.username,
        'firstName': userInfo.first_name,
        'lastName': userInfo.last_name,
        'user': username,
        }

    return HttpResponse(template.render(context, request))
