import cv2
import numpy as np
# Assume detections: list of [x,y,w,h,score]
detections = np.array([[100,100,50,50,0.9], [105,105,50,50,0.8]])  # Example
indices = cv2.dnn.NMSBoxes(detections[:,:4].tolist(), detections[:,4].tolist(), 0.5, 0.4)
img = cv2.imread('segmented.jpg')
for i in indices:
    x,y,w,h = detections[i,:4].astype(int)
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
cv2.imshow('Post-processed Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Output: Save report or alert (e.g., print("Detected objects: {}".format(len(indices))))
