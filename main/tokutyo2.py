import cv2
from matplotlib import pyplot as plt

def hist(img, name):
# ヒストグラムの作成
    src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r_histogram = cv2.calcHist([src], [0], None, [256], [0, 256])
    g_histogram = cv2.calcHist([src], [1], None, [256], [0, 256])
    b_histogram = cv2.calcHist([src], [2], None, [256], [0, 256])

    # ヒストグラムの可視化
    plt.rcParams["figure.figsize"] = [12,3.8]
    plt.subplots_adjust(left=0.05, right=0.95, bottom=0.15, top=0.9)
    plt.subplot(121)
    plt.imshow(src)
    plt.axis("off")
    plt.subplot(122)
    plt.plot(r_histogram, color='red', label='red')
    plt.plot(g_histogram, color='green', label='green')
    plt.plot(b_histogram, color='blue', label='blue')
    plt.legend(loc=0)
    plt.xlabel('Brightness')
    plt.ylabel('Count')
    plt.savefig("C:/Users/hirok/Documents/images/" + name +".png")
    plt.close()


file_name1 = "C:\\Users\\hirok\\desktop\\Mandrill.png"
file_name2 = "C:\\Users\\hirok\\desktop\\Girl.png"
orig1 = cv2.imread(file_name1)
orig2 = cv2.imread(file_name2)
hist(orig1, "mand")
hist(orig2, "girl")

detector = cv2.AKAZE_create()
kp = detector.detect(orig1)
dst = cv2.drawKeypoints(orig1, kp, None)
cv2.imwrite('C:/Users/hirok/Documents/images/tokutyo.png' , dst)