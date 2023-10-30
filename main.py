import serial   #serial library to comunicate to the microcontroller
import cv2
import os
from pyzbar import pyzbar    #Qrcode library
import pytesseract as tess   #text library
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  #the path differ from pc to another
from PIL import Image


camera = cv2.VideoCapture(1)  #camera used for capturing (0 is the built in camera)
ser = serial.Serial('COM6', 9600)  # Replace 'COM1' with the actual port name


while True:

    while ser.in_waiting >= 0:

        msg = ser.readline().decode('utf-8').rstrip()  #read data and store it
        print(msg)


        if msg == "cap":                               #cap is send by the microcontroller when object is detected

            _, frame = camera.read()

            cv2.imwrite('test.jpg', frame)             #savig image (for text reading)

            decodedObjectes = pyzbar.decode(frame)      #Read the Qr code and store it
            decodedStrings = []

            for obj in decodedObjectes:
               QRdata = obj.data.decode('utf-8')                 # Decode the bytes object into a string
               print(" QR Data:", obj.data.decode('utf-8'))      # Print the decoded string
               decodedStrings.append(obj.data.decode('utf-8'))   # Append the decoded string to the list

            QRdata = decodedStrings
            print(QRdata)
            print("*********************************************")


            img = Image.open('test.jpg')                         
            text = tess.image_to_string(img)                     #Extracting the text from the saved img

            print("Text Data:",text)

            if QRdata and text:

                QRdata = QRdata.replace(" ", "").replace("\n", "")  
                text = text.replace(" ", "").replace("\n", "")      
            
                QRdata = QRdata.lower()
                text = text.lower()

                if QRdata == text:
                    print("accepted")
                    ser.write("accepted".strip().encode())
                else:
                    print("rejected")
                    ser.write("rejected".strip().encode())

            else:
                print("error")
                ser.write("rejected".strip().encode())

            os.remove('test.jpg')
