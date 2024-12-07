import random
import string

def random_tweet_generate():
    """Generate random tweet of 150 characters """
    length = random.randint(50,150)
    tweet = ''.join(random.choices(string.ascii_letters + string.digits + " ",k=length))
    return tweet.strip()