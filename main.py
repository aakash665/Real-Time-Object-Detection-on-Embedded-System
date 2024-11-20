import cv2
from camera import Camera
from object_detector import ObjectDetector

def main():

    camera = Camera()
    detector = ObjectDetector(model_path='model.tflite', labels_path='labels.txt')

    while True:
        frame = camera.get_frame()
        
        if frame is None:
            break
        
        detections = detector.detect(frame)

        # Display results on frame
        for detection in detections:
            label, confidence, box = detection['label'], detection['confidence'], detection['box']
            cv2.rectangle(frame, box[0:2], box[2:4], (255, 0, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()