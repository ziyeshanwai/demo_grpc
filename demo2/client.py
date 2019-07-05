# -*- coding: UTF-8 -*-
# Author:liyouwang
# Date: 2018.8.2
import grpc
import get_img_pb2
import get_img_pb2_grpc
import cv2
import struct
import numpy as np
import time


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:50051')

    # create a stub (client)
    stub = get_img_pb2_grpc.get_imageStub(channel)

    # create a valid request message
    while True:
        t1 = time.time()
        req_mess = get_img_pb2.requst(reu='tests')
        response = stub.getimg(req_mess)
        img = response.img
        width = response.width
        height = response.height
        img_ = struct.unpack('H' * width * height, img)
        image = np.reshape(img_, [height, width]).astype(np.uint8)

        print(response.frame)
        cv2.namedWindow('video')
        cv2.imshow('video', image)
        cv2.waitKey(1)
        t2 = time.time()
        print(1 / (t2 - t1))

