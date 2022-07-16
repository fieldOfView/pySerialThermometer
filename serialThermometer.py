#!/usr/bin/python
import serial
import time
import json
import os
from flask import Flask, request, jsonify

PORT_NUMBER = 8080

app = Flask(__name__)

@app.route('/temp.json', methods=['GET'])
def getData():
    ser.write(b'g')

    retdata = ser.readline().rstrip()
    print(retdata)
    retdata = retdata.split(b",")

    if (len(retdata) != 8):
        return ("malformed data from serial port: " + repr(retdata), 400)


    acceltijd = retdata[0]
    acx = retdata[1]
    acy = retdata[2]
    acz = retdata[3]
    gyx = retdata[4]
    gyy = retdata[5]
    gyz = retdata[6]
    acceltemp = retdata[7]

    data = {'AccelTijd':acceltijd, 'Acx':acx, 'Acy':acy, 'Acz':acz, 'Gyx':gyx, 'Gyy':gyy, 'Gyz':gyz, 'AccelTemp':acceltemp}

    return jsonify(data)


device = ""
for i in range(0,9):
    device_path = "/dev/ttyUSB%d" % i
    if os.path.exists(device_path):
        device = device_path
        break
if device == "":
    print("No ttyUSB device found; is the Pim sensor board connected?")
    exit(1)


ser = serial.Serial(device, baudrate=115200, timeout=0)
time.sleep(2)
print(ser.readline())
print(ser.readline())

app.run(host="0.0.0.0", port=PORT_NUMBER)
ser.close()
