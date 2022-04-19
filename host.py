from flask import Flask
from flask_cors import CORS
from utils.connection_types import Client
import socket
from sys import argv
from utils import logger
from threading import Thread

app = Flask(__name__)
CORS(app)

if argv[1] == '--dev':
    HOST, PORT = 'localhost', 9090
if argv[1] == '--prod':
    HOST, PORT = '0.0.0.0', 9002

### SOCKET BINDING ###
sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(5)

client_id = int()

logger.warning('DADDY STARTED ', HOST, ':', PORT)

while 'LISTENING':
    conn, addr = sock.accept()
    client_id += 1

    logger.info('CONNECTED: ', addr)
    client = Client(conn, client_id)

    handler = Thread(target=client.loop,
                     name=f"CLIENT {client_id} HANDLER")

    handler.start()

sock.close()
