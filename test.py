from framework import *
import csv,codecs, unicodedata
import sys, os

MAX_TIME_PASSED = 60*30 # 30 minutes

def fetch_tweets_till_date() :
	
	i = 0
	
	min_id = None
	with (codecs.open('test.csv' , 'w',encoding ='utf-8',errors='ignore')) as fp:
		f = csv.writer(fp , delimiter=',')

		f.writerow (["tweet_Id","Tweet_created_at","tweet_favorite_count","tweet_latitude" , "tweet_longitude",
					"tweet_language","tweet_retweet_count","tweet_retweeted","tweet_source","tweet_text",
					"user_contributors_enabled", "user_created_at","user_description", "user_Id","user_friend_count", 
					"user_time_zone", "user_location", "user_geo_enabled" , "user_screen_name", "user_name","user_follower_count",
					"user_friend_count", "user_favorities_count", "user_status_count", "user_language", 
					"user_profile_background_image_url", "user_profile_image_url", "place_coordinate_lat_A", "place_coordinate_lng_A",
					"place_coordinate_lat_B","place_coordinate_lng_B","place_coordinate_lat_C","place_coordinate_lng_C","place_coordinate_lat_D",
					"place_coordinate_lng_D","place_country",
					"place_full_name", "place_type"])
		
		t = TwitterFW()
		url ="https://api.twitter.com/1.1/search/tweets.json"
	
		geocode = "40.717728,-74.0021647,500mi"

		until = "2015-07-11"
		prev_time = None
		
		while (1):
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
										'max_id' : str(min_id) ,
										'until' : "2015-07-06"
										}
									)
			
			# printing the contents
			# pprint(json.loads(content))
			content = unicode(content,"utf-8")
			content = json.loads(content)
			# pprint(content)
			
			if not content.get('statuses' , None):
				print("End of tweets encountered.")
				return
	
			# for tweet in content['statuses'] :
			# 	print "Tweet id is " + str(tweet['id']) + " by " + str(tweet['user']['screen_name'])

			for x in range(0 , len(content['statuses'])):
				try :
					tweet_time = content['statuses'][x]['created_at']
					tweet_timestamp = twitter_date_to_timestamp(content['statuses'][x]['created_at'])
					
					if (prev_time is not None) :
						if (tweet_timestamp - prev_time > MAX_TIME_PASSED) :
							return
					
					else :
						prev_time = tweet_timestamp
					
					lat_lng1 = content['statuses'][x].get('coordinates',None)
					if lat_lng1 :
						lat_lng1 = lat_lng1.get('coordinates')
						# lat_lng_str = str(lat_lng[0]) + '-' + str(lat_lng[1])
						lat1_str = str(lat_lng1[0])
						lng1_str = str(lat_lng1[1])
					else :
						# lat_lng_str = ''
						lat1_str = ''
						lng1_str = ''
						
					try :
						lat_lng2 = content['statuses'][x]['place']['bounding_box']['coordinates']
					except Exception as e :
						lat_lng2 = None
						
					if lat_lng2 :
						# print lat_lng2[0]
						# lat_lng2 = lat_lng2.get('coordinates')
						# [[[-74.026675, 40.683935], [-73.910408, 40.683935], [-73.910408, 40.877483], [-74.026675, 40.877483]]]
						lat_lng2 = lat_lng2[0]

						latA_str = str(lat_lng2[0][0])
						lngA_str = str(lat_lng2[0][1])
						latB_str = str(lat_lng2[1][0])
						lngB_str = str(lat_lng2[1][1])
						latC_str = str(lat_lng2[2][0])
						lngC_str = str(lat_lng2[2][1])
						latD_str = str(lat_lng2[3][0])
						lngD_str = str(lat_lng2[3][1])
					
					else:
						latA_str = ''
						lngA_str = ''
						latB_str = ''
						lngB_str = ''
						latC_str = ''
						lngC_str = ''
						latD_str = ''
						lngD_str = ''
					
					if content['statuses'][x].get('place' , None):
						place = content['statuses'][x]['place']['country']
						country = content['statuses'][x]['place']['full_name']
						place_type = content['statuses'][x]['place']['place_type']
					else :
						place = ''
						country = ''
						place_type = ''
						
					s = [
					content['statuses'][x]['id'],
					content['statuses'][x]['created_at'],
					content['statuses'][x]['favorite_count'] ,
					lng1_str, # reverse lat and long
					lat1_str, # reverse lat and long
					content['statuses'][x]['lang'],
					content['statuses'][x]['retweet_count'],
					content['statuses'][x]['retweeted'],
					content['statuses'][x]['source'].encode("ascii" , "ignore"),
					content['statuses'][x]['text'].encode("ascii" , "ignore"),
					content['statuses'][x]['user']['contributors_enabled'],
					content['statuses'][x]['user']['created_at'],
					content['statuses'][x]['user']['description'].encode("ascii" , "ignore"),
					content['statuses'][x]['user']['id'] ,
					content['statuses'][x]['user']['friends_count'],
					content['statuses'][x]['user']['time_zone'],
					content['statuses'][x]['user']['location'].encode("ascii" , "ignore"),
					content['statuses'][x]['user']['geo_enabled'],
					content['statuses'][x]['user']['screen_name'].encode("ascii" , "ignore"),
					content['statuses'][x]['user']['name'].encode("ascii" , "ignore"),
					content['statuses'][x]['user']['followers_count'],
					content['statuses'][x]['user']['friends_count'],
					content['statuses'][x]['user']['favourites_count'],
					content['statuses'][x]['user']['statuses_count'],
					content['statuses'][x]['user']['lang'],
					content['statuses'][x]['user']['profile_background_image_url'].encode("ascii" , "ignore"),
					content['statuses'][x]['user']['profile_image_url'].encode("ascii" , "ignore"),
					latA_str,
					lngA_str,
					latB_str,
					lngB_str,
					latC_str,
					lngC_str,
					latD_str,
					lngD_str,
					place ,
					country ,
					place_type
					]
					# for i in range(0 , len(s)):
						# s[i] = unicode(s[i]).encode("utf-8")
			
					#print s
				
					f.writerow(s)
					
				except Exception as e:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					print str(e) , exc_tb.tb_lineno
					continue

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


'''	
