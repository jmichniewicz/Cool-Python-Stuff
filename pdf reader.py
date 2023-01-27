import PyPDF2

pdf = open("C:\Users\michniewiczj\Desktop\Python Stuff\Python Restart\app.pdf")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extract_text())