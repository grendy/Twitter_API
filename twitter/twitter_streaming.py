try:
    import json
except ImportError:
    import simplejson as json
import settings

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = settings.access_token
ACCESS_SECRET = settings.access_secret
CONSUMER_KEY = settings.consumer_key
CONSUMER_SECRET = settings.consumer_secret

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter = TwitterStream(auth=oauth)


# Get a sample of the public data following through Twitter
# iterator = twitter.statuses.filter(track="ahok")

iterator = twitter.statuses.user_timeline(screen_name="billybob")
# twitter.search.tweets(q='#haiku')

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
# tweet_count = 10
# for tweet in iterator:
#     tweet_count -= 1
#     # Twitter Python Tool wraps the data returned by Twitter
#     # as a TwitterDictResponse object.
#     # We convert it back to the JSON format to print/score
#     print json.dumps(tweet)
#
#     # The command below will do pretty printing for JSON data, try it out
#     # print json.dumps(tweet, indent=4)
#
#     if tweet_count <= 0:
#         break