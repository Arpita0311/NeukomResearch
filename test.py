from framework import *
import csv,codecs, unicodedata

def fetch_tweets_till_date() :
	
	i = 0

	min_id = None
	with (codecs.open('test.csv' , 'w',encoding ='utf-8',errors='ignore')) as fp:
		f = csv.writer(fp , delimiter=',')
		f.writerow (["Tweet ID","user ID","lat" , "lng",
					"friend_Count","location","geo_enabled",
					"Screen name","user name","users_followers_count" ,
					"users_friends_count" ,
					"users_favourites_count" , "user_statuses_count" , "users_geo_enabled" ,
					"user_profile_background_image_url" ,
					"user_profile_image_url"])
		t = TwitterFW()
		url ="https://api.twitter.com/1.1/search/tweets.json"
	
		geocode = "40.717728,-74.0021647,100mi"
		until = "2015-09-01"
	
		while (i < 10):
			if (min_id == None):
				resp, content = t.get(
										url , 
										{
											'geocode' : geocode ,
											'until' : until
										}
									)
			else :
				resp, content = t.get(
										url , 
										{'geocode' : geocode , 
										'max_id' : str(min_id)
										}
									)
			# printing the contents
			# pprint(json.loads(content))
			content = unicode(content,"utf-8")
			content = json.loads(content)
			if not content['statuses'] :
				print("End of tweets encountered.")
				return
			
			# for tweet in content['statuses'] :
			# 	print "Tweet id is " + str(tweet['id']) + " by " + str(tweet['user']['screen_name'])

			for x in range(0 , len(content['statuses'])):
				lat_lng = content['statuses'][x].get('coordinates',None)
				if lat_lng :
					lat_lng = lat_lng.get('coordinates')
					# lat_lng_str = str(lat_lng[0]) + '-' + str(lat_lng[1])
					lat_str = str(lat_lng[0])
					lng_str = str(lat_lng[1])
				else :
					# lat_lng_str = ''
					lat_str = ''
					lng_str = ''

				s = [
				content['statuses'][x]['id'],
				content['statuses'][x]['user']['id'] ,
				lat_str,
				lng_str,
				content['statuses'][x]['user']['friends_count'],
				content['statuses'][x]['user']['location'].encode("ascii" , "ignore"),
				content['statuses'][x]['user']['geo_enabled'],
				content['statuses'][x]['user']['screen_name'].encode("ascii" , "ignore"),
				content['statuses'][x]['user']['name'].encode("ascii" , "ignore"),
				content['statuses'][x]['user']['followers_count'],
				content['statuses'][x]['user']['friends_count'],
				content['statuses'][x]['user']['favourites_count'],
				content['statuses'][x]['user']['statuses_count'],
				content['statuses'][x]['user']['geo_enabled'],
				content['statuses'][x]['user']['profile_background_image_url'].encode("ascii" , "ignore"),
				content['statuses'][x]['user']['profile_image_url'].encode("ascii" , "ignore"),
				
				]
				# print s
				# for i in range(0 , len(s)):
					# s[i] = unicode(s[i]).encode("utf-8")
			
				# print s
				f.writerow(s)
				# f.writerow(s)
				# unicode(content['statuses'][x]['user']['screen_name']).replace("\/","/"),
				# unicode(content['statuses'][x]['user']['name'] , errors='ignore'),
				# str(content['statuses'][x]['geo']['coordinates'][0]) + ',' + str(content['statuses'][x]['geo']['coordinates'][1]),
				# content['statuses'][x]['place']['full_name'],
				# content['statuses'][x]['place']['country'].encode("utf-8")
		
			last_index = len(content['statuses']) -1
			min_id = content['statuses'][last_index]['id']
			max_id = content['statuses'][0]['id']
			min_id = min_id -1

			i+=1
	fp.close()
	
fetch_tweets_till_date()

#writing to json file	
# closing the file after writing the data to it
# out_file = open("test.json","a")
# json.dump(content,out_file, indent = 4)
# out_file.close()

		
'''
# Saving the data in a csv file:

f = open("test.csv",'wb+')

# initializing the header row

f.writerow (["tweet ID","user ID","tweet coordinates",
			"friend_Count","user location","geo_enabled",
			"Screen name","user name","user coordinates
			"place tagged","place_Country","place coordinates"])

for x in range(0 , len(content['statuses'])):
	f.writerow(
	[content['statuses'][x]['id'],
	content['statuses'][x]['user']['id']
	content['statuses'][x]['coordinates']['coordinates'],
	content['statuses'][x]['user']['friends_count'],
	content['statuses'][x]['user']['location'],
	content['statuses'][x]['user']['geo_enabled'],
	content['statuses'][x]['user']['screen_name'],
	content['statuses'][x]['user']['name'],
	content['statuses'][x]['geo']['coordinates'],
	content['statuses'][x]['place']['full_name'],
	content['statuses'][x]['place']['country'],
	content['statuses'][x]['place']['bounding_box']['coordinates'],
	])
f.close()


'''

		
		
		

'''
5) twitter API for Jan 2013 and July 2013. Everytweet has a date
'''