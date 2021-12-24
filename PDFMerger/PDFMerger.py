import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open(f'{sys.argv[1]}', 'rb'))
watermark = PyPDF2.PdfFileReader(open(f'{sys.argv[2]}', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open(f'{sys.argv[3]}', 'wb') as file:
        output.write(file)
