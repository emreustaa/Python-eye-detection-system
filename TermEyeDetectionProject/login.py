from tkinter import *
import signup
from main import programiAc
import tkinter.messagebox as tk
from admin import get_username, get_password

gelen_kullanici_adi = get_username()
gelen_password = get_password()


def start_program():
    giris = Tk()

    giris.title("Giriş Ekranı")
    giris.geometry("300x250")
    giris.resizable(False, False)


    def kullaniciAdiOku():
        ad = kullaniciGiris.get()

        return ad

    def sifreOku():
        sifre = sifreGiris.get()

        return sifre

    def veriGonder(event):
        gelen_ad = kullaniciAdiOku()
        gelen_sifre = sifreOku()

        if gelen_ad == '' and gelen_sifre == '':
            tk.showerror('Hata', 'Kullanıcı adı ve Şifre boş olamaz')
        else:
            if gelen_ad == gelen_kullanici_adi and gelen_sifre == gelen_password:
                giris.destroy()
                programiAc()
            else:
                tk.showerror('Hata', 'Kullanıcı adı ve şifrenizi kontrol ediniz')

    def cikis():
        giris.destroy()
        sys.exit()

    def kayit():
        giris.destroy()
        signup.kaydol()

    uygulama = Frame(giris, relief="flat", borderwidth=4)
    uygulama.grid()

    kullanici_adi = Label(uygulama, text="Kullanıcı Adı Giriniz")
    kullanici_adi.grid(padx=90, pady=20)

    kullaniciGiris = Entry(uygulama)
    kullaniciGiris.grid(padx=90, pady=0)

    sifre = Label(uygulama, text="Şifre Giriniz")
    sifre.grid(padx=90, pady=5)

    sifreGiris = Entry(uygulama, show="*")

    sifreGiris.grid(padx=90, pady=0)

    sifreGiris.bind('<Return>', veriGonder)

    buton_kaydol = Button(giris, text='Kayıt ol', command=lambda: kayit())
    buton_kaydol.grid(padx=90, pady=5)

    buton_cikis = Button(giris, text='Çıkış', command=lambda: cikis())
    buton_cikis.grid(padx=90, pady=5)

    giris.mainloop()


start_program()
