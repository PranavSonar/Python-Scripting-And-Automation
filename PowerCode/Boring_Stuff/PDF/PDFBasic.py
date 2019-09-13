# pip install PyPDF2
import PyPDF2,os
os.chdir("c:/Users/Vivek Kumar/Desktop/")
pdffile=open("IntelliSense in Visual Studio Code.pdf",'rb')
pdf=PyPDF2.PdfFileReader(pdffile)
print(pdf.numPages)
page=pdf.getPage(1)
print(page.extractText())
