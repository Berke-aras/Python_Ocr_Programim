from PIL import Image
from pytesseract import pytesseract
import tkinter as tk
from tkinter import filedialog
import subprocess 
import os

#with open('path.txt') as f:
#    line = f.readline().strip('\n')
#path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_tesseract = os.path.expandvars(r'%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe')



#tessaract.exe path i

path_to_tesseract = path_to_tesseract


#resim yolu

file_path = filedialog.askopenfilename()


#tessaract_cmd -> tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#PIL ile resim acma

img = Image.open(file_path)

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
print(desktop)
#resimden yazı cikarma
try:
    text = pytesseract.image_to_string(img)
except:
    subprocess.call("tesseract-ocr-w64-setup-5.3.0.20221222.exe", shell=True) 

print(text)

with open(f'{desktop}\sonuc.txt', 'w') as f:
    f.write(text)