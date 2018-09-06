import requests
import csv

api_url = 'https://earthquake.usgs.gov/fdsnws/event/1/'
api_method = 'query?'
api_method_2 = 'count?'
api_format = 'format=geojson'
api_starttime = '2018-09-06 12:00:00'
api_minlatitude ='5.870'
api_minlongitude ='-180.000'
api_maxlatitude ='71.390'
api_maxlongitude ='-66.900'

query_url ='{0}{1}{2}&starttime={3}&minlatitude={4}&maxlatitude={5}&minlongitude={6}&maxlongitude={7}'.format(api_url,api_method,api_format,api_starttime,api_minlatitude,api_maxlatitude,api_minlongitude,api_maxlongitude)
count_url ='{0}{1}{2}&starttime={3}&minlatitude={4}&maxlatitude={5}&minlongitude={6}&maxlongitude={7}'.format(api_url,api_method_2,api_format,api_starttime,api_minlatitude,api_maxlatitude,api_minlongitude,api_maxlongitude)

response = requests.get(count_url)
data = response.json()
data

response = requests.get(query_url)
data = response.json()
data

import twitter
api=twitter.Api(consumer_key='twitter consumer key',
                consumer_secret='twitter consumer secret',
                access_token_key='the_key_given',
                access_token_secret='the_key_secret')

import time
for i in range(0,len(data['features'])):
    timestamp=data['features'][i]['properties']['time']/1000
    time_local=time.localtime(timestamp)
    dt=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    status=api.PostUpdate('A %d magnitude earthquake occurred on %s,at %d'%(data['features'][i]['properties']['mag'],data['features'][i]['properties']['place'],dt))
    print(status)