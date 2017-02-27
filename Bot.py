# Imports from the Python standard library
import time
from random import randint

# Try to import tweepy (twitter API wrapper), and pip install tweept if import fails
try:
	import tweepy
except ImportError:
	import os
	#if they have pip already on the machine, this should install tweepy
	os.system("pip install --ignore-installed tweepy --user")
	time.sleep(50) #Wait a bit for tweepy to pip install before trying to import tweepy
	try:
		import tweepy
	# If second import fails, write the failure to the console
	except ImportError as e:
		print("An error occurred with importing Twitter\'s API")
		print(e.reason)
		#Code will not run without tweepy - please pip install tweepy

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

# Try to read in data for the twitter bot to work with
try:
	from ReadData import *
	data = ReadData()
	actionList = data.getActionList()
	criteriaList = data.getCriteriaList()
except ImportError:
	actionList = []
	actionList.append('tweet=')
	criteriaList = []
	criteriaList.append(input('What would you like to tweet?'))

# Establish URL for opening webpage upon code completion
user = api.me()
_URL = 'https://www.twitter.com/'+user.screen_name

# Import webbrowser library for opening url in default browser
try:
	import webbrowser
except ImportError as e:
	print(e.reason)
	print("Web Browser Library wasn't found.\nPaste this url into your browser to see your handy work:\n" + _URL)

# Set up list of original tweets
__tweetList = []

for index in range(len(actionList)-1):
	if actionList[index] == 'user-timeline':
		fav_counter = 0
		rt_counter = 0

		# Find 50 most recent tweets from user account and like & retweet them
		for tweet in tweepy.Cursor(api.user_timeline, screen_name=criteriaList[index]).items(50):
			if fav_counter >= 3 and rt_counter >= 3:
				print("You're all caught up on this user's timeline")
				break
			try:
				print('\nTweet from @' + tweet.user.screen_name)
				if not tweet.favorited:
					api.create_favorite(tweet.id)
					print('Favorited tweet')
				else:
					fav_counter+=1
					print('Tweet already favorited')
				if not tweet.retweeted:
					api.retweet(tweet.id)
					print('Retweeted tweet')
				else:
					rt_counter+=1
					print('Tweet already retweeted')
				time.sleep(5)
			except Exception as e:
				print(e.reason)
				print('\nCheck out your handywork!')
				webbrowser.open(_URL)
			except StopIteration:
				break
	elif actionList[index] == 'hashtag':
		# Reset Counters
		rt_counter = 0
		fav_counter = 0

		# Find 50 most recemt tweets containing hashtag and like & retweet them
		for tweet in tweepy.Cursor(api.search, q=criteriaList[index]).items(50):
			if fav_counter >= 3 and rt_counter >= 3:
				print("You're all caught up on that hashtag")
				break
			try:
				if not tweet.user.screen_name == user.screen_name:
					print('\nTweet by: @' + tweet.user.screen_name)
					if not tweet.retweeted:
						tweet.retweet()
						print('Retweeted the tweet')
					else:
						print('Tweet already retweeted')
					if not tweet.favorited:
						tweet.favorite()
						print('Favorited the tweet')
					else:
						print('Tweet already favorited')
					time.sleep(5)
				else:
					print('\nYou found your tweet. Consider it ignored.')
					time.sleep(5)
			except tweepy.TweepError as e:
				print(e.reason)
			except StopIteration:
				print('\nCheck out your handywork!')
				webbrowser.open(_URL)
				break

	elif actionList[index] == 'search':
		# Find 50 most recent tweets containing search term and like & retweet them
		for tweet in tweepy.Cursor(api.search, q=criteriaList[index]).items(50):
			try:
				if not tweet.user.screen_name == user.screen_name:
					print('\nTweet by: @' + tweet.user.screen_name)
					if not tweet.retweeted:
						tweet.retweet()
						print('Retweeted the tweet')
					else:
						print('Tweet already retweeted')
					if not tweet.favorited:
						tweet.favorite()
						print('Favorited the tweet')
					else:
						print('Tweet already favorited')
					time.sleep(5)
				else:
					print('\nYou found your tweet. Consider it ignored.')
					time.sleep(5)
			except tweepy.TweepError as e:
				print(e.reason)
			except StopIteration:
				print('\nCheck out your handywork!')
				webbrowser.open(_URL)
				break

	elif actionList[index] == 'tweet':
		__tweetList.append(criteriaList[index])
		time.sleep(5)

# Find 100 most recent tweets in your main timeline and like & retweet them
for tweet in tweepy.Cursor(api.home_timeline).items(100):
	try:
		if not tweet.user.screen_name == user.screen_name:
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
		else:
			print('\nTweet in timeline by: @' + tweet.user.screen_name)
			print('This is your own tweet')
	except Exception as e:
		print(e.reason)
	except StopIteration:
		print('\nCheck out your handywork!')
		webbrowser.open(_URL)
		break

# try to tweet from __tweetList
try:
	string = __tweetList[randint(0,len(__tweetList)-1)]
	api.update_status(string)
	print('\n'+'Just tweeted: '+string)
	time.sleep(5)
except tweepy.error.TweepError:
	print('\nJust tried fo tweet: ' + string)
	print('That tweet has already been tweeted')

print('\nCheck out your handywork!')
webbrowser.open(_URL)