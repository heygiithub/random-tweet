from django.shortcuts import render

from .utils import random_tweet_generate

# Create your views here.

def random_tweet(request):
    tweet = random_tweet_generate()
    return render(request, 'random_tweet.html', {'tweet': tweet})


