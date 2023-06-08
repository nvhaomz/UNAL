# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 00:14:28 2023
@author: nvhao
"""

# pip install pymupdf


import fitz
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


archivo = fitz.open('C:/_/_UNAL/proyecto/LAREP_2023_febrero_28.pdf')

#archivo = fitz.open('C:/_/_UNAL/proyecto/salud_S2023001075.pdf')

print(os.path.curdir)

print(type(archivo))

print(archivo.metadata)

print(len(archivo))                 # numero de paginas

pag1 = archivo.load_page(1)         # carga la pagina 0

print(type(pag1))

imagen = pag1.get_pixmap()          # captura de pantalla de la pagina 0

print(type(imagen))

imagen.save("pagina1.png")          # guarda la imagen como un png


img = mpimg.imread("pagina1.png")   # lee la imagen

print(os.path.exists("pagina1.png"))

# fig, ax = plt.subplots(figsize=(7, 10))
# ax.imshow(img)
# ax.axis("off")


# EXTRAER EL TEXTO

#print("PAGINA 1 -----------------------------------------------------------")
#texto = pag0.get_text("text")
#print(texto)

#print("PAGINA 2 -----------------------------------------------------------")
#texto2 = archivo.load_page(9).get_text("text")
#print(texto2)



textoCompleto = [pagina.get_text('text') for pagina in archivo]
#print(textoCompleto)
#print(len(textoCompleto))



#for pagina in textoCompleto:
#    print(pagina)
#    print('------------')



print("PAGINA N -----------------------------------------------------------")
#textoN = archivo.load_page(0).get_text("text")
#textoN = archivo.load_page(0).get_text("text").encode("utf-8").decode("latin1")

#textoN = archivo.load_page(0).get_text("text").decode("utf-8")
textoN = archivo.load_page(1).get_text("text").encode("utf-8").decode("utf-8")
#textoN = archivo.load_page(0).get_text("text").encode("latin1").decode("latin1")
print(textoN)



