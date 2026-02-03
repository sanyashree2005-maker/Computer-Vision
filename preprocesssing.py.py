import cv2
img = cv2.imread('acquired_image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscale
blur = cv2.GaussianBlur(gray, (5,5), 0)       # Denoise
equalized = cv2.equalizeHist(blur)            # Contrast enhancement
cv2.imshow('Preprocessed', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('preprocessed.jpg', equalized)    # Save for next
