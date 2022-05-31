import socket
import pickle
from tkinter import *

root = Tk()
chatout = StringVar()
root.title("Server side")
message_to_put = ''


def sendtext(event):
    x = ''
    # with open('chat.txt', 'w+') as writer:
    #     x+= 'Me: '+chatout.get()+'\n'
    #     writer.write(x)
    #     text_ent.delete(0, END)
    # with open('chat.txt', 'r') as reader:
    #     for x in reader:
    #         print(x)
    #         x+=reader.readline()
    #         print(x)

    text.insert(END, text_ent.get())
    text.insert(END, message_to_put)


text = Text(width=50, height=10)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.pack()
text_ent = Entry(textvariable=chatout)
text_ent.pack()
text_ent.bind('<Return>', sendtext)

# слушаем и отправляем данные
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(2)
c, addr = s.accept()
# M = 19
# recvd_data = c.recv(1024)
# key = pickle.loads(recvd_data)
# print('The recieved open key is: ', key)
# C = (M ** key[0]) % key[1]
# c.send(bytes([C]))
# print('Cryptogram is sent: ', C)

name = 'Server'
client = (c.recv(1024)).decode()
# print(client + ' has connected.')
c.send(name.encode())
print(client, 'has joined')
root.mainloop()
while True:
    message = 'Me : ' + text_ent.get()
    # clienttext = 'Me: ' + message
    c.send(message.encode())
    message = c.recv(1024)
    message = message.decode()
    print(client, ':', message)
    message_to_put = client + ':' + message
# f = open('Chat.txt', 'a')
# f.write(clienttext + '\n')
# f.write(message_to_put + '\n')
# f.close()