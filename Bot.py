try:
	from tweepy import *
except ImportError:
	import os
	os.system("python get-pip.py --user")
	os.system("pip install --ignore-installed tweepy --user")

