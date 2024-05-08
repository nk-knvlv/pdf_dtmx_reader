import cv2
from pylibdmtx import pylibdmtx

# Загрузка изображения с кодом DataMatrix
image = cv2.imread('image_pagsssse_0_img0.jpg')

# Декодирование кода DataMatrix
data = pylibdmtx.decode(image)

# Вывод декодированных данных
if data:
    print('Декодированные данные:', data[0].data.decode('utf-8'))
else:
    print('Не удалось декодировать код DataMatrix')