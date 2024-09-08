## 1. Fetching Astronaut Information
The script sends a GET request to the http://api.open-notify.org/astros.json API endpoint to retrieve information about astronauts currently in space. The response is printed in JSON format.

import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response)
# print(response.status_code)   #Gives the status code only
print(response.json())  #Gives us the JSON output, basically the response that the API should return.

## 2. Retrieving ISS Location
The script sends a GET request to the http://api.open-notify.org/iss-now.json API endpoint with specified latitude and longitude parameters. The current location of the ISS is retrieved and printed in JSON format.

# API with parameters

parameter = {
    "latitude": 45.0,
    "longitude": -122.05
}

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameter)
print(response.status_code)
print(response.json())


## How to Run
1. Save the script to a file, e.g., api_interaction.py.

2. Run the script using Python:
      python api_interaction.py

3. The script will output the JSON responses from the APIs to the console.

## License
This project is licensed under the MIT License.




