import cv2
img = cv2.imread('preprocessed.jpg', 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # Binary segmentation
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(output, contours, -1, (0,255,0), 2)  # Draw segmented regions

cv2.imshow('Segmented', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('segmented.jpg', output)
