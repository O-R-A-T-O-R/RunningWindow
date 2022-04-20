import json
from . import logger

class Client:
    __proccessing__ = False
    __last__ = dict()

    def __init__(self, conn, client_id ):
        self.conn = conn
        self.client_id = client_id

    def loop(self):
        while 'LISTENING':
            try:
                data = self.conn.recv(1024)

                # callback
                content = json.loads(data.decode('utf-8').replace("'", '"'))

                self.__proccessing__ = False
                self.__last__ = content

            except Exception as e:
                logger.error(e)
                if e.args[0] == 10054:
                    return