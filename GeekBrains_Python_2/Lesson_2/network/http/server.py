import json
import settings


class JSONRequest:
    def __init__(self, message_bytes):
        message_str = message_bytes.decode(settings.ENCODING)
        self._envelope = json.loads(message_str)
        self._startline = self._envelope.get('startline')

    @property
    def uri(self):
        uri = self._startline.get('uri')
        return uri

    @property
    def method(self):
        method = self._startline.get('method')
        return method

    @property
    def body(self):
        body = self._envelope.get('body')
        return body


class JSONResponse():
    def __init__(self, code, method, body, **headers):
        self._headers = headers
        self._code = code
        self._method = method
        self._body = body


    def add_header(self, key, value):
        self._headers.update({key:value})

    def remove_header(self, key):
        del self._headers[key]

    def to_bytes(self):
        envelope = dict()
        start_line = dict()
        start_line.update({'code': self._code})
        start_line.update({'version': settings.VERSION})
        envelope.update({'startline': start_line})
        envelope.update({'headers': self._headers})
        envelope.update({'body':self._body})
        data_str = json.dumps(envelope)
        return data_str.encode(settings.ENCODING)




































