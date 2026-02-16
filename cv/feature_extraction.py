import cv2
img = cv2.imread('segmented.jpg', 0)
orb = cv2.ORB_create()
keypoints, descriptors = orb.detectAndCompute(img, None)  # Extract features
output = cv2.drawKeypoints(img, keypoints, None, color=(0,255,0))
cv2.imshow('Features', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Descriptors are arrays; save keypoints if needed
