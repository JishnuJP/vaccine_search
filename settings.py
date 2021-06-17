from defaults import defaultValues
from utils import apiSetu,bot
import pandas as pd

## Search filtering parameters and telegram bot settings
class settings(defaultValues, apiSetu):
	def __init__(self):
		defaultValues.__init__(self)
		apiSetu.__init__(self)
		self.bot = bot(self.TELE_URL,self.CHAT_ID)
		
		self.displaySettings()
		temp = input('Change Settings ? (y/n):')
		if temp == 'y':
			self.setValues()
	def setValues(self):
		self.AGE = int(input('Age : '))
		self.DOSE = int(input('Dose (1 or 2) : '))
		self.DAYS = int(input('Days : '))
		self.STATE_ID = self.getStateId()
		self.DISTRICTS = self.getDistrictId()
		self.telegram_activation()
	def getStateId(self):
		states = self.request(self.STATESCODE_URL)
		states = pd.DataFrame(states['states'])
		print(states)
		print('__________________________')
		temp = input('\nYour state Id: ')
		if temp == '*':
			return self.STATE_ID
		else:
			return int(temp)
	def getDistrictId(self):
		dist = self.request(self.DISTRICTCODE_URL+str(self.STATE_ID))
		dist = pd.DataFrame(dist['districts'])
		print(dist)
		print('__________________________')
		temp =  input('\nEnter District Ids (seprerated by coma(,)) : ')
		if temp == '*':
			return self.DISTRICTS
		else:
			return list(temp.split(','))
	def displaySettings(self):
		print('#######################-Settings-##########################')
		print('Age : ',self.AGE)
		print('Dose : ',self.DOSE)
		print('State Id : ',self.STATE_ID)
		print('District Ids : ',self.DISTRICTS)
		print('Chat Id : ', self.CHAT_ID)
		print('###########################################################')
	def telegram_activation(self):
		temp = input('Do you have a telegram bot (y/n) : ')
		if temp == 'y':
			print(''' NOTE : Please make sure that your telegram token and chat id 
				are in the file telegram_token.txt''' )
			self.initTelegram(True)
			
		else:
			self.initTelegram(False)
		self.bot = bot(self.TELE_URL,self.CHAT_ID)
##------------------------------------------------------------------------------------------


if __name__ == '__main__':
	
	settings().displaySettings()
