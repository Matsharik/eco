import cv2
#import tracemalloc
from PIL import Image
import av
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, components_callbacks
from imageai.Detection.Custom import CustomObjectDetection

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'

if "_components_callbacks" not in st.session_state:
    st.session_state._components_callbacks = {}

nam = "dg"
per = "gg"
box = "bb"

st.markdown("# Распознавание мусора с конвейера")

st.write("Десятки объектов одновременно будут обводиться разными цветами и помечаться как пластик, бумага и стекло.")
st.write("Если в кадре будет только 1 объект, то его тип и местоположение относительно камеры будут озвучены.")

# st.image("Site IMG/Free-Cinema-4D-3D-Model-Xpresso-Rig-Conveyor-Belt-System.jpg")

st.write("Важно! Вам необходимо установить камеру над конвейером.")

st.write("Если все готово, нажмите START")


class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        print("init")
        self.detector = CustomObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath("pages/yolov3_hololens_mAP-0.11072_epoch-48.pt")
        self.detector.setJsonPath("pages/hololens_yolov3_detection_config.json")
        self.detector.loadModel()

    def transform(self, frame):
        img = frame.to_ndarray(format="rgb24")

        # Преобразование изображения с помощью ImageAI здесь
        detected_image, detections = self.detector.detectObjectsFromImage(input_image=img, output_type="array")

        print("Updated")
        for detection in detections:
            cv2.rectangle(detected_image, (detection["box_points"][0], detection["box_points"][1]),
                          (detection["box_points"][2], detection["box_points"][3]), (255, 0, 0), 2)
            #nam = detection["name"]
            #per = detection["percentage_probability"]
            #box = detection["box_points"]

        return detected_image

#st.write(nam, " : ", per, " : ", box)
webrtc_streamer(key="example", video_processor_factory=VideoTransformer, rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}, media_stream_constraints={"video": True, "audio": False})



# class DetectionVideoTransformer(VideoTransformerBase):

# def recv(self, frame):
# frm = frame.to_ndarray(format="bgr24")

# detections, detected_image = detector.detectObjectsFromImage(input_image=frm, output_type="array")

# for eachObject in detections:
# cv2.rectangle(detected_image, (eachObject["box_points"][0], eachObject["box_points"][1]),
# (eachObject["box_points"][2], eachObject["box_points"][3]), (0, 255, 0), 2)
# cv2.putText(detected_image, eachObject["name"],
# (eachObject["box_points"][0], eachObject["box_points"][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
# (0, 255, 0), 2)

# return detected_image


# webrtc_streamer(key="er", video_processor_factory=DetectionVideoTransformer,
# rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
# media_stream_constraints={"video": True, "audio": False})
