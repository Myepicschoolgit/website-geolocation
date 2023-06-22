import requests
import socket
from colorama import Fore, Back, Style, init

api_key = "API KETY" # go to https://ipgeolocation.io/ and sign up out your api key here
base_url = "https://api.ipgeolocation.io/ipgeo"

def get_ip_info(ip):
    params = {
        "apiKey": api_key,
        "ip": ip
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

website = input("Website: ")
websiteip = socket.gethostbyname(website)
ip_address = websiteip

ip_info = get_ip_info(ip_address)

def print_in_box(content):
    lines = content.splitlines()
    max_length = max(len(line) for line in lines)
    horizontal_line = "╔" + "═" * (max_length + 2) + "╗"
    print(horizontal_line)
    for line in lines:
        if line.strip() == "":
            continue
        print("║ " + line.ljust(max_length) + " ║")
    print("╚" + "═" * (max_length + 2) + "╝")

output = """
Website: {wsite}
{line}
IP Address: {ip}
Country: {country_name}
Region: {state_prov}
City: {city}
Latitude: {latitude}
Longitude: {longitude}
Calling Code: {calling_code}
Zipcode: {zipcode}
ISP: {isp}
""".format(wsite=website, line="---------------------", ip=ip_info["ip"], country_name=ip_info["country_name"],
           state_prov=ip_info["state_prov"], city=ip_info["city"],
           latitude=ip_info["latitude"], longitude=ip_info["longitude"],
           calling_code=ip_info["calling_code"], zipcode=ip_info["zipcode"],
           isp=ip_info["isp"])

print_in_box(output)