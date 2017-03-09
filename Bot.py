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
	# Reset Counters at every loop iteration
	fav_counter = 0
	rt_counter = 0

	if actionList[index] == 'user-timeline':
		print('In user-following section for user: @' + criteriaList[index])
		# Find 50 most recent tweets from user account and like & retweet them
		for tweet in tweepy.Cursor(api.user_timeline, screen_name=criteriaList[index]).items(50):
			if fav_counter >= 3 and rt_counter >= 3:
				break
			if not tweet.text.startswith('@'):
				try:
					if not tweet.favorited:
						api.create_favorite(tweet.id)
					else:
						fav_counter+=1
					if not tweet.retweeted:
						api.retweet(tweet.id)
					else:
						rt_counter+=1
					time.sleep(25)
				except tweepy.error.TweepError as e:
					print(e.reason)
					time.sleep(25)
				except tweepy.error.RateLimitError as r:
					print('Rate limited. Waiting')
					time.sleep(200)
				except StopIteration:
					break
			else:
				time.sleep(25)

	elif actionList[index] == 'hashtag':
		print('In hashtag-following section for hashtag ' + criteriaList[index])
		query = criteriaList[index] + ' filter:safe :)'
		# Find 50 most recemt tweets containing hashtag and like & retweet them
		for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(50):
			if fav_counter >= 5 and rt_counter >= 5:
				break
			try:
				if not tweet.user.screen_name == user.screen_name and not tweet.text.startswith('@'):
					if not tweet.retweeted:
						tweet.retweet()
					else:
						rt_counter += 1
					if not tweet.favorited:
						tweet.favorite()
					else:
						fav_counter += 1
					time.sleep(25)
				else:
					time.sleep(25)
			except tweepy.error.TweepError as e:
				print(e.reason)
				time.sleep(25)
			except tweepy.error.RateLimitError as r:
				print('Rate limited. Waiting')
				time.sleep(200)
			except StopIteration:
				break

	elif actionList[index] == 'search':
		print('In search-following section for search: ' + criteriaList[index])
		query = criteriaList[index] + ' filter:safe :)'
		# Find 50 most recent tweets containing search term and like & retweet them
		for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(50):
			if fav_counter >= 10 and rt_counter >= 10:
				break
			try:
				if not tweet.user.screen_name == user.screen_name and not tweet.text.startswith('@'):
					if not tweet.retweeted:
						tweet.retweet()
					else:
						rt_counter += 1
					if not tweet.favorited:
						tweet.favorite()
					else:
						fav_counter += 1
					time.sleep(25)
				else:
					time.sleep(25)
			except tweepy.error.TweepError as e:
				print(e.reason)
				time.sleep(25)
			except tweepy.error.RateLimitError as r:
				print('Rate limited. Waiting')
				time.sleep(200)
			except StopIteration:
				break

	elif actionList[index] == 'tweet':
		__tweetList.append(criteriaList[index])
		time.sleep(20)

# Reset Counters
fav_counter = 0
rt_counter = 0
# Find 50 most recent tweets in your main timeline and like & retweet them
print('In main timeline section')
for tweet in tweepy.Cursor(api.home_timeline).items(50):
	try:
		if not fav_counter >= 30 and not rt_counter >= 30:
			if not tweet.user.screen_name == user.screen_name and not tweet.text.startswith('@'):
				if not tweet.favorited:
					api.create_favorite(tweet.id)
				else:
					fav_counter += 1
				if not tweet.retweeted:
					api.retweet(tweet.id)
				else:
					rt_counter += 1
				time.sleep(25)
	except tweepy.error.TweepError as e:
		print(e.reason)
		time.sleep(25)
	except tweepy.error.RateLimitError as r:
		print('Rate limited. Waiting')
		time.sleep(200)
	except StopIteration:
		break

# try to tweet from __tweetList
try:
	print('In Tweeting section')
	string = __tweetList[randint(0,len(__tweetList)-1)]
	api.update_status(string)
	time.sleep(25)
except tweepy.error.TweepError:
	time.sleep(25)
except tweepy.error.RateLimitError:
	print('Rate limited. Waiting')
	time.sleep(200)

print('\nCheck out your handywork!')
webbrowser.open(_URL)