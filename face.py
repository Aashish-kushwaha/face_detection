import cv2

#reading image:python store image as numpy array
#coloured image:colour image is 3-D matrix this can be proved using ndarray

#imread(): this method loads an image from the specified file, if file if missing or can't be read it returns the empty matrix
#syntax: cv2.imread(path,flag)
img=cv2.imread("D:/projects/face_detection/face.jpeg",1)  #1 here represnt that iamge is colourd
print(img)
print(img.shape)

#imshow():this method is used to display an image in a window,the window automatically fits to the image size
#to reisze the the image
#syntax:  cv2.imshow(window_name,image)
cv2.imshow('aashish',img)
#waitKey(): this method in python allow user to display window for given millisecnds or until any key is presse.
#syntax: cv2.waitkey(2000)
cv2.waitKey(1000)

#cv2.destroyAllWindow() #used to close the windows
#resize=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
#OR
resize=cv2.resize(img,(600,600))
cv2.imshow('new',resize)
cv2.waitKey(1000)

#gray scale :black and white is a 2-D matrix
img=cv2.imread("D:/projects/face_detection/face.jpeg",0)  #0 here represent that image is black and white
print(img)
print(img.shape)
cv2.imshow('aashish1',img)
cv2.waitKey(1000)

