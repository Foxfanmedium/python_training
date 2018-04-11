import socket
import select
import collections
import socket.settings


class EchoServer:
    def __init__(self):
        self._connections = list()  # Создаем список для хранения клиентских соединений
        self._requests = collections.deque()  # Создаем список для хранения клиентских запросов
        self._sock = socket.socket()  # Создаем экземпляр сокет соединения
        self._sock.bind((settings.HOST, settings.PORT))  # Связываем сокет соединение с хостом и портом сервера
        self._sock.listen(settings.CLIENTS_NUM)  # Ждем обращений клиентов
        self._sock.settimeout(settings.TIMEOUT)  # Определяем время ождания запроса клиента

    def connect(self):
        try:
            client, address = self._sock.accept()  # Получаем подключение клиента
            self._connections.append(client)  # Сохраняем подключение клиента

        except OSError:
            pass  #

    def read(self, client):
        try:
            data = client.recv(settings.BUFFER_SIZE)  # Получаем данные от клиента
            if data:  #
                str_data = data.decode(settings.ENCODING)  # Приводим полученные данные к строковому виду
                self._requests.append(str_data)  # Сохраняем запрос на сервере

        except ConnectionResetError:
            if client in self._connections:  # В случае разрыва соединения с клиентом и наличии
                self._connections.remove(client)  # Удаляем соответствующего клиента из списка получателей

    def write(self, client, request):
        try:
            bytes_message = request.encode(settings.ENCODING)  # Приводим отпарвленные данные к байтовому виду
            client.send(bytes_message)  # Отправляем данные на клиент
        except (ConnectionResetError, BrokenPipeError):
            if client in self._connections:  # В случае разрыва соединения с клиентом и наличии
                self._connections.remove(client)  # Удаляем соответствующего клиента из списка подключений

    def mainloop(self):
        try:
            while True:
                self.connect()  # Обрабатываем подключения к серверу
                for client in self._connections:
                    self.read(client)  # Сохраняем запрос клиента к серверу

                    if self._requests:
                        request = self._requests.popleft()  # Извлекаем первый запрос
                        self.write(client, request)  # Отправляем запрос клиенту

        except KeyboardInterrupt:
            pass  # Обрабатываем сочетание клавиш Ctrl+C


if __name__ == '__main__':
    server = EchoServer()
    server.mainloop()
