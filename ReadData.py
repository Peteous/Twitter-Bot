'''
This class is meant to be used in Bot.py

This class provides methods to read in data from an external file for use in the Twitter Bot. Data is 
structured in format action="criteria"\n
'''
class ReadData:
	# upon object creation, twitter-data.txt is read into object
	def __init__(self):
		#dataList = []
		try:
			with open('data.txt','r') as datafile:
				self.dataList = datafile.readlines()
			datafile.close
		# If import fails, establish data from user input
		except:
			print('An error occured opening the required data file')

	def getAction(self,text):
		action = ''
		end = False
		for index in range(len(text)):
			if not text[index] == '=' and not end == True:
				action += text[index]
			if text[index] == '=' and not end == True:
				end = True
		return action

	def getActionList(self):
		actionList = []
		for line in self.dataList:
			actionList.append(self.getAction(line))
		return actionList

	def getCriteria(self,text):
		equals = False
		code = ''
		for index in range(len(text)):
			if text[index] == '"' and not equals == True:
				equals = True
			elif equals == True and not text[index] == '"':
				code += text[index]
		return code.rstrip()

	def getCriteriaList(self):
		criteriaList = []
		for line in self.dataList:
			criteriaList.append(self.getCriteria(line))
		return criteriaList

test = ReadData()