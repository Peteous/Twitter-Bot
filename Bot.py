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

import time
from random import randint

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

for tweet in tweepy.Cursor(api.search, q='python').items(20):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        time.sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

for tweet in tweepy.Cursor(api.user_timeline).items(50):
	try:
		print(tweet)
		if not tweet.favorited:
			api.create_favorite(tweet.id)
		if not tweet.retweeted:
			api.retweet(tweet.id)
		time.sleep(5)
	except Exception as e:
		print(e.reason)
	except StopIteration:
		break

__tweetList = ["What is a git and how do I eat one? I'm a python.","Can a mouse be parsed? I'm a python.","I don't string parse, I slither. I'm a python.","Just adaded a commit to a repo. I'm a python."]
__oopsList = ["Oops!","Oops","Gee Wiz!","Darn."]
__errorOccured = ["Was error found.","I rattled my rattler.","Sssssthtthssss","I forgot parseltongue."]
try:
	for string in __tweetList:
		api.update_status(string)
		print(string)
		__tweetList.remove(string)
		__tweetList.append(string)
		time.sleep(900)
except tweepy.error.TweepError:
	print('That tweet has already been tweeted')
	try:
		__status = __oopsList[randint(0,len(__errorOccured))] + " " + __errorOccured[randint(0,len(__errorOccured))] + " I'm a python."
		api.update_status(__status)
	except TweepError:
		print('Something is boggled')
		__status = ""
		for index in range(0,randint(1,5)):
			__status += "Bother "
		__status += ". I'm a python."
		api.update_status(__status)
