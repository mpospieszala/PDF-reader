#encoding: utf-8
__author__ = 'Magdum'
__version__ = '1.0 beta'

import pyPdf
import re
import glob

def getPDFContent(path):
    content = ''
    # Load PDF into pyPDF:
    pdf = pyPdf.PdfFileReader(file(path, 'rb'))
    # Iterate pages:
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content:
        content += pdf.getPage(i).extractText() + '\n'
    return content

def matchURLs(value):
    ret = []
    for url in re.findall('((https?:\/\/|www.)+([\da-z\.-]+)\.([a-z\.]{2,6}))', value):
        ret.append(url[0])
    return ret

if __name__ == '__main__':
    f = open('URLlist.txt', 'w+')
    # search for all pdf files in directory:
    for files in glob.glob('*.pdf'):
        pdfContent = getPDFContent(files)
        urls = matchURLs(pdfContent)
        for url in urls:
            # skip paulieciara domain
            if url == 'http://www.paulieciara.com':
                continue
            elif url == 'www.paulieciara.com':
                continue
            # skip yourdomain domain
            elif url == 'http://www.yourdomain.com':
                continue
            elif url == 'http://yourdomain.com':
                continue
            else:
                f.writelines(url + '\n')
    f.close()
    print "Koniec programu"
