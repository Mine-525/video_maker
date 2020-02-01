# -*- coding: utf-8 -*-
"""
For converting pictures to video
Argument str:
    Directry name containing pictures
"""
import sys
import glob
import cv2
from natsort import natsorted
from argparse import ArgumentParser



def main():
    usage = 'Usage: python {}FILE [--phone] [--help]'\
            .format(__file__)
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('dname', type=str, help='echo dname')
    argparser.add_argument('-p', '--phone', action='store_true', help='pictures are taken by a phone or not?')

    args = argparser.parse_args()

    path = "./" + str(args.dname) + "/*"
    pic_list = glob.glob(path)
    pic_list = natsorted(pic_list)

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    if args.phone:
        fps = 10.0
    else:
        fps = 20.0

    video = cv2.VideoWriter(str(args.dname) + '.mp4', fourcc, fps, (480, 360))

    for i in pic_list:
        img = cv2.imread(i)
        video.write(img)

if __name__ == "__main__":
    main()