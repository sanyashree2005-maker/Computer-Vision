import cv2
import numpy as np
img1 = cv2.imread('segmented.jpg', 0)
img2 = cv2.imread('acquired_image.jpg', 0)  # Assume a second image
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)  # Good matches
output = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None)
cv2.imshow('Matches', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
