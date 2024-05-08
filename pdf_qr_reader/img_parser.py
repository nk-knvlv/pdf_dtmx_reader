import cv2
import os
import fitz
import numpy as np
import pylibdmtx.pylibdmtx as dmtx

pdf_file = '100-.pdf'
pdf_document = fitz.open(pdf_file)
img_dir_name = 'images'


test_img_path = 'ds_data-matrix-oblozhka.jpg'

if not os.path.exists(img_dir_name):
    os.mkdir(img_dir_name)
else:
    print('already exist')


for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    image_list = page.get_images(full=True)
    for img_index, img_info in enumerate(image_list):
        xref = img_info[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image['image']

        image_np = np.frombuffer(image_bytes, dtype=np.uint8)

        image = cv2.imdecode(image_np, cv2.IMREAD_UNCHANGED)

        image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

        # # Находим белые пиксели (255, 255, 255) и устанавливаем прозрачность в 0
        # white_pixels = np.all(image_rgba[..., :3] == [255, 255, 255], axis=-1)
        # image_rgba[white_pixels] = [0, 0, 0, 0]

        # Определим цвет рамки (например, красный)
        border_color = (255, 255, 255, 1)  # BGR формат (красный)

        # Создадим новое изображение с дополнительной рамкой
        border_thickness = 6
        image_with_border = cv2.copyMakeBorder(image_rgba, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=border_color)

        # image[np.where(image == 255)] = 0

        if img_index == 0:
            image_filename = f'images/image_page_{page_num}_img{img_index}.png'
            cv2.imwrite(image_filename, image_with_border)

            print(f'Image saved{img_index}')

        # # Распознавание Data Matrix кодов
        # decoded_objects = dmtx.decode(image_rgba)
        # if decoded_objects:
        #     for obj in decoded_objects:
        #         data = obj.data.decode('utf-8')
        #         print("Extracted data: {}".format(data))
        # else:
        #     print("Data Matrix code not found on the image.")