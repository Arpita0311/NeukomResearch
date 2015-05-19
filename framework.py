import oauth2 as oauth
from config import CONFIG

class TwitterFW:
	def __init__(self):
		token = oauth.Token(
						key=CONFIG.get("auth_token_key"), 
						secret=CONFIG.get("auth_token_secret")
						)
		consumer = oauth.Consumer(key=CONFIG.get("consumer_key"), 
								secret=CONFIG.get("consumer_secret")
								)
		self.client = oauth.Client(consumer, token)

	def get(self , url , get_params = None):
		if get_params :
			url = url + '?'
			for key in get_params.iterkeys():
				url += key + "=" + get_params.get(key) + "&"
		print url
		return self.client.request(url , 
					method="GET", 
		)
