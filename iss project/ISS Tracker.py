import requests
import serial
arduino = serial.Serial('COM3', 9600)
url = "https://ipapi.co/json/"
response = requests.get(url)
data = response.json()
myLatitude = data["latitude"]
myLongitude =data["longitude"]
url = "https://api.wheretheiss.at/v1/satellites/25544"
def getDirection(issLatitude,issLongitude,myLatitude,myLongitude):
    latitudeDifference=issLatitude-myLatitude
    longitudeDifference=issLongitude-myLongitude
    if abs(latitudeDifference)>abs(longitudeDifference):
        if latitudeDifference>0:
            return"N"
        else:
            return "S"
    else:
        if longitudeDifference>0:
            return"E"
        else:
            return "W"
while 1==1:
    response = requests.get(url)
    data = response.json()
    issLatitude = data["latitude"]
    issLongitude = data["longitude"]
    timestamp = data["timestamp"]
    direction=getDirection(issLatitude,issLongitude,myLatitude,myLongitude)
    print("ISS direction : ", direction)
    print("Longitude : ", issLongitude, "Latitude : ", issLatitude,"Last Checked : ",timestamp)
    arduino.write(direction.encode())
