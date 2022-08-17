# importing requests for communicating with the API
import requests
# importing json for working with json files and data
import json


# importing urllib3 for disabling warnings
import urllib3

# disabling warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# setting the sensor url
#sensor_url = "https://192.168.178.71/api/dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa/sensors/3"

sensor_url = "https://192.168.178.71/api/JoSOxXkKb6sVDmTNEVsGel3sFh0wehyC3WHv0oAv/sensors/3"


def check_motion():

    # getting all the sensor data (raw json format)
    sensor_data = requests.get(sensor_url, verify=False)

    # storing the data in a variable and filtering the value of "presence"
    output = sensor_data.json()["state"]["presence"]

    # returning the current presence state (boolean value)
    return output
