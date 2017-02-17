# Try to import tweepy (twitter API wrapper), and pip install tweept if import fails
try:
	import tweepy
except ImportError:
	import os
	#if they have pip already on the machine, this should install tweepy
	os.system("pip install --ignore-installed tweepy --user")
	try:
		import tweepy
	# If second import fails, write the failure to the console
	except ImportError as e:
		print("An error occurred with importing Twitter\'s API")
		print(e.reason)
		#Code will not run without tweepy - please pip install tweepy

# Imports from the Python standard library
import time
from random import randint

# Imports class to read in authorization codes from an external file
try:
	from AuthCodes import *
	codes = AuthCodes()
	'''
	The consumer keys can be found on your application's Details
	page located at https://dev.twitter.com/apps (under "OAuth settings")
	'''
	consumer_key=codes.consumerkey() # authorization information is read in from an external file
	consumer_secret=codes.consumersecret()
	access_token=codes.accesstoken()
	access_token_secret=codes.accesssecret()
except ImportError as e:
	print(e.reason())
	consumer_key = input('What is your consumer key?')
	consumer_secret = input('What is your consumer secret?')
	access_token = input('What is your access token?')
	access_token_secret = input('What is your access token secret?')

# Set up tweepy object for user account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Find 50 most recent tweets from @UNDRAPTOR account and like & retweet them
for tweet in tweepy.Cursor(api.user_timeline, screen_name='UNDRAPTOR').items(50):
	try:
		print('\nTweet direct from user: @' + tweet.user.screen_name)
		if not tweet.favorited:
			api.create_favorite(tweet.id)
			print('Favorited tweet')
		else:
			print('Tweet already favorited')
		if not tweet.retweeted:
			api.retweet(tweet.id)
			print('Retweeted tweet')
		else:
			print('Tweet already retweeted')
		time.sleep(5)
	except Exception as e:
		print(e.reason)
	except StopIteration:
		break

# Find 50 most recent tweets in your main timeline and like & retweet them
for tweet in tweepy.Cursor(api.home_timeline).items(50):
	try:
		print('\nTweet in timeline by: @' + tweet.user.screen_name)
		if not tweet.favorited:
			api.create_favorite(tweet.id)
			print('Favorited tweet')
		else:
			print('Tweet already favorited')
		if not tweet.retweeted:
			api.retweet(tweet.id)
			print('Retweeted tweet')
		else:
			print('Tweet already retweeted')
		time.sleep(5)
	except Exception as e:
		print(e.reason)
	except StopIteration:
		break

# Find 50 most recemt tweets containing "python" and like & retweet them
for tweet in tweepy.Cursor(api.search, q='python').items(50):
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

# Set up list of original tweets
__tweetList = ["Snake, snake, Severus Snake. I'm a python.","What is a git and how do I eat one? I'm a python.","Can a mouse be parsed? I'm a python.","I don't string parse, I slither. I'm a python.","Just adaded a commit to a repo. I'm a python.","If machines can learn, then snakes can learn. I'm a python.","They've taught machines to learn to code. I'm a snake who learned to code. You can learn to code. I'm a python."]

# Set up list of exclamations and descriptors for random combination and tweeting
__oopsList = ["Oops!","Oops","Gee Wiz!","Darn.","Oh deer."]
__errorOccured = ["Was error found.","I rattled my rattler.","Sssssthtthssss","I forgot parseltongue.","I can't bot."]

# try to tweet from __tweetList, of that fails, random combine words from __oopsList and __errorOccured list for tweeting
try:
	string = __tweetList[randint(0,len(__tweetList))]
	api.update_status(string)
	print('\n'+string)
	__tweetList.remove(string)
	__tweetList.append(string)
	time.sleep(5)
except tweepy.error.TweepError:
	print('That tweet has already been tweeted')
	try:
		__status = __oopsList[randint(0,len(__errorOccured))] + " " + __errorOccured[randint(0,len(__errorOccured))] + " I'm a python."
		api.update_status(__status)
	except tweepy.error.TweepError:
		print('Something is boggled')
		__status = ""
		for index in range(0,randint(1,5)):
			__status += "Bother "
		__status += ". I'm a python."
		api.update_status(__status)
		print(__status)
