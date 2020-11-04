import pyzbar.pyzbar as pyzbar  # pip install pyzbar
import numpy as np  # pip install numpy
import cv2  # pip install opencv-python


# 바코드 탐지하는 엔진(바코드 및 QR코드 탐지)
def decode(im):
    # find barcodes and QRcodes
    decodedObejects = pyzbar.decode(im)

    # print results

    for obj in decodedObjects:
        print('Type :', obj.type)
        print('Data :', obj.data, '\n')

    return decodedObjects


# display barcode and QRcode location
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # if the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Number the convext hull
        n = len(hull)

        for j in range(0, n):
            cv2.line(im, hull[(j + 1) % n], (255, 0, 0), 3)

    # display results
    cv2.imshow("Results", im0);
    cv2.waitKey(0);


# 파일명 zbar.jpg의 이미지에서 바코드를 탐지하면 해당 코드를 리턴
# main
if __name__ == '__main__':
    im = cv2.imread('zbar.jpg')

    decodedObjects = decode(im)
    display(im, decodedObjects)
