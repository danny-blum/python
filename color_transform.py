#!/usr/bin/python

from PIL import Image, ImageFilter, ImageOps 
import sys
#import cv2
#import numpy as np

if len(sys.argv) != 2:
    sys.exit(1) 

filename = sys.argv[1]

with Image.open(filename) as image: 
    width, height = image.size
 
    im_sharp = image.filter( ImageFilter.SHARPEN )

    im_inv = ImageOps.solarize(im_sharp, 50)  

    im_inv.show()


#    img = cv2.imread(filename, 0)
#    rows,cols = img.shape
#    
#    M = np.float32([[1,0,100],[0,1,50]])
#    dst = cv2.warpAffine(img,M,(cols,rows))
#    
#    cv2.imshow('img',dst)




