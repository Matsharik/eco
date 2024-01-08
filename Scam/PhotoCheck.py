import cv2
import os
import numpy as np
import streamlit as st
from PIL import Image
#from pages import Найти_мусор_на_фото
from imageai.Detection.Custom import CustomObjectDetection
detector = CustomObjectDetection()


def analyz():
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("pages/yolov3_hololens_mAP-0.11072_epoch-48.pt")
    detector.setJsonPath("pages/hololens_yolov3_detection_config.json")
    detector.loadModel()
    detected_image, detections = detector.detectObjectsFromImage(input_image="Scam/filename.png", output_type="array")

    print("Updated")
    for detection in detections:
        cv2.rectangle(detected_image, (detection["box_points"][0], detection["box_points"][1]),
                      (detection["box_points"][2], detection["box_points"][3]), (255, 0, 0), 2)
        st.write(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

    #img = Image.fromarray(detected_image)
    img = Image.fromarray(detected_image.astype(np.uint8))
    st.image(img)

    return
