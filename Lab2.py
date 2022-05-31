from tkinter import *
from tkinter import filedialog as fd

root=Tk()
Alphalist = list("abcdefghiklmnopqrstuvwxyz ".upper())
lang=IntVar()

def doallshit():
    startMessage = entstartMessage.get().upper()
    numberkey = int(entkey.get())
    stringkey = list(entstrkey.get().upper())

    def remove(alpha, string):
        for symbol in string:
            if symbol not in [chr(x) for x in range(65, 91)] or string.count(symbol) > 1:
                string.remove(symbol)
            if symbol in alpha:
                alpha.remove(symbol)
        return alpha, string

    def insert(alpha_string):
        for index, symbol in enumerate(alpha_string[1]):
            alpha_string[0].insert((numberkey + index) % 26, symbol)
        return alpha_string[0]

    def encryptDecrypt(mode, message, key, final=""):
        alpha = insert(remove(Alphalist, stringkey))
        for symbol in message:
            if mode == 1:
                final += alpha[(alpha.index(symbol) + key) % 26]
            elif mode == 2:
                final += alpha[(alpha.index(symbol) - key) % 26]
        return final
    message = encryptDecrypt(lang.get(), startMessage, numberkey)
    with open('Lab2.txt', 'w') as file:
        file.write(message)

lblmes=Label(root, text='Введите предложение для зашифровки: ')
lblmes.grid(row=1, column=0, sticky=W)
entstartMessage=Entry(root)
entstartMessage.grid(row=1, column=1, sticky=W)
lblkey=Label(root, text='Введите ключ(число): ')
lblkey.grid(row=2, column=0, sticky=W)
entkey=Entry(root)
entkey.grid(row=2, column=1, sticky=W)
lblstrkey=Label(root, text='Введите ключевое слово: ')
lblstrkey.grid(row=3, column=0, sticky=W)
entstrkey=Entry(root)
entstrkey.grid(row=3, column=1, sticky=W)
radioEnc=Radiobutton(text="Encryption", value=1, variable=lang, padx=15, pady=10)
radioEnc.grid(row=4, column=0, sticky=W)
radioDec=Radiobutton(text="Decryption", value=2, variable=lang, padx=15, pady=10)
radioDec.grid(row=4, column=1, sticky=W)
filebutt=Button(text='Do all shit', command=doallshit)
filebutt.grid(row=5, columnspan=2, sticky=W)

root.mainloop()