import requests
from datetime import datetime

TOKEN = "" #Enter a Token
USERNAME = "" #Enter a username
GRAPH_ID = "" #Enter GraphID

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "Running graph",
    "unit": "miles",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()

endpoint_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you run today? ")
}

response = requests.post(url=pixel_endpoint, json=endpoint_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_dic = {
    "quantity": "5.50"
}

#response = requests.put(url=update_endpoint, json=new_pixel_dic, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)