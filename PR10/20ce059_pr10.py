# 20CE059 Dev Nakum

from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    pass        # nothing happens when it is executed.

class PDF(FPDF):
    def lines(self):
        self.set_line_width(0.0)
        self.line(5.0,5.0,205.0,5.0) # top one
        self.line(5.0,292.0,205.0,292.0) # bottom one
        self.line(5.0,5.0,5.0,292.0) # left one
        self.line(205.0,5.0,205.0,292.0) # right one



pdf = PDF()      #pdf object
# pdf=PDF(orientation='L') # landscape
# pdf=PDF(unit='mm') #unit of measurement
# pdf=PDF(format='A4') #page format. A4 is the default value of the format, you don't have to specify it.
# # full syntax


#default
pdf = PDF(orientation='P', unit='mm', format='A4')

pdf.add_page()


image_1 = Image.open(r'D:\clg\Python Practical\PR10\Sem3.jpeg')
im1 = image_1.convert('RGB')
im1.save(r'D:\clg\Python Practical\20CE059.pdf')


pdf_w=210
pdf_h=297