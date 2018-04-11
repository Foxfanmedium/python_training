import json
import jim.settings


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
        self._code = code
        self._action = action
        self._body = body

    def add_header(self, key, value):
        self._headers.update({key: value})

    def remove_headers(self, key):
        del self._headers[key]

    def to_bytes(self):
        envelope = dict()
        envelope.update({'code': self._code})
        envelope.update({'action': self._action})
        envelope.update({'headers': self._headers})
        envelope.update({'body': self._body})
        data_str = json.dumps(envelope)
        return data_str.encode(settings.ENCODING)
