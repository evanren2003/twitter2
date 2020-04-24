from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# https://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/
#https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django
#https://stackoverflow.com/questions/6195478/max-image-size-on-file-upload
#https://stackoverflow.com/questions/8189800/django-store-user-image-in-model
class userProfile(models.Model):
    #extension of auth.user to include a profile picture
    #this doesn't work yet so Tweet doesn't include it yet (i will add it to Tweet later)

    #also add a username field
    def validate_image(fieldfile_obj):
        # checks for size of the image
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='twitterapp/images', validators=[validate_image]) #supposed to be profile picture field

class TweetUser(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, default = 1)
    username = models.CharField(max_length = 50)

    def __str__(self):
        return self.username

# https://stackoverflow.com/questions/44604405/django-uploading-image-using-builtin-user-model
class Tweet(models.Model):
    #user = models.ForeignKey(TweetUser, on_delete=models.CASCADE, default = None, null=True, blank=True)
    tweetuser = models.ForeignKey(TweetUser, unique=False, on_delete=models.CASCADE, default = 1)

    #fields for username, the text, and the publication date
    username = models.CharField(max_length = 50) #what is this username for its tied to tweetuser
    tweet_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)


    def __str__(self):
        return self.tweet_text

    def getUsername(self):
        return self.user

    def test_function(self):
        return true
