import cv2

#create casscade classifier object
face=cv2.CascadeClassifier("D:\projects/face_detection/haarcascade_frontalface_default.xml")

#reading the image
img=cv2.imread("D:\projects/face_detection/face.jpeg",1)
#converting image into grayscale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#search the co-ordinates of the image
faces=face.detectMultiScale(gray_img,1.05,3)

for( x,y,w,h) in faces:
     img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,233,0),3)
#resizing the image
rimg=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow('new',rimg)
cv2.waitKey()
