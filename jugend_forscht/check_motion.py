# importing requests for communicating with the API
import requests
# importing json for working with json files and data
import json

from credentials import ip_adress, user

# setting the sensor url

sensor_url = f"http://{ip_adress}/api/{user}/sensors/3"


def check_motion():

    # getting all the sensor data (raw json format)
    sensor_data = requests.get(sensor_url)

    # storing the data in a variable and filtering the value of "presence"
    output = sensor_data.json()["state"]["presence"]

    # returning the current presence state (boolean value)
    return output
