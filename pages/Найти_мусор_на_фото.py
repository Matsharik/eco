import streamlit as st
import Scam.PhotoCheck
import cv2
from PIL import Image
import os
import io

# import Scam.PhotoCheck as sp

st.markdown("# Распознавание мусора по фото")


def rgba_to_rgb(image_path):
    # Read the image
    img_rgba = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    img_rgb = cv2.cvtColor(img_rgba, cv2.COLOR_RGBA2RGB)

    return img_rgb


st.write("Данная функция нужна в личных и экспериментальных целях. На конвейере используйте другой режим.")

uploaded_img = st.file_uploader("Выберите фото, на котором есть мусор", ['png', 'jpeg'], accept_multiple_files=False)

image = None

if uploaded_img is not None:
    file_contents = uploaded_img.read()
    image = Image.open(io.BytesIO(file_contents))
    image_path = os.path.join('Scam', 'filename.png')
    image.save(image_path)
    st.write("Изображение успешно сохранено!")
    Scam.PhotoCheck.analyz()
else:
    st.write("Пожалуйста, загрузите файл.")


def showR():
    # st.image("Scam/imagenew1.png")
    return


