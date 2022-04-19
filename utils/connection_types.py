from . import logger

class Client:
    def __init__(self, conn, client_id ):
        self.conn = conn
        self.client_id = client_id

    def loop(self):
        while 'LISTENING':
            data = self.conn.recv(1024)

            # callback
            content = data.decode('utf-8')

            logger.info(content)
            self.conn.send('SUCCESS'.encode('utf-8'))            