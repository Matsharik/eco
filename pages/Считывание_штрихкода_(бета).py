import streamlit as st
import Scam.CodCheck
import cv2
from PIL import Image
import os
import io

# import Scam.PhotoCheck as sp

st.markdown("# Распознавание штрих-кода и считывание цвета, материала")

st.text("Важно! Это бета-версия, которая не встроена в распознавание мусора с конвейера, т.к. этим методом можно выделить только координаты штрих-кода и цвет для стекла (по ГОСТ 32131-2013) (а не весь объект), что затрудняет работу сортировочным роботам.")
st.text("Кроме того, в Беларуси нет ГОСТ-стандартов, по которым в штрих-коде отводились бы специальные цифры для материала и цвета.")
st.text("Если они появятся, можно будет определять материал мусора точнее (при видимости штрих-кода).")

def rgba_to_rgb(image_path):
    # Read the image
    img_rgba = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    img_rgb = cv2.cvtColor(img_rgba, cv2.COLOR_RGBA2RGB)

    return img_rgb


uploaded_img = st.file_uploader("Выберите фото, на котором есть стекло со штрих-кодом", ['png', 'jpeg'], accept_multiple_files=False)

image = None

if uploaded_img is not None:
    file_contents = uploaded_img.read()
    image = Image.open(io.BytesIO(file_contents))
    image_path = os.path.join('Scam', 'filename.png')
    image.save(image_path)
    st.write("Изображение успешно сохранено!")
    Scam.CodCheck.analyz()
else:
    st.write("Пожалуйста, загрузите файл.")


def showR():
    # st.image("Scam/imagenew1.png")
    return