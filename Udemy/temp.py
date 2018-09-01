# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img = cv2.imread("picture.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()