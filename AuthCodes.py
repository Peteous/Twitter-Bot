class AuthCodes:
	def __init__(self):
		try:
			with open('auth-codes.txt','r') as authfile:
				self.consumer_key=authfile.readline()
				self.consumer_secret=authfile.readline()
				self.access_token=authfile.readline()
				self.access_token_secret=authfile.readline()
			authfile.close
		except:
			print('An error occured opening the required authorization file') 
	def _stripID(self,text):
		equals = 0
		code = ''
		for index in range(len(text)):
			if text[index] == '"' and not equals == 1:
				equals = 1
			elif equals == 1 and not text[index] == '"':
				code += text[index]
		return code.rstrip()
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