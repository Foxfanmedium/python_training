from network.socket.server import EchoServer

from network.jim.server import JSONRequest, JSONResponse

import network.settings


class EchoServer(EchoServer):
    def read(self, client):
        try:
            data = client.recv(settings.BUFFER_SIZE)  # Получаем данные от клиента
            if data:  # Если данные не являются пустой строкой
                request = JSONRequest(data)  # Передаем полученные данные в конструктор JSONRequest
                self._request.append(request)  # сохраняем запрос на сервере

        except ConnectionResetError:
            if client in self._connections:  # В случае разрыва соеднинения с клиентом и наличии
                self._connections.remove(client)  # Удаляем соответствующего клиента из списка подключений

    def write(self, client, request):
        try:
            response = JSONResponse(200, 'echo', request.body)  # Создаем JSONResponse на основании тела запроса

            bytes_message = response.to_bytes()  # Переводим JSONResponse в bytes
            client.send(bytes_message)  # Отправляем данные на клиент

        except (ConnectionResetError, BrokenPipeError):
            if client in self._connections:  # В случае разрыва соединения с клиентом и наличии данного клиента
                # в списке подключений
                self._connections.remove(client)  # Удаляем соответствующего клиента из списка подключений


if __name__ == '__main__':
    server = EchoServer()
    server.mainloop()
