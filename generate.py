import socket
from keepAliveTimer import RepeatedTimer
from ErrorCodes import *

keep_alive = [0x01,  0x81, 0x05,  0x1E,  0xA5]


def send_keep_alive(c):
    try:
        c.sendall(bytes(keep_alive))
        print("keep alive send"),
    except:
        rt.stop()


while 1:

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 1002))
        print('socket bind complete')
    except socket.error as inst:
        print('socket bind failed. No network available:', inst)
    else:
        s.listen(10)
        print('socket now listening')
       # while 1:
        conn, address = s.accept()
        rt = RepeatedTimer(5, send_keep_alive, conn)
        print('Connected with ' + address[0] + ':' + str(address[1]))

        last_ip_digit = int(conn.getsockname()[0].split('.')[3])

        while 1:
            print("Enter command to send"),
            try:
                num = int(input())
                print(erros[num])
                conn.sendall(bytes(erros[num]))
            except:
                rt.stop()
                break


