#import all nessesary processes
import requests
import serial
import time
import math
#what usb port the arduino connects to
arduino = serial.Serial("COM3", 9600)
#insert your lat and lon using https://www.gps-coordinates.net/
my_lat = 57.15386291492336
my_lon = -2.293427928384182
#this api gets the iss's real time location
iss_url = "https://api.wheretheiss.at/v1/satellites/25544"
#some complex math to calculate the bearing to the iss
def calculate_bearing(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    diff_lon = math.radians(lon2 - lon1)
    x = math.sin(diff_lon) * math.cos(lat2)
    y = (math.cos(lat1) * math.sin(lat2) -
         math.sin(lat1) * math.cos(lat2) * math.cos(diff_lon))
    bearing = math.atan2(x, y)
    bearing = math.degrees(bearing)
    return (bearing + 360) % 360
#the direction is assigned depending on bearing angle
def bearing_to_direction(angle):
    if angle >= 337.5 or angle < 22.5:
        return "N"
    elif angle < 67.5:
        return "NE"
    elif angle < 112.5:
        return "E"
    elif angle < 157.5:
        return "SE"
    elif angle < 202.5:
        return "S"
    elif angle < 247.5:
        return "SW"
    elif angle < 292.5:
        return "W"
    else:
        return "NW"
#constant iss positional updates
while True:
    iss_data = requests.get(iss_url).json()
    iss_lat = iss_data["latitude"]
    iss_lon = iss_data["longitude"]
    bearing = calculate_bearing(my_lat, my_lon, iss_lat, iss_lon)
    direction = bearing_to_direction(bearing)
    print("Bearing:", round(bearing, 1), "Direction:", direction)
    arduino.write((direction + "\n").encode())
    time.sleep(1)
