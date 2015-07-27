#encoding: utf-8
__author__ = 'Magdum'
__version__ = '1.0 beta'

import pyPdf
import re
import glob
import shutil
import os

def getPDFContent(path):
    content = ''
    # Load PDF into pyPDF:
    f = file(path, 'rb')
    pdf = pyPdf.PdfFileReader(f)
    # Iterate pages:
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content:
        content += pdf.getPage(i).extractText() + '\n'
    f.close()
    return content


def matchURLs(value):
    ret = []
    for url in re.findall('((https?:\/\/|www.)+([\da-z\.-]+)\.([a-z\.]{2,6}))', value):
        ret.append(url[0])
    return ret


def checkAllFiles():
    allLinkArray = []
    for files in glob.glob('*.pdf'):
        pdfContent = getPDFContent(files)
        urls = matchURLs(pdfContent)
        for url in urls:
            # skip paulieciara domain
            if url == 'http://www.paulieciara.com' or url == 'www.paulieciara.com':
                continue
            # skip yourdomain domain
            elif url == 'http://www.yourdomain.com' or url == 'http://yourdomain.com':
                continue
            else:
                allLinkArray.append(url)
                noDuplicatesArray = set(allLinkArray)
    return noDuplicatesArray

def saveUniqueLinksToFile():
    uniqueLinksSource = checkAllFiles()
    f = open('URLlist.txt', 'w+')
    for lines in uniqueLinksSource:
        f.write(lines + '\n')
    f.close()


def moveFilesAfterScraping():
    source = os.listdir('.')
    destination = '.\Done'
    if not os.path.exists(destination):
        os.mkdir(destination)
    for files in source:
        if files.endswith('.pdf'):
            shutil.move(files, destination)

if __name__ == '__main__':
    checkAllFiles()
    saveUniqueLinksToFile()
    moveFilesAfterScraping()
    print "Koniec programu"

