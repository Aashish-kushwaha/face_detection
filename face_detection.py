import cv2

#create casscade classifier object
face=cv2.CascadeClassifier("D:\projects/face_detection/haarcascade_frontalface_default.xml")

#reading the image
img=cv2.imread("D:\projects/face_detection/face.jpeg",0)


faces=face.detectMultiScale(img,1.05,3)

for( x,y,w,h) in faces:
     img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,233,0),3)

rimg=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow('new',rimg)
cv2.waitKey()
