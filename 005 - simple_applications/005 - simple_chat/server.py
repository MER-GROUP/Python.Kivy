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
# Далее напишем метод где сервер будет отправлять всем подключенным клиентам данные 
# полученные от одного клиента
# ******************************************************************************************
# отправка данных всем клиентам и списка clients
def send_message(data):
    for cl in clients:
        cl.send(data)
# ******************************************************************************************
# Далее напишем метод message_handler который в качестве параметра будет принимать 
# клиента. Этот метод нужен для приема сообщений от клиента и будет вызываться в 
# отдельном потоке.Почему в отдельном потоке? Дело в том что если мы запустим сервер 
# с одним потоком то он будет ждать входящие подключения и когда клиент будет отсылать 
# сообщения он не будет на это реагировать так как у него лишь один поток где он принимает 
# входящие подключения от клиентов, поэтому мы создаем отельный поток где сервер будет 
# принимать сообщения и отсылать их клиентам
# Пишем метод message_handler
# ******************************************************************************************
def message_handler(client):
    while True:
        # сервер ждет когда придет поток байт (сообщение)
        # от клиентского сокета
        data = client.recv(1024)
        # преобразование из массива бай в строку
        data = data.decode('utf-8')
        # разделяем пришедшие данные
        d =data.split('-')
        # приверяем  если пришло слово exit то удаляем его со списка склиентов
        # то есть клиент выходит из чата и отключается от сервера
        if (d[0] == 'exit'):
            clients.remove(client)
            print(data)
            print(d[1])
            # также удаляем со списка пользователей
            users_list.remove(d[1])
            # проверяем если пользователей больше нуля то отправляем соосбщение
            # пользователям о том что такой то пользователь 
            # вышел из чата и заново отправляем список пользователей
            if (0 < len(clients)):
                user_left = f'Пользователь {d[1]} вышел из чата'
                user_left = user_left.encode('utf-8')
                send_message(user_left)
                users = '[' + ','.join(user_left) + ']'
                print(users)
                users = users.encode('utf-8')
                send_message(users)
            print('Количество пользователей: ' + str(len(clients)))
            break
        else:
            # печатаем сообщение в консоли, кодируем
            # в массив байт и отправляем всем клиентам
            print(data)
            data = data.encode('utf-8')
            send_message(data)
# ******************************************************************************************
# Далее напишем метод accept_connection который будет принимать входящие подключения
# ******************************************************************************************
# метод который принимает подключения от клиентов
def accept_connection():
    # бесконечный цикл что бы сервер мог всегда 
    # ждать подключения клиентов
    while True:
        # выводим количество пользователей
        print('Количество пользователей: ' + str(len(clients)))
        # функция s.accept возвращает кортеж где первый 
        # параметр клиенсткий сокет (client) и адрес
        # подключенного сокета (IP и порта) 
        client, addr = s.accept()
        # получаем имя клиентского сокета.
        # Сокет принимает данные в виде массива байт
        # с помощью метода recv(количество байт)
        nick = client.recv(1024)
        # переводим массив байт в текст формата 'utf-8'
        nick = nick.decode('utf-8')
        # добавляем имя в список users_list
        users_list.append(nick)
        # присваиваем переменной mess сообщение о том 
        # что пользователь с именем зашел в чат
        mess = f'Пользователь {nick} заходит в чат'
        # переводим в массив байт для отправки клиентским сокетам сообщение
        mess = mess.encode('utf-8')
        # выводим в консоли адрес клиентсткого сокета
        print(addr)
        # если клиентского сервера нет в списке то добавляем
        if client not in clients:
            clients.append(client)
        # создаем отдельный поток для метода message_handler и
        # в качестве параметра передаем client
        threading.Thread(target=message_handler, args=((client,))).start()
        # передаем всем сообщение о том кто зашел в чат
        send_message(mess)
        # в users мы из списка users_list в квадратных скобках
        # через запятую пишем всех пользователей
        users = '[' + ','.join(users_list) + ']'
        # выводи в консоль users
        print(users)
        # переводим в миссив байт для отправки клиентским сокетам
        # список пользователей которые будут отображаться
        users = users.encode('utf-8')
        # отправляем список пользователей клиентам
        send_message(users)
# ******************************************************************************************
# Далее пишем что при запуске файла будет вызываться метод accept_connection
# ******************************************************************************************
# запуск программы
if __name__ == '__main__':
    # ---------------------------------------------------------------------------
    accept_connection()
    # ---------------------------------------------------------------------------
    # # выводим сокет
    # print(f'socket.AF_INET = {socket.AF_INET}')
    # print(f'type(socket.AF_INET) = {type(socket.AF_INET)}')
    # print(f'socket.SOCK_STREAM = {socket.SOCK_STREAM}')
    # print(f'type(socket.SOCK_STREAM) = {type(socket.SOCK_STREAM)}')
    # print(f's = {s}')
    # print(f'type(s) = {type(s)}')
    # print(f'host = {host}')
    # print(f'port = {port}')
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# С файлом server.py всё.
# *****************************************************************************************