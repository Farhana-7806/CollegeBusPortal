import serial
gps = serial.Serial("COM3", baudrate=9600, timeout=1)
line = gps.readline().decode("utf-8", errors="ignore")

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(1)
conn, _ = server.accept()
line = conn.recv(1024).decode("utf-8", errors="ignore")

import pynmea2
msg = pynmea2.parse(line)
print(msg.latitude, msg.longitude)

import folium
map = folium.Map(location=[msg.latitude, msg.longitude], zoom_start=15)
folium.Marker([msg.latitude, msg.longitude], popup="Current Location").add_to(map)
map.save("gps_map.html")
