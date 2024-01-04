from pypdf import PdfMerger
pdfs = []
no_of_pdf = int(input("Enter the number of pdf you want to merge"))
for i in range(no_of_pdf):
    pdf_name = input("Enter the pdf name")
    pdfs.append(pdf_name)


merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()