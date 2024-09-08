import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response)
# print(response.status_code)   #Gives the status code only
print(response.json())  #Gives us the JSON output, basically the response that the API should return.


# API with parameters

parameter = {

    "latitude": 45.0,
    "longitude": -122.05

}

response = requests.get("http://api.open-notify.org/iss-now.json", params= parameter)
print(response.status_code)
print(response.json())


