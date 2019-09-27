import requests
import pandas as pd


offset = 0

base_url  = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69"
api_key = "Your API Key"
data_format = "json"
offset = 0

url = "{}?api-key={}&format={}&offset={}".format(base_url,api_key,data_format, offset)

data = []

retrieved_rows = 1
while retrieved_rows < 200000:
# print(url)
    url = "{}?{}&format={}&offset={}".format(base_url,api_key,data_format, offset)
    r = requests.get(url)
    # print (r)
    response = r.json()
    # print(data['records'])
    retrieved_rows += len(response['records'])
    # if retrieved_rows == 0 :
    #     break
    # else:
    data.extend(response['records'])
    offset = 100 #len(response['records'])
    print("retrieved_rows", retrieved_rows)

df = pd.DataFrame(data)  
print(df.head())
df.to_csv("aqi.csv")

