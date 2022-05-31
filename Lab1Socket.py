import pickle
import socket
from tkinter import *
root=Tk()
chatout=StringVar()
root.title("Client side")
message_to_put=''
def sendtext(event):
    x=''
    # with open('chat.txt', 'w+') as writer:
    #     x+= 'Me: '+chatout.get()+'\n'
    #     writer.write(x)
    #     x+=text.get(END, END)
    #     text_ent.delete(0, END)
    # with open('chat.txt', 'r') as reader:
    #     for x in reader:
    #         x+=reader.readline()
    #         text.insert(END, x)

    text.insert(END, text_ent.get())
    text.insert(END, message_to_put)


text = Text(width=50, height=10)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.pack()
text.config(yscrollcommand=scroll.set)
text_ent=Entry(textvariable=chatout)
text_ent.pack(side=LEFT, fill=X)
text_ent.bind('<Return>', sendtext)

s_cli = socket.socket()
host = socket.gethostname()
port = 12345

# def eua(a, b):
#     r=[a, b]
#     q=[r[0]//r[1]]
#     i=1
#     s=[1, 0]
#     t=[0, 1]
#     while 1:
#         r.append(r[i-1]-q[i-1]*r[i])
#         s.append(s[i-1]-q[i-1]*s[i])
#         t.append(t[i-1]-q[i-1]*t[i])
#         if r[i+1]==0:
#             break
#         q.append(r[i]//r[i+1])
#         i=i+1
#     if t[-2]>=0:
#         return(t[-2])
#     else:
#         return(a+t[-2])
# p, q, e= 7, 17, 5
# N=p*q
# fiN=(p-1)*(q-1)
# d=eua(fiN, e)
# print('Open key: (', e, ',', N, ')')
# print('Private key: (', d, ',', N, ')')

#Подключение к серверу
s_cli.connect((host, port))
# data=pickle.dumps([e, N])
# s_cli.send(data)

# u=s_cli.recv(1024)
# C=int.from_bytes(u, byteorder='big')
# print('Cryptogram recieved: ', C)
# M=(C**d)%N
# print('Message is decrypted: ', M)

name='Client'
s_cli.send(name.encode())
ser_name=s_cli.recv(1024)
ser_name=ser_name.decode()

print(ser_name, 'has joined...')
root.mainloop()
while True:
    message = (s_cli.recv(1024)).decode()
    message_to_put = ser_name + ':' + message
    print(message_to_put)
    message = input('Me: ')
    s_cli.send(message.encode())