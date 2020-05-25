import login
from tkinter import *
from admin import addData
import tkinter.messagebox as tk


def kaydol():
    kayit_ekrani = Tk()

    kayit_ekrani.title("Kayıt Ekranı")
    kayit_ekrani.geometry("300x400")
    kayit_ekrani.resizable(False, False)

    uygulama = Frame(kayit_ekrani, relief="flat", borderwidth=4)
    uygulama.grid()

    isim = Label(uygulama, text="Adınızı Giriniz")
    isim.grid(padx=90, pady=10)

    isim_al = Entry(uygulama)
    isim_al.grid(padx=90, pady=0)

    soyisim = Label(uygulama, text="Soyadınızı Giriniz")
    soyisim.grid(padx=90, pady=10)

    soyisim_al = Entry(uygulama)
    soyisim_al.grid(padx=90, pady=0)

    kullanici_adi = Label(uygulama, text="Kullanıcı Adınızı Giriniz")
    kullanici_adi.grid(padx=90, pady=10)

    kullanici_adi_al = Entry(uygulama)
    kullanici_adi_al.grid(padx=90, pady=0)

    sifre = Label(uygulama, text="Şifre Giriniz")
    sifre.grid(padx=90, pady=10)

    sifre_al = Entry(uygulama)
    sifre_al.grid(padx=90, pady=0)

    mail = Label(uygulama, text="Mail Giriniz")
    mail.grid(padx=90, pady=10)

    mail_al = Entry(uygulama)
    mail_al.grid(padx=90, pady=0)

    def isim_oku():
        read_name = isim_al.get()
        return read_name

    def soyisim_oku():
        read_surname = soyisim_al.get()

        return read_surname

    def kullanici_adi_oku():
        read_username = kullanici_adi_al.get()
        return read_username

    def sifre_oku():
        read_password = sifre_al.get()

        return read_password

    def mail_oku():
        read_mail = mail_al.get()

        return read_mail

    def bilgiGonder():
        isim_gonder = isim_oku()
        soyisim_gonder = soyisim_oku()
        kullanici_adi_gonder = kullanici_adi_oku()
        sifre_gonder = sifre_oku()
        mail_gonder = mail_oku()

        if isim_gonder == '' or soyisim_gonder == '' or kullanici_adi_gonder == '' or sifre_gonder == '' or mail_gonder == '':
            tk.showerror('Hata', 'Bilgiler boş bırakılamaz')
        else:
            addData(isim_gonder, soyisim_gonder, kullanici_adi_gonder, sifre_gonder, mail_gonder)
            kayit_ekrani.destroy()
            login.start_program()

    save = Button(uygulama)
    save.config(text="Kaydet")
    save.config(command=lambda: bilgiGonder())
    save.grid(padx=110, pady=10)

    kayit_ekrani.mainloop()
