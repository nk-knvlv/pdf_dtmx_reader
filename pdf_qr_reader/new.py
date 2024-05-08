from pyzbar.pyzbar import decode
from PIL import Image

# Загрузка изображения
image = Image.open('image_pagsssse_0_img0.jpg')

# Декодирование Data Matrix
data = decode(image)
print(data)

# Вывод результатов
for barcode in data:
    print(barcode.data.decode('utf-8'))