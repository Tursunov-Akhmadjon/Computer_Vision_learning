import cv2
from PIL import Image
from util import get_limits 

yellow = [0, 255, 255]  # Object rangini aniqlash
cap = cv2.VideoCapture(0) # Webcamerani aniqlash(real-time video uchun, 0; 1 ta kamera uchun) 

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()  # Kamera yaxshi o'rnatilmagan bo'lsa yoki muammo bo'lsa eror message  print bdi

while True:  # Webcame dan cheksiz framelarni oladi(infinite)
    success, frame = cap.read()  # Success=Boolean qiymat yoki istalgan yordamchi element frame muvofiqiyatli read qilsa True aks xolda False, Frame imageni numpy array ko'rinishida oladi
    if not success:
        print("Error: Failed to capture image.")
        break  # Agar imagini yaxshi read qila olmasa break qiladi loopni 
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #frameni BGR dan HSVga convert qiladi
    lowerLimit, upperLimit = get_limits(color=yellow)  # HSV ni chegaralaydi

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #Yellow colorni detect qilsa oq rang chiqadi aks xolda qora rang turadi, inRange bu Binary mask xosil qiluvchi funksiya
    mask_=Image.fromarray(mask)#Numpy maskni PIL imagega convert qiladi
    bbox=mask_.getbbox()# bbox- Boundary box va u sariq rangni atrofida 4burchak chizadi
    #print(bbox)
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame=cv2.rectangle(frame, (x1, y1), (x2 ,y2), (0, 255,0), 5)
    cv2.imshow('Webcam Feed', frame)  

    if cv2.waitKey(1) & 0xFF == ord('s'):  # ikki frame orasidagi vaqt: wait key(1) va 0XFF bu turli xil sistemalarda xam ishlashini taminlaydi va ord(s) s ni bosganda webcamden chiqadi
        break

cap.release()
cv2.destroyAllWindows()
