'''
This class is meant to be used in Bot.py

This class provides methods to read in authorization information from an external file which should be
	.gitignored in order to not show up in public git repos. This is by no means meant to be a secure
	storage method, but it's a way to privately store your auth codes while still using a public repo
'''
class AuthCodes:
	# upon object creation, auth-codes.txt is read into object
	def __init__(self):
		try:
			with open('auth-codes.txt','r') as authfile:
				self.consumer_key=authfile.readline()
				self.consumer_secret=authfile.readline()
				self.access_token=authfile.readline()
				self.access_token_secret=authfile.readline()
			authfile.close
		# If import fails, establish data from user input
		except:
			print('An error occured opening the required authorization file')
			self.consumer_key = input('What is your consumer key?')
			self.consumer_secret = input('What is your consumer secret?')
			self.access_token = input('What is your access token?')
			self.access_token_secret = input('What is your access token secret?')

	# Internal method for removing the descriptor text before the actual code
	def _stripID(self,text):
		equals = 0
		code = ''
		for index in range(len(text)):
			if text[index] == '"' and not equals == 1:
				equals = 1
			elif equals == 1 and not text[index] == '"':
				code += text[index]
		return code.rstrip()
	
	# If you want to use one method and parse theh values on your own, you can use this method
	def token_list(self):
		return [self._stripID(consumer_key), self._stripID(consumer_secret), self._stripID(access_token), self._stripID(access_token_secret)]
	
	def consumerkey(self):
		return str(self._stripID(self.consumer_key))
	def consumersecret(self):
		return str(self._stripID(self.consumer_secret))
	def accesstoken(self):
		return str(self._stripID(self.access_token))
	def accesssecret(self):
		return str(self._stripID(self.access_token_secret))