import json
import requests

# https://docs.vestaboard.com/methods
board_id = "a91c3c15-2d5b-4167-aa65-192f7ccb3b45"
url = "https://platform.vestaboard.com/subscriptions/{}/message".format(board_id)

secrets = ''
with open('secret', 'r') as infile:
    for line in infile:
        secrets += line

key, secret = secrets.split()
        
headers = {"X-Vestaboard-Api-Key": key,
           "X-Vestaboard-Api-Secret": secret}

def update_text(message):
    body = {"text": message} 

    response = requests.request("POST", url, headers=headers, data=json.dumps(body))

    print(response.text)


def update_board(char_array):
    body = {"characters": char_array} 

    response = requests.request("POST", url, headers=headers, data=json.dumps(body))

    print(response.text)


