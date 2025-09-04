# gps_server.py
import socket
import threading
import pynmea2
from flask import Flask, render_template_string

# Store latest positions per device
gps_data = {}

def handle_device(device_id, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(1)
    print(f"[{device_id}] Listening on port {port}")

    conn, _ = server.accept()
    while True:
        try:
            line = conn.recv(1024).decode("utf-8", errors="ignore")
            if line.startswith("$GPGGA"):
                msg = pynmea2.parse(line)
                gps_data[device_id] = (msg.latitude, msg.longitude)
        except Exception as e:
            print(f"[{device_id}] Error:", e)

# Start threads for each GPS device
devices = {
    "Bus_1": 7000,
    "Bus_2": 7001,
    "Bus_3": 7002,
   
}

for device_id, port in devices.items():
    threading.Thread(target=handle_device, args=(device_id, port), daemon=True).start()