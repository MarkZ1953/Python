from PIL import Image
from pytesseract import *

#pytesseract.tesseract_cmd

img = Image.open("ImagenVidaMuerteImagenes.png")

resultado = pytesseract.image_to_string(img,lang="spa")

print(resultado)