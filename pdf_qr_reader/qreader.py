import cv2
import pylibdmtx.pylibdmtx as dmtx

# Загрузка изображения
image_path = "image_pagsssse_0_img0.jpg"
image = cv2.imread(image_path)  # Чтение изображения в оттенках серого

# Распознавание Data Matrix кодов
decoded_objects = dmtx.decode(image)
print(len(decoded_objects))

if decoded_objects:
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print("Extracted data: {}".format(data))
else:
    print("Data Matrix code not found on the image.")