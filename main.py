
import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
CITY = "Brisbane"
auth_token = "23a5281f341d3b6711fe87c4c18098f1"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
                "q":CITY,
                "appid":API_KEY,
                "cnt":4
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
response = requests.get(OWM_Endpoint,params= parameters)
response.raise_for_status()
data = response.json()
check = data['list'][1]['weather'][0]['id']
count = 0
will_rain = False
for c in data['list']:

    check = data['list'][count]['weather'][0]['id']
    if check < 700:
        print("Its going to rain")
        will_rain = True
    else:
        print("Its not going to rain")
    count += 1

if will_rain:
    message = client.messages.create(
        body = "Its going  to rain today. Remember to bring an ☂️",
        from_= "+16062499868",
        to ="+61433748911",
)
print(message.status)

