# Twitter-Bot
## A Python based twitter bot
### Table of Contents
- Requirements
- Bot.py
- AuthCodes.py
- .gitignore
- Disclaimer

### Requirements
This bot implements the Twitter API wrapper called tweeps. It requires that you have proper access to that library. I recommend using pip install to install tweepy, but you could try repo-cloning of all the dependent libraries if you really like to work extra hard.

This bot also expects you to have a .txt file named auth-codes.txt in the same repo as the bot. This is where you are expected to store your 4 authorization codes for your twitter bot, in format: key_name:”key”\n

### Bot.py
The bot begins by importing Python standard library components time and randint for use later in the code. 

The bot then tries to `import tweepy`, which is critical to code functioning. If it fails, it then performs `import os` from the standard library, and uses that library to try to `$ pip install tweepy` and wait for a short time for tweepy to install. It then tries `import tweepy` again, and if that fails, it outputs to the console. In this final case, the code will fail out.

Next, the code with try to `import AuthCodes` and establish an AuthCodes object in order to set the authorization codes from an external file. If it cannot `import AuthCodes` then it will ask the user via the console for their codes 1 by 1. The bot then uses these authorization codes to establish an api object for the twitter actions.

It also creates a URL with the user’s profile address for opening a browser tab upon completion of code to see what you’ve done. Then is tries to `import webbrowser` from the standard library. The code will be boggled if this import fails.

The first twitter section of the code searches for a specific user, and then sorts through their 50 most recent tweets, likes them if they haven’t already been liked, and retweets them if they haven’t already been retweeted. A counter system was implemented to skip over this step if 3 tweets have already been retweeted and liked, because it could be assumed that the bot is caught up with this user’s timeline.

The next section of the code pulls up the latest section of the bot account’s timeline, composed of the last 50 tweets from users the bot account is following and tweets from the bot account itself. The code iterates through all 50 of these tweets. It checks to see if the tweet is from an account other than itself, and if so, favorites the and retweets the tweets if they are not already favorited or retweeted. If it is a tweet from your own account, it just prints to the console that you found your own tweet. 

The next section of the code finds the 50 most recent tweets which use the given search term. It iterates through and likes and retweets the tweets which have not already been liked and retweeted. It checks to see if the username of the tweet author is your own username, and ignores the tweet if it is. 

The next section of the code finds the 30 most recent tweets using a hashtag, and likes and retweets those tweets if they haven’t been found in a previous iteration of the bot code. The code ensures that if the found tweet is from the bot’s own account, it gets ignored. Additionally, if 3 or more tweets have already been favorited and 3 or more tweets have already been retweeted, then the bot breaks out of this code section. 

The final bit of the code pulls in a random tweet from a list of tweets and posts the tweet. If it encounters an error, it builds a tweet of random “oops” type language and tweets that out instead. The code completes by opening a web browser page to the twitter bot’s account profile so you can see what your bot has done.

### AuthCodes.py
This is a class that was built for use in Bot.py. It’s `__init__` method reads in data from auth-codes.txt for use as authorization codes, and if it can’t find that text file, it asks the user to type in their codes. The internal method `_stripID()` is used to pull in just the authorization code, stripping the code identifier that was read in during the `__init__` method. The `token_list()` method returns a list of all of the authorization code values. The four remaining methods return their namesake authorization code. 

### .gitignore
To avoid uploading my security codes to GitHub in this public repo, I have implemented the AuthCodes class to read in the codes from an external file. As such, I have used .gitignore to avoid uploading this external file. 

.gitignore is also used to avoid uploading the AuthCodes.pyc (and any other .pyc files that may be generated in the future) which are generated upon running Bot.py. This is simply because the file is redundant an unnecessary. 

### Disclaimer
Reading in authorization codes from a text file is not secure. They are stored in an unencrypted state in a simple txt file. I am using this method because it makes it easy for me to keep testing the Bot while also storing the code in a public repo. Using .gitignore is secure enough for my attack vector of people reading my authorization codes in the source code of the file. It is not bullet-proof security, and it may not be good enough for you. I encourage you to fork this repo and implement better security if you’re interested. I will absolutely consider merge requests that improve security. 