import requests
import csv
url='https://api.douban.com/v2/movie/in_theaters'
response=requests.get(url)
data=response.json()
with open('movies.csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['title']
    writer.writerow(header)
for i in range(0,len(data['subjects'])):
    writer.writerow([data['subjects'][i]['title']])

