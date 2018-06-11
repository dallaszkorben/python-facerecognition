import cv2
from time import sleep

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=input('enter your id: ')
sampleNum=input('enter your number: ')
file_name=input("file name: ")

img = cv2.imread(file_name, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:

    #saving the captured face in the dataset folder
    cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

