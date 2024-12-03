import requests
from twilio.rest import Client

#twilio
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
CLIENT = Client(account_sid, auth_token)

#open weather api
MY_KEY = os.getenv("MY_KEY")
PH_LATITUDE = "12.879721"
PH_LONGITUDE = "121.774017"

parameters = {
    "lat": PH_LATITUDE,
    "long": PH_LONGITUDE,
    "appid": MY_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=12.879721&lon=121.774017&appid=07caee0baee9414850fa0e793fb77d46", params=parameters)
response.raise_for_status()
weather_data = response.json()


# if data["list"][0]["weather"][0]['id'] < 700:
#     print("Bring Umbrella")
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = CLIENT.messages.create(
        body = "It will rain today, please bring your umbrella ☂️",
        from_= "+17753209620",
        to="+639472084004",
    )

    print(message.sid)
