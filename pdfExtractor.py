from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = 'Document1.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfFileReader(pdf_file_path)

pages = [1]
pdfWriter = PdfFileWriter()

for pageNum in pages:
    pdfWriter.addPage(pdf.getPage(pageNum))

with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f :
    pdfWriter.write(f)
    f.close()