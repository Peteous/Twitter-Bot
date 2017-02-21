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

This bot also expects you to have a .txt file named auth-codes.txt in the same repo as the bot. This is where you are expected to store your 4 authorization codes for your twitter bot, in format key_name:”key”\n

### Bot.py

### AuthCodes.py

### .gitignore
To avoid uploading my security codes to GitHub in this public repo, I have implemented the AuthCodes class to read in the codes from an external file. As such, I have used .gitignore to avoid uploading this external file. 

.gitignore is also used to avoid uploading the AuthCodes.pyc (and any other .pyc files that may be generated in the future) which are generated upon running Bot.py. This is simply because the file is redundant an unnecessary. 

### Disclaimer
Reading in authorization codes from a text file is not secure. They are stored in an unencrypted state in a simple txt file. I am using this method because it makes it easy for me to keep testing the Bot while also storing the code in a public repo. Using .gitignore is secure enough for my attack vector of people reading my authorization codes in the source code of the file. It is not bullet-proof security, and it may not be good enough for you. I encourage you to fork this repo and implement better security if you’re interested. I will absolutely consider merge requests that improve security. 