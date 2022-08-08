# *****************************************************************************************
# Простой чат
# *****************************************************************************************
# server.py - сервер для чата
# *****************************************************************************************
# Напишем простой чат. Напишем два файла python server.py и client.py.
# Файл server.py не будет иметь пользовательского интерфейса. 
# Это простой сервер который будет принимать подключения от клиентов и сообщения. 
# От клиента будет приходить сообщения на сервер а сервер перешлет 
# это сообщения всем подлкюченным клиентам.
# Файл client.py будет иметь пользовательский интерфейс который мы напишем на Kivy. 
# Мы будем использовать модуль socket. В server.py мы напишем сокет к которому 
# привяжем ip и port чтобы клиенту могли по этому ip и port подключаться. 
# Так же напишем чтобы сокет постоянно прослушивал входящие сообщения 
# от клиентов и отправлял их всем клиентам
# В client.py мы напишем чтобы сокет подключался по протоколу TCP и подключался 
# по тому ip и port который у сервера. И так же напишем чтобы этот же сокет 
# принимал сообщения от сервера и выводил их в Label с сообщениями. 
# Так же будут приходить от сервера сообщения кто подключился к чату 
# и кто вышел из чата
# Сначало напишем файл sever.py. 
# Импоритруем два модуля socket и threading
# *****************************************************************************************
# socket - работа с TCP/IP и сетью в целом
import socket
# threading - работа с потоками
import threading
# *****************************************************************************************
# Далее напишем сокет. Создадим его по протоколу TCP, присвоим ip компа на котором 
# запустим сервер с помощью socket.gethostbyname(socket.gethostname()) и напишем порт. 
# Далее привяжем к сокету ip и порт. У сокета вызовем метод listen для того чтобы 
# прослушивать входящие подключения
# *****************************************************************************************
# создаем TCP сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# присваиваем IP адреса компьютера в переменную host
host = socket.gethostbyname(socket.gethostname())
# порт
port = 9090
# привязываем к сокету host и port
s.bind((host, port))
# прослушиваем соединение с клиента
s.listen()
# *****************************************************************************************
# Далее создадим пустой список клиентов и user_list(этот список мы будем передавать 
# клиентам и сбоку в клиенте будет отображаться список пользователей).Так же выведем 
# в консоли сообщение на каком ip и порту сервер запущен
# ******************************************************************************************
# список клиентов
clients = list()
# список имен который будет отображаться в клиенте
users_list = list()
# в терминале при запуске сервера выведиться текст
# о том что сервер запущен на host (IP адрессе) и порте
print(f'Сервер запущен на {host}:{port} ...')
# ******************************************************************************************
# запуск программы
if __name__ == '__main__':
    # выводим сокет
    print(f'socket.AF_INET = {socket.AF_INET}')
    print(f'type(socket.AF_INET) = {type(socket.AF_INET)}')
    print(f'socket.SOCK_STREAM = {socket.SOCK_STREAM}')
    print(f'type(socket.SOCK_STREAM) = {type(socket.SOCK_STREAM)}')
    print(f's = {s}')
    print(f'type(s) = {type(s)}')
    print(f'host = {host}')
    print(f'port = {port}')
# *****************************************************************************************