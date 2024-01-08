from imageai.Detection.Custom import CustomObjectDetection
import cv2
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolov3_hololens_mAP-0.19383_epoch-39.pt")# Замените на путь к вашей модели
detector.setJsonPath("hololens_yolov3_detection_config.json")# Замените на путь к вашему JSON-файлу конфигурации
detector.loadModel()

cap = cv2.VideoCapture(0)# Захват видео с камеры

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected_image, detections = detector.detectObjectsFromImage(input_image=frame, output_type="array")

    for eachObject in detections:
        cv2.rectangle(detected_image, (eachObject["box_points"][0], eachObject["box_points"][1]), (eachObject["box_points"][2], eachObject["box_points"][3]), (0, 255, 0), 2)
        cv2.putText(detected_image, eachObject["name"], (eachObject["box_points"][0], eachObject["box_points"][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('frame', detected_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
