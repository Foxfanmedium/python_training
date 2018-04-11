import socket

import settings

import select

import collections

import json


class EchoServer:

    def __init__(self, **args):
        self._connections = list()
        self._requests = collections.deque()
        self._sock = socket.socket()
        self._sock.bind((settings.HOST, settings.PORT))
        self._sock.listen(settings.N_CLIENTS)

    def connect(self):

        try:
            client, address = self._sock.accept()
            self._connections.append(client)

        except OSError:
            pass

    def read(self, client):

        try:
            data = client.recv(settings.BUFFER_SIZE)
            if data:
                str_data = data.decode(settings.ENCODING)
                self._requests.append(str_data)

        except ConnectionResetError:
            if client in self._connections:
                self._connections.remove(client)

    def write(self, client, request):

        try:
            bytes_message = request.encode(settings.ENCODING)
            client.send(bytes_message)

        except(ConnectionResetError, BrokenPipeError):
            if client in self._connections:
                self._connections.remove(client)

    def mainloop(self):

        try:

            while True:
                print('i am waiting for you-u-u! Your server...')
                self.connect()
                for client in self._connections:

                    self.read(client)

                    if self._requests:
                        request = self._requests.popleft()
                        self.write(client, request)

        except KeyboardInterrupt:
            pass


class JSONRequest:

    def __init__(self, message_bytes):
        message_str = message_bytes.decode(settings.ENCODING)

        self._envelope = json.loads(message_str)

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


class JSONResponse:
    def __init__(self, code, action, body, **headers):
        self._headers = headers
        self._action = action
        self._code = code
        self._body = body

    def add_header(self, key, value):
        self._headers.update({key: value})

    def remove_header(self, key):
        del self._headers[key]

    def to_bytes(self):
        envelope = dict()
        envelope.update({'code': self._code})
        envelope.update({'action': self._action})
        envelope.update({'headers': self._headers})
        envelope.update({'body': self._body})

        data_str = json.dumps(envelope)

        return data_str.encode(settings.ENCODING)


if __name__ == '__main__':
    server = EchoServer()

    server.mainloop()
