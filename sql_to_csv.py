from framework import *
import csv,codecs, unicodedata

def convert_sql_to_csv():

    file_name = "tweets.csv"
    with (codecs.open(file_name , 'w',encoding ='utf-8',errors='ignore')) as fp:
        f = csv.writer(fp , delimiter=',')
        f.writerow (["id" , "tweet_Id","Tweet_created_at","tweet_favorite_count","tweet_latitude" , "tweet_longitude",
					"tweet_language","tweet_retweet_count","tweet_retweeted","tweet_source","tweet_text",
					"user_contributors_enabled", "user_created_at","user_description", "user_Id","user_friend_count",
					"user_time_zone", "user_location", "user_geo_enabled" , "user_screen_name", "user_name","user_follower_count",
					"user_favorities_count", "user_status_count", "user_language",
					"user_profile_background_image_url", "user_profile_image_url", "place_coordinate_lat_A", "place_coordinate_lng_A",
					"place_coordinate_lat_B","place_coordinate_lng_B","place_coordinate_lat_C","place_coordinate_lng_C","place_coordinate_lat_D",
					"place_coordinate_lng_D","place_country",
					"place_full_name", "place_type"])
        tweets = m.fetch_all_tweets()

        for tweet in tweets:
            f.writerow(tweet)

convert_sql_to_csv()