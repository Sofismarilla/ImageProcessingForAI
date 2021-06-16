# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:48:38 2020

@author: Admin
"""

import cv2
import numpy as np

filePath = "images/figures2/Baboon.jpg"
imgColor = cv2.imread(filePath)

mask = np.ones((5,5),np.float32)/25
#mask = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/16
imgSmoothing = cv2.filter2D(imgColor,-1,mask)

imgBlur = cv2.blur(imgColor,(5,5))

cv2.imshow("imgColor",imgColor)
cv2.imshow("imgSmoothing",imgSmoothing)
cv2.imshow("imgBlur",imgBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()