
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
  
def api_request(query):
    #Query must be a string
    api_key = os.getenv("GOOGLE_TOKEN")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    
    r = requests.get(url + 'query=' + query +'&key=' + (api_key))
    x = r.json() 
    print(x)
    y = x['results'] 
    lst=[]
    for i in range(len(y)):
        lst.append(( y[i]))
    return lst

