# pyPDF website read karo 
# write a program to manipulate pdf files using pyPDF your program should be able to merge multiple pdf you are welcome to add more functaionlities 
# pypdf is a free and open-source pure python PDF library capable of spliting merging and croppoing and transforming the pages of pdf files it can also add custom datta viewing options and password to pdf
# pyPDF can retrive text and metadata from pdf as well 

# from PyPDF2 import PdfWriter
# import os 
# merger = PdfWriter()
# files=os.listdir()
# for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
#     merger.append(pdf)
# merger.write("merged-pdf.pdf")
# merger.close()


from pypdf import PdfWriter
import os 

merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
















