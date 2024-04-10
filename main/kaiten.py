import cv2
from matplotlib import pyplot as plt


file_name = "C:\\Users\\hirok\\desktop\\Mandrill.png"

orig = cv2.imread(file_name)
rot = cv2.rotate(orig, cv2.ROTATE_90_CLOCKWISE)
im_gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(im_gray, 0, 255, cv2.THRESH_OTSU)

cv2.imwrite('C:/Users/hirok/Documents/images/rot.png' , rot)
cv2.imwrite('C:/Users/hirok/Documents/images/bin.png' , img)