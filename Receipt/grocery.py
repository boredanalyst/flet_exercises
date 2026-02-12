import flet as ft
import os
from fpdf import FPDF
from datetime import datetime as dt

## -- FILEPATH -- ##


## Creating the file path

folder = "Receipt\\sample receipts"
os.makedirs(folder, exist_ok=True)

filename = "grocer.pdf"
filepath = os.path.join(folder, filename)


## -- PDF -- ##

pdf = FPDF(orientation="portrait", format="Letter")

## Create the page details
pdf.set_margins(left=10, top=5, right=10)
pdf.add_page()

## Creating the upper area
pdf.set_font(family="Arial", size=15, style="B")
pdf.ln(10)
pdf.cell(0, 10, txt="GROCERY RECEIPT", ln=True, align="C")

## Add the address
pdf.set_font(family="Arial", size=8)
pdf.cell(0, 5, txt="111 Mahogany St.", ln=True, align="C")
pdf.cell(0, 5, txt="Southeast Forest Drive", ln=True, align="C")
pdf.cell(0, 5, txt="Midtown, New York", ln=True, align="C")

## Adding a line
pdf.set_line_width(0.1)
pdf.line(10, pdf.get_y() + 5, 200, pdf.get_y() + 5)
pdf.ln(10)

## Add the items:
pdf.set_font(family="Arial", size=10)

## Venti Chocolate
pdf.cell(10, 5, txt="1 Venti Chocolate Latte")
pdf.set_x(150)
pdf.cell(10, 5, txt="$13.90", ln=True)

## Oat Milk cup
pdf.cell(10, 5, txt="1 Cup Oat Milk")
pdf.set_x(150)
pdf.cell(10, 5, txt="$0.50", ln=True)

## Chocolate Pie
pdf.cell(10, 5, txt="1 Chocolate Pie")
pdf.set_x(150)
pdf.cell(10, 5, "$15.90", ln=True)

## Grande Mocha Latte
pdf.cell(10, 5, txt="1 Grande Mocha Latte")
pdf.set_x(150)
pdf.cell(10, 5, "$13.90", ln=True)

## Create the subtotal
pdf.set_font(family="Arial", size=10, style="B")
pdf.set_x(100)
pdf.cell(10, 5, txt="Subtotal")
pdf.set_x(150)
pdf.cell(10, 5, txt="$44.20", ln=True)

## Create the tax line
pdf.set_x(100)
pdf.cell(10, 5, txt="Tax")
pdf.set_x(150)
pdf.cell(10, 5, txt="$4.20", ln=True)

## Create the Total line
pdf.ln(10)
pdf.set_x(100)
pdf.cell(10, 5, txt="Total")
pdf.set_x(150)
pdf.cell(10, 5, txt="$48.40", ln=True)

## Adding a line
pdf.set_line_width(0.1)
pdf.line(10, pdf.get_y() + 5, 200, pdf.get_y() + 5)
pdf.ln(10)

## Add the contact details
pdf.set_font(family="Arial", size=10)
pdf.cell(0, 5, txt="013-230-230", align="C", ln=True)
pdf.cell(0, 5, txt="grocerycafe@amt.com", align="C", ln=True)

## Add the timeline
pdf.set_font(family="Arial", size=8)
time = dt.today().strftime("%H:%M")
date = dt.today().strftime("%m/%d/%Y")
pdf.cell(0, 5, txt=f'{date} {time}', align="C")


## Output the PDF file
pdf.output(filepath)

print("Program initiated successfully.")