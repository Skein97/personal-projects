import PyPDF2 as PDF
import sys

content_pdf = sys.argv[1]
stamp_pdf = sys.argv[2]


# Simpler
def watermark(template, stamp):
    content = PDF.PdfFileReader(open(template, 'rb'))
    mark = PDF.PdfFileReader(open(stamp, 'rb'))
    writer = PDF.PdfFileWriter()
    with open(input('Please name your new pdf file: ') + '.pdf', "wb") as file:
        for i in range(content.getNumPages()):
            page = content.getPage(i)
            page.mergePage(mark.getPage(0))
            writer.addPage(page)
            writer.write(file)


watermark(content_pdf, stamp_pdf)

# Convoluted!!
# def watermark(content_pdf, stamp_pdf, page_indices: Union[Literal["ALL"], List[int]] = "ALL"):
#     reader = PDF.PdfFileReader(content_pdf)
#
#     if page_indices == "ALL":
#         page_indices = list(range(0, len(reader.pages)))
#
#     writer = PDF.PdfFileWriter()
#     for index in page_indices:
#         content_page = reader.pages[index]
#         mediabox = content_page.mediaBox
#
#         # You need to load it again, as the last time it was overwritten
#         reader_stamp = PDF.PdfFileReader(stamp_pdf)
#         image_page = reader_stamp.pages[0]
#
#         image_page.mergePage(content_page)
#         image_page.mediaBox = mediabox
#         writer.addPage(image_page)
#
#     with open(input('Please name your new pdf file: ') + '.pdf', "wb") as fp:
#         writer.write(fp)
#
#     print('All done!')
#
#
# watermark(content_pdf, stamp_pdf, 'ALL')
