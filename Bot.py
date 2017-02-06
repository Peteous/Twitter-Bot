try:
	import tweepy
except ImportError:
	import os
	os.system("python get-pip.py --user")
	os.system("pip install --ignore-installed tweepy --user")
	try:
		import tweepy
	except ImportError:
		print("An error occurred with importing Twitter\'s API")

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
