import cv2
import copy

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=input('enter your id: ')
sampleNum=58

while(True):

    while True:

        # capture image
        ret, img = cam.read()
        orig_img = copy.deepcopy(img)

        # convert image to black&white
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        has_face = True if len(faces) > 0 else False

        # rectangle on the color image
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        # message to the color image
        cv2.putText(img, "Click Space to Capture" if has_face else "", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # show color image
        cv2.imshow('frame',img)

        k = cv2.waitKey(33)

        # in case of quit
        if k == ord('q'):
            break

        if k == 32 and has_face:
            break

    if k == ord('q'):
        break

    #incrementing sample number 
    sampleNum += 1
    #saving the captured face in the dataset folder
    cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

    for (x,y,w,h) in faces:
        cv2.rectangle(orig_img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(orig_img, "Captured: #" + str(sampleNum), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame',orig_img)

    k = cv2.waitKey(0)
    if k == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()