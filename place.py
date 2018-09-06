import requests
url1='https://maps.googleapis.com/maps/api/geocode/json?address=new%20york'
response1=requests.get(url1)
data1=response1.json()
lat1=data1['results'][0]['geometry']['location']['lat']
lng1=data1['results'][0]['geometry']['location']['lng']
url2='https://maps.googleapis.com/maps/api/geocode/json?address=Hong%20Kong'
response2=requests.get(url2)
data2=response2.json()
lat2=data2['results'][0]['geometry']['location']['lat']
lng2=data2['results'][0]['geometry']['location']['lng']
import math
import numpy
a=numpy.pi/180
def haversin(x):
    return (1-math.cos(x))/2
    
c=haversin(lat1*a-lat2*a)+math.cos(lat1*a)*math.cos(lat2*a)*haversin(lng1*a-lng2*a)
n=1-2*c
d=math.acos(n)*6371
print('the distance between HONGKONG and New York is:',d,'km')