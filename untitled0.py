# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 16:56:14 2015

@author: alex
"""

import numpy
import cv2
import os
import math
import stat
import time
import getpass
import sys

img = cv2.imread('/home/alex/skindata/UL_Knuckle/5cc-4ee7-9421-11a37297ffe2-dbdfa6-1-tech-0-1-1-1-0.0-3.jpg', 0)
edges = cv2.Canny(img,150,200)
cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', 600, 450)
cv2.imshow('dst_rt', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
print "win"