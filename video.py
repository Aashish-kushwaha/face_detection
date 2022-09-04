import cv2,time
'''
steps to cature video
1->use cv2.VideoCapture() to get a vedio capture bject for the camera
2->setup the infinite loop and use the read() method to read the frames using the created object
3->use imshow() method to show the frames in the video
4->breaks the loops when user click the specific key

'''
'''
#for capturinf single frame as vedio is the collection of frame
vid=cv2.VideoCapture(0)
check,frame=vid.read()
print(check)
print(frame)
time.sleep(3)
cv2.imshow("capture",frame)
cv2.waitKey(0)
vid.release()
'''

video=cv2.VideoCapture(0)
a=1

while True:
    a=a+1
    check,img=video.read()
    print(img)
    face = cv2.CascadeClassifier("D:\projects/face_detection/haarcascade_frontalface_default.xml")

    #converting frame into gray sclae from color
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #checking if frames have face feature
    faces=face.detectMultiScale(gray,1.05,3)

    for(x,y,w,h) in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,233,0),3)

    cv2.imshow('capture',img)

    key=cv2.waitKey(1)
    if key==ord('q'): #on pressing q window will close
        break
print(a)
video.release()
cv2.destroyAllWindows

