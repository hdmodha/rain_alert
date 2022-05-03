import requests
import smtplib

api_key = "<your-api-key>"
parameters = {
    "lat": 21.1667,
    "lon": 72.8333,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False
for hour_data in weather_slice:
    id_code = hour_data['weather'][0]['id']
    if int(id_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="<your-email>", password="<your-password>")
        connection.sendmail(from_addr="<your-email>", to_addrs="<receiver-email>",
                            msg=f"Subject: Rain Alert\n\n"
                                f"Bring your Umbrella, it will rain today!!!")
