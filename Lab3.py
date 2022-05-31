import hashlib
from random import randint
from tkinter import *
from tkinter import filedialog as fileask

root=Tk()
S=b''
f=[]
int_var = IntVar()

def eua(a, b):
    r=[a, b]
    q=[r[0]//r[1]]
    i=1
    s=[1, 0]
    t=[0, 1]
    while 1:
        r.append(r[i-1]-q[i-1]*r[i])
        s.append(s[i-1]-q[i-1]*s[i])
        t.append(t[i-1]-q[i-1]*t[i])
        if r[i+1]==0:
            break
        q.append(r[i]//r[i+1])
        i=i+1
    if t[-2]>=0:
        return t[-2]
    else:
        return a+t[-2]
def euagcd(a, b):
    r=[a, b]
    q=[r[0]//r[1]]
    i=1
    while 1:
        r.append(r[i-1]-q[i-1]*r[i])
        if r[i+1]==0:
            break
        q.append(r[i]//r[i+1])
        i=i+1
    return r[-2]

def signFile():
    global f
    # # Генерация цифровой подписи на основе алгоритма Ель-Гамаля
    if int_var.get() == 1:
        h = hashlib.sha256(S)
    else:
        h = hashlib.sha512(S)
    h1 = int(h.hexdigest(), 16)
    print(h1)
    p, g = 144, 89
    # Секретный ключ
    x = randint(2, p-2)
    y = pow(g, x, p)
    print('Открытый ключ: ', y)
    w = True
    while w:
        k = randint(2, p - 2)
        if euagcd((p - 1), k) == 1:
            w = False
        else:
            w = True
    with open('Lab3.txt', 'a') as file:
        r = pow(g, k, p)
        u = (h1 - x * r) % (p - 1)
        s = (eua((p - 1), k) * u) % (p - 1)
        settofile='\n'+str(r)+'\n'+str(s)
        file.write(settofile)
    f=[p, g, r, s, x]

def checksignFile():
    global f
    with open('Lab3.txt', 'r') as file:
        S, r, s=file.read().encode().splitlines()
    if int_var.get()==1:
        h = hashlib.sha256(S)
    else:
        h = hashlib.sha512(S)
    h1 = int(h.hexdigest(), 16)
    print(h1)
    p, g, r, s, x=f[0], f[1], f[2], f[3], f[4]
    y = pow(g, x, p)
    valA = (pow(y, r, p) * pow(r, s, p)) % p
    valB = pow(g, h1, p)
    print("Значение отправителя= ", valA)
    print("Значение получателя= ", valB)
    if valA == valB:
        print('Signature is valid')
    else:
        print('Signature is invalid')

def openFile():
    file=fileask.askopenfilename()
    fileS = open(file, 'br')
    S=fileS.read().splitlines()[0]
    print(S)

button=Button(root, text='Open file', command=openFile)
button.pack()
rb1=Radiobutton(root, text='Sha256', value=1, variable=int_var)
rb1.pack()
rb2=Radiobutton(root, text='Sha512', value=2, variable=int_var)
rb2.pack()
butsign=Button(root, text='Sign file', command=signFile)
butsign.pack()
butchecksign=Button(root, text='Check sign', command=checksignFile)
butchecksign.pack()

root.mainloop()