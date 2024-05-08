import os
import fitz  # PyMuPDF
import cv2
import pylibdmtx.pylibdmtx as dmtx
from pyzbar.pyzbar import decode

import setuptools

img_dir_name = 'images'
pdf_path = '100-.pdf'
test_img_path = 'ds_data-matrix-oblozhka.jpg'

if not os.path.exists(img_dir_name):
    os.mkdir(img_dir_name)
else:
    print('already exist')

#save_str = 'C:\\Users\-\AppData\Local\Programs\Python\Python312\python.exe -m pip install'



def extract_data_matrix_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()

        image_rgb = cv2.cvtColor(pix.samples, cv2.COLOR_BGR2RGB)
        image = cv2.imread(image_rgb, cv2.IMREAD_GRAYSCALE)  # Чтение изображения в оттенках серого

        # Декодирование Data Matrix
        data = decode(image)
        print(data)

        # Вывод результатов
        for barcode in data:
            print(barcode.data.decode('utf-8'))


        # decoded_objects = dmtx.decode(image)
        #
        # for obj in decoded_objects:
        #     data = obj.data.decode('utf-8')
        #     print(f"Extracted data: {data}")

    doc.close()


# extract_data_matrix_from_pdf(pdf_path)
#
# image = cv2.imread(test_img_path, cv2.IMREAD_GRAYSCALE)  # Чтение изображения в оттенках серого
# decoded_objects = dmtx.decode(image)
#
# for obj in decoded_objects:
#     data = obj.data.decode('utf-8')
#     print(f"Extracted data: {data}")
