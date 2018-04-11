import socket
import network.socket.settings


class EchoClient:
    def __init__(self):
        self._sock = socket.socket()  # Создаем экземпляр сокет соединения
        self._sock.connect((settings.HOST, settings.PORT))  # Связываем сокет соединения с хостом и портом сервера

    def read(self, sock):
        bytes_data = self._sock.recv(settings.BUFFER_SIZE)  # Получаем данные с сервера
        str_data = bytes_data.decode(settings.ENCODING)  # Приводим полученные данные к стрококвому виду
        print(str_data)  # Выводим полученные данные на экран

    def write(self):
        str_data = input('Enter data: ')  # Вводим данные с клавиатуры
        bytes_data = str_data.encode(settings.ENCODING)  # Приводим отправляемые данные к байтовому виду
        self._sock.send(bytes_data)  # Отправляем данные на сервер

    def run(self):
        try:
            while True:
                self.write()
                self.read(self._sock)
        except KeyboardInterrupt:
            pass  # Обрабатываем сочетание клавиш Ctrl+C


if __name__ == '__main__':
    client = EchoClient()
    client.run()
