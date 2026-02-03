import cv2
# Option 1: Acquire from webcam (real-time)
cap = cv2.VideoCapture(0)  # 0 = default camera
ret, frame = cap.read()    # Capture a frame
if ret:
    cv2.imwrite('acquired_image.jpg', frame)  # Save for next steps
cap.release()
# Option 2: Load from file (simulated acquisition)
# frame = cv2.imread('input.jpg')  # Use this if no camera
cv2.imshow('Acquired Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
