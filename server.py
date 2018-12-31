from socket import *
import cv2
import numpy
import struct

HOST = '127.0.0.1'
PORT = 8002
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

while True:
    tcpclient, addr = server.accept()
    print(addr)

    data = tcpclient.recv(struct.calcsize('<L'))
    L = struct.unpack ('<L', data)[0]
    print(L)

    data = tcpclient.recv(L)
    print('length of data', len(data))
    if len(data) < L:
        data += tcpclient.recv(L-len(data))

    img_array = numpy.array(bytearray(data), dtype = numpy.uint8)
    img = cv2.imdecode (img_array, cv2.IMREAD_ANYCOLOR )
    cv2.imshow ('Server:image', img)
    if cv2.waitKey(1) == ord ('q'):
        break
    
server.close()
print('server close')
