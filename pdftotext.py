import pypdfium2 as pdfium
from PIL import Image, ImageTk
from pytesseract import pytesseract
import tkinter as tk
from tkinter import filedialog
import subprocess 
import os
import tkinter as tk
from time import sleep

def task():
    try:
        os.mkdir("pdftoimg")
    except:
        print("hata")
    finally:
        imglist = list()

        pdf = filedialog.askopenfilename()
        pdf = pdfium.PdfDocument(pdf)
        n_pages = len(pdf)
        for page_number in range(n_pages):
            page = pdf.get_page(page_number)
            pil_image = page.render_topil(
                scale=8,
                rotation=0,
                crop=(0, 0, 0, 0),
                greyscale=False,
                optimise_mode=pdfium.OptimiseMode.NONE,
            )
            pil_image.save(f"pdftoimg/image_{page_number+1}.png")
            imglist.append(f"image_{page_number+1}.png")


        print(imglist)


        path_to_tesseract = os.path.expandvars(r'%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe')




        path_to_tesseract = path_to_tesseract



        desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
        print(desktop)
        with open(f'{desktop}\sonuc.txt', 'w') as f:
                f.write("")

        for i in imglist:
            file_path = f"pdftoimg/{i}"
            

            #tessaract_cmd -> tessaract.exe
            pytesseract.tesseract_cmd = path_to_tesseract

            #PIL ile resim acma

            img = Image.open(file_path)
            
            

            #resimden yazı cikarma
            try:
                text = pytesseract.image_to_string(img)
                if len(text) < 5:
                    continue
            except:
                subprocess.call("tesseract-ocr-w64-setup-5.3.0.20221222.exe", shell=True)
                break
            
            print(text)

            with open(f'{desktop}\sonuc.txt', 'a') as f:
                f.write(text)

        dir = 'pdftoimg'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        

    root.destroy()

root = tk.Tk()
root.title("Pdf to text")
img = ImageTk.PhotoImage(Image.open("gif.gif"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
label = tk.Label(root, text="Bitmesi bekleniyor. Otomatik Kapanacak")
label.pack()

root.after(200, task)
root.mainloop()

print("Main loop is now over and we can do other stuff.")


