## Contains the default values for search settings.

AGE = 45
DOSE = 2
DAYS = 2
STATE_ID = 17
DISTRICTS = ['304', '300', '303','307']


TELEGRAM_BOT = True


#----------------------------------------------------------

class defaultValues:
	def __init__(self):
		print('Initializing default values')
		self.AGE = AGE
		self.DOSE = DOSE
		self.DAYS = DAYS
		self.STATE_ID =STATE_ID
		self.DISTRICTS = DISTRICTS
		self.initTelegram(TELEGRAM_BOT)
	def initTelegram(self,command):
		if command:
			f=open("telegram_token.txt","r")
			lines = f.readlines() #it has a \n at the end of each line
			self.TELE_URL =  "https://api.telegram.org/bot"+str(lines[0].strip('\n'))
			self.CHAT_ID = str(lines[1].strip('\n'))
			f.close()
		else:
			self.TELE_URL = None
			self.CHAT_ID = None

