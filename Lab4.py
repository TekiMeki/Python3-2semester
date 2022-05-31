from random import randint
import pickle
from tkinter import *
import hashlib

root=Tk()


def main():
    int_var = IntVar()
    alphabet = 'abcdefghijklmnopqrstuvwxyz{|}~\x7f'
    bytealpha = {alphabet[i]: bin(ord(alphabet[i]))[4:] for i in range(len(alphabet))}

    def log_xor(str1, str2):
        res=''
        for i in range(len(str1)):
            res+=str(int(str1[i])^int(str2[i]))
        return res

    def en_de_crypt(m, num_page):
        res_en_bit_mes=[]
        res_de_bit_mes=[]
        res_mes=''
        bit_m=m.split('|')
        s = []
        for i in bytealpha.keys():  # второй
            s.append((bytealpha[i], i))  # словарь
        b = dict(s)
        if int_var.get()==1:
            put_in_dat(len(mes_ent.get()), int(num_page_ent.get()))
            bit_page = put_out_dat()
            for i in range(len(bit_m)):
                if bit_m[i]!='':
                    res_en_bit_mes.append(str(log_xor(bit_m[i], bit_page.get(num_page)[i+1])))
            print('Битово зашифрованое сообщение: ', res_en_bit_mes) #Шифртекст
            for stroka in res_en_bit_mes:
                res_mes+=b.get(stroka)
            print('Зашифрованное сообщение-шифртекст: ', res_mes)
            print(res_mes)
            with open('lab4.txt', 'w') as file:
                file.write(res_mes)
            return res_mes
        else:
            bit_page = put_out_dat()
            for i in range(len(bit_m)):
                if bit_m[i]!='':
                    res_de_bit_mes.append(str(log_xor(bit_m[i], bit_page.get(num_page)[i+1])))
            print('Битово дешифрованое сообщение: ', res_de_bit_mes)
            for stroka in res_de_bit_mes:
                res_mes+=b.get(stroka)
            print('Дешифрованное сообщение: ', res_mes)
            with open('lab4.txt', 'a') as file:
                file.write('\n'+res_mes)
            return res_mes

    def put_in_dat(lenmes, n_p):
        infile = open('test.dat', 'wb')  # Открываем файл в режиме wb
        dic_page={}
        list = []
        bitapen = ''
        for pagelist in range(1, n_p+1):
            for i_list in range(lenmes+1):
                for j_bit in range(5):
                    bitapen+=str(randint(0, 1))
                list.append(bitapen)
                bitapen=''
            dic_page[pagelist]=list
            list=[]
        pickle.dump(dic_page, infile)  # Сериализовать объекты и записать в файлы
        infile.close()

    def put_out_dat():
        outfile = open('test.dat', 'rb')  # Открываем файл в режиме rb
        dic_page = pickle.load(outfile)
        outfile.close()
        print(dic_page)
        return dic_page

    def start_en_de():
        bit_mes = ''
        print('Исходное сообщение: ', mes_ent.get())
        for i in range(len(mes_ent.get())):
            bit_mes += bytealpha.get(mes_ent.get()[i]) + '|'
        print('Двоичное представление сообщения: ', bit_mes)
        out_text = en_de_crypt(bit_mes, int(num_page_ent.get()))
        print('Зашифрованое сообщение: ', out_text)
        result_label['text']=out_text

    mes_ent = Entry(root)
    mes_ent.grid(row=0, column=1, sticky=W)
    mes_lab = Label(root, text='Введите текст для шифрации: ')
    mes_lab.grid(row=0, column=0, sticky=W)

    num_page_ent = Entry(root)
    num_page_ent.grid(row=1, column=1, sticky=W)
    num_page_lab = Label(root, text='Введите номер страницы одноразового блокнота: ')
    num_page_lab.grid(row=1, column=0, sticky=W)

    label = Label(root, text='Выберите режим Encrypt/Decrypt')
    label.grid(row=2)

    radben = Radiobutton(root, text='Encrypt', value=1, variable=int_var)
    radben.grid(row=3, column=0, sticky=W)
    radbde = Radiobutton(root, text='Decrypt', value=2, variable=int_var)
    radbde.grid(row=3, column=1, sticky=W)

    start_bt=Button(root, text='Начать', command=start_en_de)
    start_bt.grid(row=4)

    result_label=Label(root)
    result_label.grid(row=5)

    root.mainloop()


if __name__=='__main__':
    main()