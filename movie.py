import requests
import csv
url='https://api.douban.com/v2/movie/in_theaters'
response=requests.get(url)
data=response.json()
with open('movies.csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['title','director','year','cast','description']
    writer.writerow(header)
    for i in range(0,len(data['subjects'])):
        if len(data['subjects'][i]['casts'])==1:
            if len(data['subjects'][i]['genres'])==1:
                writer.writerow([data['subjects'][i]['title'],data['subjects'][i]['directors'][0]['name'],data['subjects'][i]['year'],data['subjects'][i]['casts'][0]['name'],data['subjects'][i]['genres'][0]])
            elif len(data['subjects'][i]['genres'])==2:
                writer.writerow([data['subjects'][i]['title'],data['subjects'][i]['directors'][0]['name'],data['subjects'][i]['year'],data['subjects'][i]['casts'][0]['name'],data['subjects'][i]['genres'][0]+' '+data['subjects'][i]['genres'][1]])
            else:
                writer.writerow([data['subjects'][i]['title'],data['subjects'][i]['directors'][0]['name'],data['subjects'][i]['year'],data['subjects'][i]['casts'][0]['name'],data['subjects'][i]['genres'][0]+' '+data['subjects'][i]['genres'][1]+' '+data['subjects'][i]['genres'][2]])
        else:
            if len(data['subjects'][i]['genres'])==1:
                writer.writerow([data['subjects'][i]['title'],data['subjects'][i]['directors'][0]['name'],data['subjects'][i]['year'],data['subjects'][i]['casts'][0]['name']+' '+data['subjects'][i]['casts'][1]['name']+' '+data['subjects'][i]['casts'][2]['name'],data['subjects'][i]['genres'][0]])
            elif len(data['subjects'][i]['genres'])==2:
                writer.writerow([data['subjects'][i]['title'],data['subjects'][i]['directors'][0]['name'],data['subjects'][i]['year'],data['subjects'][i]['casts'][0]['name']+' '+data['subjects'][i]['casts'][1]['name']+' '+data['subjects'][i]['casts'][2]['name'],data['subjects'][i]['genres'][0]+' '+data['subjects'][i]['genres'][1]])
            else:
                writer.writerow([data['subjects'][i]['title'],data['subjects'][i]['directors'][0]['name'],data['subjects'][i]['year'],data['subjects'][i]['casts'][0]['name']+' '+data['subjects'][i]['casts'][1]['name']+' '+data['subjects'][i]['casts'][2]['name'],data['subjects'][i]['genres'][0]+' '+data['subjects'][i]['genres'][1]+' '+data['subjects'][i]['genres'][2]])