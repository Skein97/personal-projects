import PyPDF2 as PDF

with open('dummy.pdf', 'rb') as file:
    reader = PDF.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PDF.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as file2:
        writer.write(file2)

