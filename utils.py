
import requests
import json

class bot:
	def __init__(self,url,chat=None):
		self.url = str(url) # url is api url+bot token
		self.chat_id = str(chat)
	def sendMessage(self,msg,chat_id=None):
		if self.chat_id == None or self.url==None:
			pass
			return
		elif chat_id ==None:
			chat_id = self.chat_id
			query = self.url+'/sendMessage?chat_id='+chat_id+'&text='+msg
			resp = requests.get(query)
			if resp.status_code == 200:
				print('send msg',end='\r')
			else:
				print('failed to send msg. code:',resp.status_code,end = '\r')

class apiSetu:
	def __init__(self):
		print('Initializing api setu')
		self.FIND_BY_DISTRICT = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id='
		self.STATESCODE_URL = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
		self.DISTRICTCODE_URL='https://cdn-api.co-vin.in/api/v2/admin/location/districts/'
	def request(self,url):
		header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
		resp = requests.get(url,headers = header)
		# content of resp is in bytes
		if resp.status_code == 200:
			content = resp.content.decode('UTF-8') # converting bytes to str
			return json.loads(content) #converting str to dict
		else:
			responseHandler(resp.status_code,url)

#----------------------------------------------------------------------------------
def responseHandler(code,url = None):
# to handle the HTTP error code.
	if code == 401:
		raise Exception('HTTPS: Unauthorised Access ',url)
	elif code ==  500:
		raise Exception('HTTPS: Invalid Query', url)
	else:
		raise Exception(f'HTTPS: Response Code is {code} ', url)
if __name__ =='__main__':
	bot = bot('xyz')
	api = apiSetu()
