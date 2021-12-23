import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdfs in pdf_list:
        merger.append(pdfs)
    merger.write('super.pdf')
    print(pdf_list)


pdf_combiner(inputs)
