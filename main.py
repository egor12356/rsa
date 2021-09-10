import rsa
from tkinter import *


def code():
    # message = inputEntry.get().encode()
    message = inputEntry.get(1.0, 'end-1c').encode()
    print(message)
    if message:
        global CRYPTO
        CRYPTO = rsa.encrypt(message, pubkey)
        textEntry.set(CRYPTO)


def decode():
    if textEntry.get():
        message = rsa.decrypt(CRYPTO, privkey)
        decodeEntry.delete(1.0, END)
        decodeEntry.insert(1.0, message)
# print(pubkey)
# print(privkey)
#
# message = b'Hello Blablacode.ru!'
#
# # шифруем
# crypto = rsa.encrypt(message, pubkey)
# print(crypto)
# # расшифровываем
# message = rsa.decrypt(crypto, privkey)
# print(message)

pubkey, privkey = rsa.newkeys(512)
privateKeyPkcs1PEM = privkey.save_pkcs1().decode('utf8')
print(privateKeyPkcs1PEM)

with open('privatekey.txt', 'w') as file:
    file.write(privateKeyPkcs1PEM)

# privateKeyReloaded = rsa.PrivateKey.load_pkcs1(privateKeyPkcs1PEM.encode('utf8'))


CRYPTO = ''
root = Tk()
root.title("RSA")
textEntry = StringVar()
strDecode = StringVar()


textInput = Label(root, text='Введите фразу для кодирования')
textInput.grid(column=1, row=1)


inputEntry = Text(root, width=50, height=5)
inputEntry.grid(column=2, row=1)

codeButton = Button(root, text='Закодировать', command=code)
codeButton.grid(column=2, row=2)

textInput = Label(root, text='Закодированная фраза')
textInput.grid(column=1, row=3)

outputEntry = Entry(root, width=50, state="readonly", textvariable=textEntry)
outputEntry.grid(column=2, row=3)

decodeButton = Button(root, text='Раскодировать', command=decode)
decodeButton.grid(column=2, row=4)

textDecode = Label(root, text='Раскодированная фраза')
textDecode.grid(column=1, row=5)

decodeEntry = Text(root, width=50, height=5)
decodeEntry.grid(column=2, row=5)

root.mainloop()