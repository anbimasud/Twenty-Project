from PyPDF2 import PdfMerger

AllPdf = ["first.pdf", "sceond.pdf"]

MyMerger = PdfMerger()

for NewPDF in AllPdf:
    MyMerger.append(NewPDF)

MyMerger.write("Expecter.pdf")
MyMerger.close()