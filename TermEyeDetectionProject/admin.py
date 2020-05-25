import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from firebase_admin import *



firebase_admin.initialize_app(credentials, {'databaseURL': 'url'})

ref = db.reference(path')
ref2 = db.reference('')


def addData(ad, soyad, kullaniciAdi, sifre, mail):
    ref.set({

        kullaniciAdi: {
            'ad': ad,
            'soyad': soyad,
            'kullaniciAdi': kullaniciAdi,
            'sifre': sifre,
            'mail': mail,

        },

    })


def sendTime(timer):
    ref2.set(

        {

            "sayac": {
                'sure': timer,
            }
        },
    )

def get_username():
    results = db.reference('/path/', None).get()

    for id in results:
        username = results[id]['path']

    return username


def get_password():
    results = db.reference('/path/', None).get()

    for passwords in results:
        password = results[passwords]['path']

    return password


print("Username: " + get_username())
print("Password : " + get_password())
