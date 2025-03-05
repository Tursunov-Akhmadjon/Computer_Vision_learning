import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])  # Funksiyaga qo'yilgan rangni numoy arrayga convert qiladi 2_D da shuning uchun 2 ta [[]]
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)  # BGR(Blue green red ) ni HSV ga convert qiladi

    lowerLimit = (max(hsvC[0][0][0] - 10, 0), 100, 100)  # Hue raqamini ajratib olish uchun[0][0][0] dan foydalaniladi chunki u nested np arrayda saqlangan, va max bu eng pastki nuqat a va hue ni no'lga teng bop qolishini oldini oladi
    upperLimit = (min(hsvC[0][0][0] + 10, 179), 255, 255)  # HSV Hue range: 0-179 shuning uchun upper limit 179 dan oshib ketmasligini taminlaydi

    lowerLimit = np.array(lowerLimit, dtype=np.uint8) # Raqamlarni np arrayga convert qiladi
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
