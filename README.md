# Track-and-Trace-system 
Used on a medicine production line 
This project is a base module that can be customized for specific purposes.

Youtube link : https://youtu.be/wrTnvzPaxEU

In this project, my role was to establish communication with a microcontroller via a Python app, with the microcontroller responding to any action such as rejection or approval in the production line.

![mainboard](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/1661ed71-993d-4d11-b330-db9947aa2552)





## Python code:

This code is a demonstration of the app code that is responsible for of processing the image from the camera. When the object is detected by the microcontroller, the first section decodes the QR code, and the second section extracts the text from a frame saved as an image.The text from the QR code is then compared to the text from the captured image to make a decision.
The code communicates with the serial library by specifying the port and the baud rate.


## Microconntroller code:

This code is responsible for the app code's actions and also sends a string to the app that acts as a trigger to notify the app code when an object is detected using an IR sensor.

## Hardware circuit:

This circuit is designed to have:
* 4 output relay
* 2 IR sesonrs
* RGBA 12v output connection
* 12v, 5v and GND output
* Input power 24V

## System schematic:
![image](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/7e619932-76c7-426c-817d-39d6ff9154fb)

## Pico pinout connection:
![image](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/baa082e0-c604-4582-9908-7acffde2ccbc)

## layout design:
![image](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/e3f37bb9-a03d-497c-9a8e-2cc7e5e5ec9f)

## Crcuit:
![20231010_012355](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/3622fbad-0d12-4fd2-acd1-77856ea3db17)

## Test:

![image](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/a69f3452-2415-4148-bbd2-31eb7afeb76b)

![image](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/7d03d2d4-3dcf-4039-85ad-32173d3bd963)

![image](https://github.com/Mo-Elshamy/Track-and-Trace-system/assets/121442515/9e8985f4-6753-4006-8b1b-2e156c9f72a6)


