import urllib.request
import json
from tabulate import tabulate


def getInfo():
    URL = "https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0"
    print("URL request is: " + URL)
    print("Data format is: JSON")
    # Make the request and save the response as a string.
    connection = urllib.request.urlopen(URL)
    responseString = connection.read().decode()
    return responseString

data = json.loads(getInfo())

# Extracting relevant information
table_data = []
for entry in data["dataseries"]:
    timepoint = entry["timepoint"]
    cloudcover = entry["cloudcover"]
    seeing = entry["seeing"]
    transparency = entry["transparency"]
    lifted_index = entry["lifted_index"]
    rh2m = entry["rh2m"]
    wind_direction = entry["wind10m"]["direction"]
    wind_speed = entry["wind10m"]["speed"]
    temp2m = entry["temp2m"]
    prec_type = entry["prec_type"]

    table_data.append(
        [
            timepoint,
            cloudcover,
            seeing,
            transparency,
            lifted_index,
            rh2m,
            wind_direction,
            wind_speed,
            temp2m,
            prec_type,
        ]
    )

# Creating a text table
headers = [
    "Timepoint",
    "Cloud Cover",
    "Seeing",
    "Transparency",
    "Lifted Index",
    "RH2m",
    "Wind Direction",
    "Wind Speed",
    "Temp2m",
    "Precipitation Type",
]
table = tabulate(table_data, headers, tablefmt="pretty")

print(table)
