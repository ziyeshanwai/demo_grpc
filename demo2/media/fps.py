# -*- coding: UTF-8 -*-
# Author:liyouwang
# Date: 2018.8.2

import cv2
import time


if __name__ == "__main__":
    capture = cv2.VideoCapture("./IMG_0010.MOV")
    while True:
        t1 = time.time()
        ret, color_frame = capture.read()
        if ret:
            color_frame = cv2.resize(color_frame, dsize=(960, 540))
            t2 = time.time()
            print(1/(t2-t1))
