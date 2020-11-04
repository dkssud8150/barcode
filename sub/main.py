import pyzbar.pyzbar as pyzbar
import cv2
import matplotlib.pyplot as plt

#img = cv2.imread('img/bh_bar.jpg')
import tensorflow as tf
#file_path = tf.keras.utils.get_file('youtube.jpg', 'https://github.com/kairess/qrcode_barcode_detection/raw/master/img/bh_bar.jpg')
file_path = tf.keras.utils.get_file('bh_bar.jpg', 'https://github.com/kairess/qrcode_barcode_detection/raw/master/img/bh_bar.jpg')
img = cv2.imread(file_path)

plt.imshow(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap='gray')

decoded = pyzbar.decode(gray)

decoded #[Decoded(data=b'bbanghyong', type='CODE128', rect=Rect(left=19, top=10, width=140, height=17), polygon=[Point(x=19, y=11), Point(x=19, y=27), Point(x=159, y=26), Point(x=159, y=10)])]

for d in decoded:
    print(d.data.decode('utf-8'))
    print(d.type)

    cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0] + d.rect[2], d.rect[1] + d.rect[3]), (0, 0, 255), 2)

plt.imshow(img)