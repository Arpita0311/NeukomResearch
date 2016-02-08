from framework import twitter_date_to_datetime , Model

# print twitter_date_to_datetime("Sun Aug 02 22:05:45 +0000 2015")
m = Model()
m.save_times_for_tweets()

# file_name = 'test' + datetime.datetime.now().time().isoformat() + '.csv'
# print file_name