#!/usr/bin/env python3
import datetime
import search
import settings

class vaccineSearch:
	def __init__(self,**kwargs):
		for key,value in kwargs.items():
			if key == 'bot':
				self.messenger = value
		self.vax_scanner = search.scanner(**kwargs)
		self.errors = []
		self.today = datetime.datetime.today().strftime('%d-%m-%Y')
	def launchScan(self):
	# Launching an infinite search
		while True:
			today = datetime.datetime.today().strftime('%d-%m-%Y')
			if today != self.today:
				self.today = today
				self.messenger.sendMessage('Good day guyzz :)')
				# Daily msg, to make sure that bot is working.
			self.vax_scanner.scan()	#Find slot and send telegram msg.
			self.vax_scanner.display()	#Display on terminal
#---------------------------------------------------------------------------------
if __name__=='__main__':
	s = settings.settings()
	finder = vaccineSearch(bot = s.bot,age = s.AGE, districts = s.DISTRICTS,
				dose = s.DOSE, days = s.DAYS)
	telegram = s.bot
	try:
		finder.launchScan()

	except Exception as e:
		if str(e) not in search.errors:
			search.errors.append(str(e))
			telegram.sendMessage(str(e))
			print(e)

