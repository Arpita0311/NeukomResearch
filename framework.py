import oauth2 as oauth
from config import CONFIG
from pprint import pprint
import json


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
		# print url
		return self.client.request(url , 
					method="GET",
					)
t = TwitterFW()
resp, content = t.get("https://api.twitter.com/1.1/search/tweets.json" , {'q':"@twitterapi"})
pprint(json.loads(content))
