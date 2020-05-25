import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import login
from admin import sendTime, get_username


def programiAc():
    mixer.init()
    alarm = mixer.Sound('alarm.wav')

    yuz = cv2.CascadeClassifier('haarcascadefile\\haarcascade_frontalface_alt.xml')
    solG = cv2.CascadeClassifier('haarcascadefile\\haarcascade_lefteye_2splits.xml')
    sagG = cv2.CascadeClassifier('haarcascadefile\\haarcascade_righteye_2splits.xml')

    durum = ['Kapali', 'Acik']

    model = load_model('models/cnncat2.h5')
    yol = os.getcwd()
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    sayac = 0
    sure = 0
    uyariDortgeni = 2
    rpred = [99]
    lpred = [99]

    while True:
        ret, frame = cap.read()
        yukseklik, genislik = frame.shape[:2]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        yuzler = yuz.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
        solGoz = solG.detectMultiScale(gray)
        sagGoz = sagG.detectMultiScale(gray)

        cv2.rectangle(frame, (0, yukseklik - 50), (200, yukseklik), (0, 0, 0), thickness=cv2.FILLED)

        for (x, y, w, h) in yuzler:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)

        for (x, y, w, h) in sagGoz:
            saggoz = frame[y:y + h, x:x + w]
            sayac = sayac + 1
            saggoz = cv2.cvtColor(saggoz, cv2.COLOR_BGR2GRAY)
            saggoz = cv2.resize(saggoz, (24, 24))
            saggoz = saggoz / 255
            saggoz = saggoz.reshape(24, 24, -1)
            saggoz = np.expand_dims(saggoz, axis=0)
            rpred = model.predict_classes(saggoz)
            if rpred[0] == 1:
                durum = 'Acik'
            if rpred[0] == 0:
                durum = 'Kapali'
            break

        for (x, y, w, h) in solGoz:
            solgoz = frame[y:y + h, x:x + w]
            sayac = sayac + 1
            solgoz = cv2.cvtColor(solgoz, cv2.COLOR_BGR2GRAY)
            solgoz = cv2.resize(solgoz, (24, 24))
            solgoz = solgoz / 255
            solgoz = solgoz.reshape(24, 24, -1)
            solgoz = np.expand_dims(solgoz, axis=0)
            lpred = model.predict_classes(solgoz)
            if lpred[0] == 1:
                durum = 'Acik'
            if lpred[0] == 0:
                durum = 'Kapali'
            break
        cv2.putText(frame, "Aktif Kullanici:" + get_username(), (10, yukseklik - 450), font, 1, (255, 255, 255), 1,
                    cv2.LINE_8)
        if rpred[0] == 0 and lpred[0] == 0:
            sure = sure + 1
            cv2.putText(frame, "Lutfen gozlerinizi acin", (10, yukseklik - 20), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
        else:
            sure = sure - 1
            cv2.putText(frame, "Gozleriniz Acik", (10, yukseklik - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

        if sure < 0:
            sure = 0
            alarm.stop()
        cv2.putText(frame, "Sure:" + str(sure), (530, yukseklik - 20), font, 1, (255, 255, 255), 1, cv2.LINE_8)

        if sure < 15:
            alarm.stop()
        if sure > 15:

            cv2.imwrite(os.path.join(yol, 'image.jpg'), frame)
            try:
                alarm.play()
            except():
                pass
            if uyariDortgeni < 16:
                uyariDortgeni = uyariDortgeni + 2
                if uyariDortgeni < 2:
                    uyariDortgeni = 2
            cv2.rectangle(frame, (0, 0), (genislik, yukseklik), (0, 0, 255), uyariDortgeni)
        sendTime(sure)
        cv2.imshow('Surucu Takip Uygulamasi', frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
