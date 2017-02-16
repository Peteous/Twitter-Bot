class AuthCodes:
	def __init__(self):
		try:
			with open('auth-codes.txt','r') as authfile:
				consumer_key=authfile.readline()
				consumer_secret=authfile.readline()
				access_token=authfile.readline()
				access_token_secret=authfile.readline()
			authfile.close
		except:
			print('An error occured opening the required authorization file') 
	def _stripID(self,text):
		equals = 0
		code = String()
		for index in len(text):
			if text[index] == '=' and not equals == 1:
				equals = 1
			if equals == 1:
				code += text[index]
		return code
	def token_list(self):
		return [self._stripID(consumer_key), self._stripID(consumer_secret), self._stripID(access_token), self._stripID(access_token_secret)]
	def consumerkey(self):
		return self._stripID(consumer_key)
	def consumersecret(self):
		return self._stripID(consumer_secret)
	def accesstoken(self):
		return self._stripID(access_token)
	def accesssecret(self):
		return self._stripID(access_token_secret)