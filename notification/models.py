from django.db import models

from twitteruser.models import TwitterUserModel
from tweet.models import TweetModel


# Create your models here.

class NotificationModel(models.Model):
  user = models.ForeignKey(TwitterUserModel, on_delete=models.CASCADE)
  tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
  time_viewed = models.DateTimeField(default=None, blank=True, null=True)