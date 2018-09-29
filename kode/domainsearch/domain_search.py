#!/usr/local/bin/python3

from datetime import datetime, date, timedelta
import urllib.request
import zipfile

today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday = (datetime.strftime(yesterday, '%Y-%m-%d'))

URL='https://whoisds.com/whois-database/newly-registered-domains/' + yesterday + '.zip/nrd'

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(URL , yesterday + '.zip')

temp = yesterday + '.zip'

zip = zipfile.ZipFile(temp)
zip.extractall(yesterday)
zip.close()


print(yesterday)

file_data = open(yesterday + '/domain-names.txt', 'r')
lines = file_data.readlines()
#print(lines[:-1])

search_data = open("./temp/search_list.txt", 'r')
keywords = search_data.readlines()
#print(keywords[:-1])

for keys in keywords:
   key =  keys.strip()
   for domains in lines:
     domain = domains.strip()
     A1 = domain.find(key)
     if A1!=-1:
      print(domain)

file_data.close()
search_data.close()
