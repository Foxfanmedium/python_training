from network.socket.client import EchoClient

from network.jim.client import JSONRequest, JSONResponse

import network.settings


class EchoClient(EchoClient):
    def read(self, sock):
        data = self._sock.recv(settings.BUFFER_SIZE)  # получаем данные с сервера
        response = JSONResponse(data)  # Передаем полученные данные в конструктор JSONResponse
        print(response.body)  # Выводим тело запроса на экран

    def write(self):
        data = input('Enter data: ')  # Вводим данные с клавиатуры
        request = JSONRequest('echo', data)  # Создаем JSONRequest на основании введеных пользователем данных
        bytes_data = request.to_bytes()  # Переводим JSONRequest в bytes
        self._sock.send(bytes_data)  # Отправляем данные на сервер


if __name__ == '__main__':
    client = EchoClient()
    client.run()
