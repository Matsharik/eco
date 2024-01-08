import cv2
from pyzbar.pyzbar import decode
import os
import numpy as np
import streamlit as st
from PIL import Image

def analyz():
    # Загрузка изображения
    img = Image.open('Scam/filename.png')
    np_array = np.asarray(img)
    # Декодирование штрих-кода
    barcodes = decode(np_array)

    for barcode in barcodes:
        # Извлечение информации о штрих-коде
        barcode_info = barcode.data.decode("utf-8")
        st.write("Обнаружен штрих-код: {barcode_info}")

        (x, y, w, h) = barcode.rect
        cv2.rectangle(np_array, (x, y), (x + w, y + h), (0, 255, 0), 2)

    img = image.fromarray(np_array.astype(np.uint8))
    st.image(img)
