import cv2
from matplotlib import pyplot as plt


file_name = "C:\\Users\\hirok\\Desktop\\Mandrill.bmp"

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)


orig = cv2.imread(file_name)
#src = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
big = cv2.resize(orig, None, None, 2.0, 2.0)
im_tile_resize = concat_tile_resize([[big],
                                     [big, big],
                                     [big, big, big, big]])
cv2.imwrite('C:/Users/hirok/Documents/images/big.png' , im_tile_resize)