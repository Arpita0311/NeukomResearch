import oauth2 as oauth
from config import CONFIG
from pprint import pprint
import json
from datetime import datetime , date
import time
import MySQLdb

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

def sanitize_string(s):
	s = s.encode("ascii" , "ignore")

def twitter_date_to_timestamp(date):
	return time.mktime(datetime.strptime(date , "%a %b %d %H:%M:%S +0000 %Y").timetuple())

def twitter_date_to_datetime(date):
	d = datetime.strptime(date , "%a %b %d %H:%M:%S +0000 %Y")
	return datetime.strftime(d , "%Y-%m-%d %H:%M:%S")

class Model:
	def __init__(self):
		self.db = MySQLdb.connect(
			host = CONFIG.get('db_host') ,
			user = CONFIG.get('db_user') ,
			passwd = CONFIG.get('db_password') ,
			db = CONFIG.get('db_name')
		)
		self.cursor = self.db.cursor()
	
	def save_min_id(self , id):
		statement = "INSERT INTO script_details(min_id) VALUES ('%s');" % id
		self.cursor.execute(statement)
		self.db.commit()
	
	def fetch_last_min_id(self):
		statement = "SELECT min_id from script_details ORDER BY id DESC LIMIT 1;"
		self.cursor.execute(statement)
		r = self.cursor.fetchone()
		if r:
			return r[0]
		else :
			return None

	def fetch_all_tweets(self):
		statement = "SELECT * FROM tweets where id>=65000;"
		self.cursor.execute(statement)
		return self.cursor.fetchall()
	
	def save_times_for_tweets(self):
		statement = "SELECT * FROM tweets;"
		self.cursor.execute(statement)
		rows = self.cursor.fetchall()
		for row in rows:
			statement = "update tweets set tweet_created_datetime='%s' where id='%s';" % (twitter_date_to_datetime(row[2]) , row[0])
			self.cursor.execute(statement)
			self.db.commit()
			# print statement
			# break

m = Model()


# print m.fetch_last_date()

# t = TwitterFW()
# resp, content = t.get("https://api.twitter.com/1.1/search/tweets.json" ,
# 						{'geocode':"40.717728,-74.0021647,100mi"})
# x = json.loads(content)
#
# pprint(x)
#
# out_file = open("test.json","w")
# json.dump(content,out_file, indent = 4)
# out_file.close()
#
# pprint(json.loads(content['statuses'
# ]))