import argparse
from PyPDF4 import PdfFileReader

#Este programa sirve para encontrar la metadata de un archivo PDF
def imprimir_metadata(nombreArchivo):
    with open(nombreArchivo, 'rb') as pdf:
        pdf_file = PdfFileReader(pdf)
        doc_info = pdf_file.getDocumentInfo()
        print(f'[*] MetaData PDF para el archivo: {str(nombreArchivo)}')
        for meta_item in doc_info:
            print(f'[+] {meta_item}: {doc_info[meta_item]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 pdf_read.py PDF_FILE_NAME')
    parser.add_argument('pdf_file', type=str, metavar='PDF_FILE_NAME',
                        help='specify the name of the PDF file')

    args = parser.parse_args()
    imprimir_metadata(args.pdf_file)
