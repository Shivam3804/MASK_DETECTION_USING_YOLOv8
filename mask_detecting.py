from ultralytics import YOLO
import cv2
model = YOLO("best.pt")  

cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    results = model.predict(source=frame, save=False, conf=0.5, show=False)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Face Mask Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
