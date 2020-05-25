import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from firebase_admin import *

credentials = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(credentials, {'databaseURL': 'https://goztakibi-e3cac.firebaseio.com//'})

ref = db.reference('/Kullanicilar')
ref2 = db.reference('/Sayac')


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
    results = db.reference('/Kullanicilar/', None).get()

    for id in results:
        username = results[id]['kullaniciAdi']

    return username


def get_password():
    results = db.reference('/Kullanicilar/', None).get()

    for passwords in results:
        password = results[passwords]['sifre']

    return password


print("Username: " + get_username())
print("Password : " + get_password())
