
from utils import apiSetu
import datetime
from time import sleep
import pandas as pd

class scanner:
	def __init__(self, **kwargs):
		self.api = apiSetu()
		self.history = []
		self.frame = pd.DataFrame(columns = ['Date','Min_Age','District',
				'1st_dose','2nd_dose','Hospital'])
		for key,value in kwargs.items():
			if key == 'age':
				self.age = value
			elif key =='districts':
				self.districts = value
			elif key == 'dose':
				if value == 1:
					self.dose = 'available_capacity_dose1'
				else:
					self.dose = 'available_capacity_dose2'
			elif key == 'days':
				self.days = value
			elif key == 'bot':
				self.messenger = value
	def scan(self,type = 'findByDistrict'):
		if type == 'findByDistrict':
			url = self.api.FIND_BY_DISTRICT
		for i in range(self.days):
			date = datetime.datetime.today() + datetime.timedelta(days= i)
			date = date.strftime('%d-%m-%Y')
			print('Searching for slot on ', date)
			for district in self.districts:
				resp = self.api.request(url+district+'&date='+date)
				self.filter(resp,date)
				sleep(3) # only 100 api calls permitted in 5 mins
			# To delete the last line in terminal
			print ("\033[A                             \033[A")

	def filter(self,content,date):
		for i in range(len(content['sessions'])):
			session = content['sessions'][i]
			if session[self.dose] > 0 and session['min_age_limit'] <= self.age:
				row= {'Date':date, 'Min_Age': session['min_age_limit'],
					'District':session['district_name'],
					'1st_dose':session['available_capacity_dose1'],
					'2nd_dose':session['available_capacity_dose2'],
					'Hospital':session['name']}
				msg = str(row['Date'])+'\n'+str(row['Hospital'])+'\n'+str(row['District'])+'\n'
				if msg not in self.history:	#to prevent repeated message of same content.
					self.history.append(msg)
					self.messenger.sendMessage(msg+self.dose+'->'+str(session[self.dose]))
					# To delete expired slots, append frame outside if statement. 
					self.frame = self.frame.append(row,ignore_index = True)
	def display(self):
		print('\x1bc') # To clear the terminal
		print(self.frame)
