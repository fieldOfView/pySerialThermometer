# pixelbar-pySerialThermometer
A flask-based server for the "Pim" temperature sensor connected via USB serial.

## setup
The script uses pySerial to communicate with the STM32 controller board. This can be installed with the following command:
```
python3 -m pip install pyserial
```
The user must be privileged to use serial devices. As a better alternative than to run the command as root, add the user to the `dialout` group:
```
sudo adduser $USER dialout
```

A systemd unitfile is provided for convencience. To install it to your system, do the following:
```
sudo ln -sf ~/pySerialThermometer/system/serialthermometer.service /etc/systemd/system/serialthermometer.service
sudo systemctl daemon-reload
sudo systemctl enable serialthermometer.py
sudo systemctl start serialthermometer.py
```
