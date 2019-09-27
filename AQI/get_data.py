import requests
import pandas as pd


offset = 0
with open("keys/data_gov_api_key.txt") as f:
    api_key = f.read()
print("api_key",api_key)
base_url  = "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69"
# api_key = "Your API Key"
data_format = "json"
offset = 0

# url = "{}?api-key={}&format={}&offset={}".format(base_url,api_key,data_format, offset)
data = []
retrieved_rows = 1
while retrieved_rows < 100000:
    
    url = "{}?api-key={}&format={}&offset={}".format(base_url,api_key,data_format, offset)
    r = requests.get(url)
    response = r.json()
    retrieved_rows += len(response['records'])
    data.extend(response['records'])
    offset = 100 #len(response['records'])
    print("retrieved_rows", retrieved_rows)

df = pd.DataFrame(data)  
# print(df.head())
last_update = df.last_update[0]
last_update = "-".join(last_update.split(" "))
last_update = "-".join(last_update.split(":"))
print(last_update)
df.to_csv("data/aqi-{}.csv".format(last_update))

