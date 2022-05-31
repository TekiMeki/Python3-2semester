from re import findall
from tkinter import *

root=Tk()

matrixKey=[]
stringkeyno='MEAT'
stringkey=[]
for i in stringkeyno:
    stringkey.append(i)
alpha='abcdefghiklmnopqrstuvwxyz'.upper()
for i in alpha:
    matrixKey.append(i)
for j in stringkey:
    matrixKey.remove(j)
matrixKey.reverse()
stringkey.reverse()
for i in stringkey:
    matrixKey.append(i)
matrixKey.reverse()

addSymbol = '@'
def regular(text):
    template = r"[A-Z]{2}"
    return findall(template, text)
def encryptDecrypt(mode, message, final=""):
    if mode == 0:
        for symbol in message:
            if symbol not in [chr(x) for x in range(65, 92)]:
                message.remove(symbol)
        for index in range(len(message)):
            if message[index] == 'J': message[index] = 'I'
        for index in range(1, len(message)):
            if message[index] == message[index - 1]:
                message.insert(index, addSymbol)
        if len(message) % 2 != 0:
            message.append(addSymbol)
    binaryList = regular("".join(message))
    for binary in range(len(binaryList)):
        binaryList[binary] = list(binaryList[binary])
        for indexString in range(len(matrixKey)):
            for indexSymbol in range(len(matrixKey[indexString])):
                if binaryList[binary][0] == matrixKey[indexString][indexSymbol]:
                    y0, x0 = indexString, indexSymbol
                if binaryList[binary][1] == matrixKey[indexString][indexSymbol]:
                    y1, x1 = indexString, indexSymbol
        for indexString in range(len(matrixKey)):
            if matrixKey[y0][x0] in matrixKey[indexString] and matrixKey[y1][x1] in matrixKey[indexString]:
                if mode == 0:
                    x0 = x0 + 1 if x0 != 4 else 0
                    x1 = x1 + 1 if x1 != 4 else 0
                else:
                    x0 = x0 - 1 if x0 != 0 else 4
                    x1 = x1 - 1 if x1 != 0 else 4
        y0, y1 = y1, y0
        binaryList[binary][0] = matrixKey[y0][x0]
        binaryList[binary][1] = matrixKey[y1][x1]
    for binary in range(len(binaryList)):
        for symbol in binaryList[binary]:
            final += symbol
    return final

def doshit():
    res=encryptDecrypt(lang.get(), list(entry.get().upper()))
    if lang.get()==0:
        with open('lab3res.txt', 'w') as f:
            f.write(res)
    label['text']=res

lang = IntVar()

entry=Entry(root)
entry.pack()
radioe=Radiobutton(root, text='Encrypt', value=0, variable=lang)
radioe.pack()
radiod=Radiobutton(root, text='Decrypt', value=1, variable=lang)
radiod.pack()
but=Button(root, text='Do shit', command=doshit)
but.pack()
label=Label(root)
label.pack()

root.mainloop()