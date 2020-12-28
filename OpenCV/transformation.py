import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x left
# -y up
# x right
# y down

translated = translate(img, 100, 100) #right and down for 100px
cv.imshow('Translated right down', translated)

translated = translate(img, -100, 100) #left and down for 100px
cv.imshow('Translated left down', translated)

#rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return  cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45) #dont do that, better directly add up the angles
cv.imshow('Double Rotated', rotated_rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, 0) #horizontal flip -> use 1 instead for vertical flip, -1 -> vertical & horizontal flip
cv.imshow('Flip', flip)

#cropping
cropped = img[200:400, 100:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)