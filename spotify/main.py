from functions import check_description
from datetime import datetime
import time as t


def append(message):
    f = open("log.txt", "a")
    f.write(f"{message}")
    f.close()


def read():
    f = open("log.txt", "r")
    print(f.read())


data_elias = False
data_katya = False

while True:
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    description_katya = check_description("6ldkeSY1xLuN85t3kWbWY9")

    description_elias = check_description("3VzX8SdzBAgss9gEfN381e")

    if description_katya != data_katya:
        # logging.debug(description_katya)
        # print(description_katya)
        append(f"\n{time} | {description_katya}")
        data_katya = description_katya

    if description_elias != data_elias:

        # print(description_elias)
        append(f"\n{time} | {description_elias}")
        data_elias = description_elias

    t.sleep(1)
