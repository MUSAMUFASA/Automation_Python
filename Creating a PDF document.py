#Step 1 - Importing the fpdp library for pdfs

from fpdf import FPDF

#Step 2 - Creating the pdf page with a portrait and A4 format
pdf = FPDF(orientation='P',unit='pt',format = 'A4')
pdf.add_page()

#Step 3 - Adding an image to the PDF page
pdf.image('IMG_9140.jpg',w=80,h=50)

#Step 4 - Setting the font and font size, whilst also drawing up a cell to contain a text and ending with a line break.
pdf.set_font(family="Times",style="B",size=24)
pdf.cell(w=0, h=50, txt="Kawu",align='C',ln=1)

#Step 5 - Setting the font and font size, whilst also drawing up a cell to contain a text and ending with a line break.
pdf.set_font(family="Times",style="B",size=14)
pdf.cell(w=0, h=50, txt="Description",ln=1)

#Step 6 - Setting the font and font size, whilst also drawing up a cell to contain multiple lines of text.
pdf.set_font(family="Times",size=12)
txt1 = """I am Kawu Musa. From Kogi. Living in Abuja"""
pdf.multi_cell(w=0,h=15,txt=txt1)

#Step 7 - Setting the font and font size, whilst also drawing up a cell to contain a text and end with a line break.
pdf.set_font(family="Times",style="B",size=24)
pdf.cell(w=100, h=50, txt="Kingdom",ln=1)


#Step 8 - Setting the font and font size, whilst also drawing up a cell to contain a text and end with a line break.
pdf.set_font(family="Times",style="B",size=24)
pdf.cell(w=100, h=50, txt="Animalia",ln=1)

#Step 9 - Saving the pdf file.
pdf.output('Kawu.pdf')