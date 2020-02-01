# -*- coding: utf-8 -*-
"""
For converting pictures to video
Argument str:
    Directry name containing pictures
"""
import sys
import glob
import re
import cv2
from natsort import natsorted


def main(_argv):
    path = "./" + str(_argv) + "/*"
    pic_list = glob.glob(path)
    pic_list = natsorted(pic_list)

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter(str(_argv) + '.mp4', fourcc, 20.0, (480, 360))

    for i in pic_list:
        img = cv2.imread(i)
        video.write(img)

if __name__ == "__main__":
    _argv = sys.argv[1]
    main(_argv)