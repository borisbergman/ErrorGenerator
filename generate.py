import socket
import serial
import threading
import time
from threading import Timer
import math
import struct
import binascii
import random
import sys
import csv
from ErrorCodes import *

#ser = serial.Serial(1, 38400, timeout=1)

#ser.write([0x01,0x81 ,0x0A,0x1F,0x01, 0x05,0x21,0x00, 0x10,0xE2])


while 1:

 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 try:
     s.bind(('', 1002))
     print('socket bind complete')
 except socket.error as inst:
     print('socket bind failed. No network available:', inst)
 else:
     s.listen(10)
     print('socket now listening')
    # while 1:
     conn, address = s.accept()
     print('Connected with ' + address[0] + ':' + str(address[1]))
     last_ip_digit = int(conn.getsockname()[0].split('.')[3])

 while(1):
  print ("Enter command to send"),
  try:
   num = int(input())
   print(erros[num])
   conn.sendall(bytes(erros[num]))
  except:
   break


