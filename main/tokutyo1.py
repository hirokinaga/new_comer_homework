import cv2

file_name1 = "C:\\Users\\hirok\\desktop\\sei.png"
file_name2 = "C:\\Users\\hirok\\desktop\\go.png"
orig1 = cv2.imread(file_name1)
orig2 = cv2.imread(file_name2)

img1_gray = cv2.cvtColor(orig1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(orig2, cv2.COLOR_BGR2GRAY)

# Calculate absolute difference between the two images
diff = cv2.absdiff(img1_gray, img2_gray)

# Apply threshold to identify significant differences
thresh = 30
diff[diff < thresh] = 0
diff[diff >= thresh] = 255

# Find contours of significant differences
contours, hierarchy = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around the differences
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(orig1, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imwrite('C:/Users/hirok/Documents/images/hikaku.png' , orig1)