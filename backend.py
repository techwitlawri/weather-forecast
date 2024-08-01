import requests

API_KEY = "7481add0c7c161e08ed21b91059b5e2a"

def get_data(place, forecast_days= None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Nigeria", forecast_days= 3))