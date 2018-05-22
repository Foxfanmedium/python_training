import socket
import time
import settings
import json


class EchoClient:

    def __init__(self):
        self._sock = socket.socket()
        self._sock.connect((settings.HOST, settings.PORT))

    def read(self, sock):
        bytes_data = self._sock.recv(settings.BUFFER_SIZE)
        str_data = bytes_data.decode(settings.ENCODING)
        print(str_data)

    def write(self):
        str_data = input('Enter data:')
        bytes_data = str_data.encode(settings.ENCODING)

    def run(self):

        try:
            while True:
                self.write()
                self.read(self._sock)

        except KeyboardInterrupt:
            pass


class JSONRequest:
    def __init__(self, action, body, **headers):
        self._headers = headers
        self._action = action
        self._body = body

    def add_header(self, key, value):
        self._headers.update({key: value})

    def remove_header(self, key):
        del self._headers[key]

    def to_bytes(self):
        envelope = dict()
        envelope.update({'action': self._action})
        envelope.update({'headers': self._headers})
        envelope.update({'body': self._body})
        data_str = json.dumps(envelope)

        return data_str.encode(settings.ENCODING)


class JSONResponse:

    def __init__(self, message_bytes):
        message_str = message_bytes.decode(settings.ENCODING)
        self._envelope = json.loads(message_str)

    @property
    def code(self):
        code = self._envelope.get('code')
        return code

    @property
    def action(self):
        action = self._envelope.get('action')
        return action

    @property
    def headers(self):
        headers = self._envelope.get('headers')

        for key, value in headers.items():
            yield key, value

    @property
    def body(self):
        body = self._envelope.get('body')
        return body





if __name__ == '__main__':
    client = EchoClient()
    client.run()
