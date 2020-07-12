import PyPDF2


imputPDfs = ["one.pdf", "two.pdf", "four.pdf"]


def pdf_merger(pdf_list):
    # object pdfFileMerger
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("newpdf.pdf")


pdf_merger(imputPDfs)
