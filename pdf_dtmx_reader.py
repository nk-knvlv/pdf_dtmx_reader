import pymupdf
import pylibdmtx.pylibdmtx as dmtx
import numpy as np


class PdfDataMatrixReader:
    def __init__(self, pdf_path, output_path):
        self.pdf_path = pdf_path
        self.output_path = output_path + '/'

    @staticmethod
    def get_text_value_from_img(img):
        decoded_objects = dmtx.decode(img)
        if decoded_objects:
            result = decoded_objects[0].data.decode('utf-8')
            return result

    def get_codes(self):
        doc = pymupdf.open(self.pdf_path)  # open document
        codes_list = []
        for page in doc:  # iterate through the pages
            pixmap = page.get_pixmap(dpi=300)  # render page to an image

            width = pixmap.w
            height = pixmap.h
            buf = pixmap.samples

            img = np.frombuffer(buf, dtype='uint8').reshape((height, width, 3))
            codes_list.append(self.get_text_value_from_img(img))
        return codes_list


pdf_path = '100-.pdf'
output_path = 'codes'

pdf_reader = PdfDataMatrixReader(pdf_path, output_path)
codes = pdf_reader.get_codes()

with open(output_path + pdf_path + 'codes.txt', 'w') as file:
    file.write('\n '.join(map(str, codes)))
