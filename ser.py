import socket
p=23
g=5
# слушаем и отправляем данные
s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('adr：', addr)
    x=9
    X=(g**x)%p
    print('Secret number is ', str(x), '. X is calculated: ', str(X))
    c.send(bytes([X]))
    print('X is sent.')
    u=c.recv(1024)
    Y=int.from_bytes(u, byteorder='big')
    print('Y is recieved ', str(Y))
    k=(Y**x)%p
    print('Key is: ', str(k))
    name_f = (c.recv(1024)).decode('UTF-8')

    # открываем файл в режиме байтовой записи в отдельной папке 'sent'
    f = open('sent-Aes.enc', 'wb')

    while True:
        # получаем байтовые строки
        l = c.recv(1024)
        # пишем байтовые строки в файл на сервере
        f.write(l)
        if not l:
            break

    f.close()
    c.close()