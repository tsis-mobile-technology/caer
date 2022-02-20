import cv2 as cv

img = cv.imread('beverages.jpg')

cv.imshow('beverages', img)
cv.waitKey(0)