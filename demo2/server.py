# -*- coding: UTF-8 -*-
# Author:liyouwang
# Date: 2018.8.2
import grpc
from concurrent import futures
import time
import get_img_pb2
import get_img_pb2_grpc
import cv2
import struct
import numpy as np


class get_imageServicer(get_img_pb2_grpc.get_imageServicer):
    def getimg(self, request, context):
        print(request.reu)
        return response


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    get_img_pb2_grpc.add_get_imageServicer_to_server(get_imageServicer(), server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    capture = cv2.VideoCapture("./media/IMG_0010.MOV")
    response = get_img_pb2.img_()
    count = 0
    try:
        while True:
            start_time = time.time()
            count += 1
            ret, color_frame = capture.read()
            if ret:
                color_frame = cv2.resize(color_frame, dsize=(960, 540))
                gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
                response.width = gray_frame.shape[1]
                response.height = gray_frame.shape[0]
                response.frame = count
                img_2_bytes = np.resize(gray_frame, [gray_frame.size])
                img_bytes = struct.pack('H' * gray_frame.size, *img_2_bytes)
                response.img = img_bytes
                end_time = time.time()
                print("fps: {}".format(1/(end_time - start_time)))
            # time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)