import PyPDF2 as PDF
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PDF.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(input('Please name your new pdf file: ')+'.pdf')
    print('All done!')

pdf_combiner(inputs)






