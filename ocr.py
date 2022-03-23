# -*- coding:utf-8 -*-
import cv2

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

img_cv = cv2.imread('./assets/image_2.png')

print(pytesseract.image_to_string(Image.open('./assets/image_2.png'), lang='kor'))
print(pytesseract.image_to_string(img_cv, lang='kor'))
