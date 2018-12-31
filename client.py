from socket import *
import cv2
import numpy
import struct

HOST = '127.0.0.1'
PORT = 8002
ADDR = (HOST, PORT)

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

image = cv2.imread (r'C:\Users\daniel.gee\Pictures\image.jpg')

img_str = cv2.imencode('.jpg', image)[1].tostring()
print(len(img_str))

L = struct.pack ('<L', len(img_str))
client.send(L)

client.send (img_str)
client.close()
print('client close')
