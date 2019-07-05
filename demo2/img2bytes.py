import struct
import cv2
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('./texture_1017.jpg')
    cv2.namedWindow('OriginImage')
    cv2.imshow('OriginImage', img)
    img_2_bytes = np.resize(img, [img.size])
    img_bytes = struct.pack('H'*img.size, *img_2_bytes)
    img_ = struct.unpack('H'*img.size, img_bytes)
    image = np.reshape(img_, img.shape).astype(np.uint8)
    cv2.namedWindow('unpack_img')
    cv2.imshow('unpack_img', image)
    cv2.waitKey(0)