import datetime

file_name = 'test' + datetime.datetime.now().time().isoformat() + '.csv'
print file_name