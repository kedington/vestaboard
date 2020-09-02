import json
import requests
from test_api import update_text

with open('wordnik_apikey', 'r') as infile:
    for line in infile:
        api_key = line.strip()

url = "http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={}".format(api_key)

response = requests.request("GET", url)

print(response.text)

data = json.loads(response.text)

update_text(data['word'] + ': ' + [d['text'] for d in data['definitions']][0])

