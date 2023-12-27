import urllib.request
import xml.etree.ElementTree as ET
from tabulate import tabulate


def getInfo():
    URL = "https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=xml&tzshift=0"
    print("URL request is: " + URL)
    print("Data format is: XML")
    # Make the request and save the response as a string.
    connection = urllib.request.urlopen(URL)
    responseString = connection.read().decode()
    return responseString

# Parse XML
root = ET.fromstring(getInfo())

# Extract data and create a list of dictionaries
data_list = []
for data_elem in root.findall(".//data"):
    data_dict = {
        "Timepoint": data_elem.get("timepoint"),
        "Cloudcover": data_elem.find("cloudcover").text,
        "Seeing": data_elem.find("seeing").text,
        "Transparency": data_elem.find("transparency").text,
        "Lifted Index": data_elem.find("lifted_index").text,
        "RH2M": data_elem.find("rh2m").text,
        "Wind Direction": data_elem.find("wind10m_direction").text,
        "Wind Speed": data_elem.find("wind10m_speed").text,
        "Temperature": data_elem.find("temp2m").text,
        "Precipitation Type": data_elem.find("prec_type").text,
    }
    data_list.append(data_dict)

# Create a table and print it
table_headers = [
    "Timepoint",
    "Cloudcover",
    "Seeing",
    "Transparency",
    "Lifted Index",
    "RH2M",
    "Wind Direction",
    "Wind Speed",
    "Temperature",
    "Precipitation Type",
]
table_data = [[data_dict[key] for key in table_headers] for data_dict in data_list]

table = tabulate(table_data, headers=table_headers, tablefmt="pretty")
print(table)
