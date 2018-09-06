import requests
import csv
url='https://api.data.gov.hk/v1/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fhk.centanet.com%2Fopendata%2FCCI%2520Estate%2520for%2520Opendata.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%2C%22filters%22%3A%5B%5B5%2C%22ct%22%2C%5B%22%E4%B9%9D%E9%BE%8D%22%5D%5D%5D%7D'
response=requests.get(url)
data=response.json()
with open('property.csv','w',newline='')as f:
    writer=csv.writer(f)
    header=['c_estate', 'e_estate', 'pc_addr', 'pe_addr', 'scp_mktc', 'scp_mkte', 'min_opdate', 'max_opdate', 'blgcount', 'pc_dev', 'pe_dev', 'facilities_c', 'facilities_e', 'url']
    writer.writerow(header)

    for i in range(0,len(data['rows'])):
        if data['rows'][i][6]>=2000:
            writer.writerow(data['rows'][i])
    
    f.close()