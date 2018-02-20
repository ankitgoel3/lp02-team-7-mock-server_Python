# importing required modules
from PyPDF2 import PdfFileReader
 
# creating a pdf file object
pdfFileObj = open('D:\Personal\Folder1\Expense Claims\Globe Moving\Sales - Invoice DEL002368.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)
content = ""
for i in range(0, pdfReader.numPages):
    content += pdfReader.getPage(i).extractText() + "\n"

print(content)

 
# # creating a page object
# pageObj = pdfReader.getPage(0)
 
# # extracting text from page
# print(pageObj.extractText())
 
# # closing the pdf file object
# pdfFileObj.close()