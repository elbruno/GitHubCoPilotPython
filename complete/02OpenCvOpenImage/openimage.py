import cv2

# open image from file using opencv
img = cv2.imread('01.jpg')
# show image in new window
cv2.imshow('image', img)
# wait for any key stroke
cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()