## THIS PROJECT CREATES A CERTIFICATE.
import flet as ft
import random as rand
from datetime import datetime as dt
import pandas as pdf
import os
from fpdf import FPDF

def main(page: ft.Page) -> None:
    ## --> PAGE DETAILS <-- ##
    page.window.height = 800
    page.window.width = 500
    page.title = "Certificate Maker"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=50

    ## --> FUNCTIONS <-- ##

    ## INPUT: Show date dialog
    def chooseDateIssuance(e):
        page.show_dialog(dt_issue)
    
    ## INPUT: Record the date of issuance in a text field
    def recordDateIssuance(e):
        date_of_issue = dt_issue.value.strftime("%m/%d/%y")
        txt_issue.value = date_of_issue
        print(date_of_issue)

    ## OUTPUT: Write the certificate
    def createPDF(e, text_template, class_taken):
        ## Set the pdf details
        pdf = FPDF(orientation="landscape", unit="mm", format="A4")

        pdf.set_author("CERTSYS")
        pdf.set_creator("CERTSYS")
        pdf.set_top_margin(30)
        pdf.set_left_margin(10)
        pdf.set_right_margin(10)
        pdf.add_page()
        
        ## Create the upper section
        pdf.set_font("Times", size=40, style="B")
        pdf.cell(0, 10, txt="Certificate of Completion", align="C", ln=True)
        pdf.ln(5)

        pdf.set_font("Times", style="I", size=20)
        pdf.cell(0, 10, txt=class_taken, align="C", ln=True)
        pdf.ln(20) ## Move the cursor downwards

        pdf.set_font("Helvetica", size=15, align="C")
        pdf.cell(200, 10, txt=text_template, ln=True)


        ## Output the pdf
        pdf.output("certificate.pdf")
        pass

    ## PROCESS: Process all the details into a certificate
    def createCertificate(e):


        lst_textfields = [txt_fname, txt_lname, drop_class, txt_issue]

        ## Check the fields
        for field in lst_textfields:
            if field.value == "":
                page.show_dialog(alt_missing_details)
                return False
                break
    
        holder_fname = txt_fname.value
        holder_lname = txt_lname.value
        holder_class = drop_class.value
        holder_issue = txt_issue.value

        template = f'This is to certify that {holder_fname} {holder_lname} has successfully completed a class on {holder_class} on this day, {holder_issue}.'
        print(template)

        createPDF(e, template, holder_class)

    ## --> CONTENT <-- ##

    ## LABEL: Title
    lbl_title = ft.Text(
        value="Certificate Maker",
        weight=ft.FontWeight.BOLD,
        size=40
    )

    ## LABEL: Heading
    lbl_heading = ft.Text(
        value="Sample Text",
        weight=ft.FontWeight.BOLD
    )

    ## LABEL: Text Template
    lbl_certificate = ft.Text(
        value= "This is to certify that ________ has successfully completed a class on __________ on this day, ___________.",
        size=15
    )

    ## -------------------

    ## LABEL: First Name
    lbl_fname = ft.Text(
        value="First Name",
        weight=ft.FontWeight.BOLD
    )

    ## FIELD: First Name
    txt_fname = ft.TextField(
        hint_text="Holder's First Name",
        expand=True
    )

    ## LABEL: Last Name
    lbl_lname = ft.Text(
        value="Last Name",
        weight=ft.FontWeight.BOLD
    )

    ## FIELD: Last Name
    txt_lname = ft.TextField(
        hint_text = "Holder's Last Name",
        expand=True
    )

    ## -------------------

    ## LABEL: Date Issue
    lbl_issue = ft.Text(
        value="Date of issuance",
        weight=ft.FontWeight.BOLD
    )


    ## BUTTON: Date Issue
    btn_issue = ft.IconButton(
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=chooseDateIssuance
    )

    ## FIELD: Date Issuance
    txt_issue = ft.TextField(
        hint_text = "Date of Issuance",
        read_only=True,
        expand=True
    )

    ## DATEPICKER: Date Issue
    dt_issue = ft.DatePicker(
        entry_mode=ft.DatePickerEntryMode.INPUT,
        on_change=recordDateIssuance
        )

    ## -------------------

    ## LABEL: Class Taken
    lbl_class = ft.Text(
        value="Class Taken",
        weight=ft.FontWeight.BOLD
    )

    ## FIELD: Class Taken
    txt_class = ft.TextField(
        hint_text = "Provide class taken",
        expand=True
    )

    ## DROPDOWN: Class Taken
    drop_class = ft.Dropdown(
        options=[
            ft.DropdownOption(text = "Introduction to Data Analytics"),
            ft.DropdownOption(text = "Introduction to Microsoft Excel"),
            ft.DropdownOption(text = "Introduction to PowerBI"),
            ft.DropdownOption(text = "Advanced Microsoft Excel")
        ], expand=True
    )

    ## -------------------

    ## BUTTON: Submit
    btn_submit = ft.Button(
        content="Create Certificate",
        icon=ft.Icons.SEND,
        on_click=createCertificate
    )

    ## ----------

    ## ALERT: Missing Details
    alt_missing_details = ft.AlertDialog(
        title=ft.Text("Error"),
        content=ft.Text("Please provide all necessary details."),
        icon=ft.Icons.WARNING
    )

    ## --> WRAPPERS <-- ##

    ## ROW: Title
    row_title = ft.Row(
        controls=[
            lbl_title
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    ## ROW: Sample Template
    col_template = ft.Column(
        controls=[
            lbl_heading,
            lbl_certificate
        ]
    )

    ## COLUMN: Inputs
    col_inputs = ft.Column(
        controls=[
            lbl_fname,
            txt_fname,
            lbl_lname,
            txt_lname
        ]
    )

    ## ROW: Input Date Issuance
    row_date = ft.Row(
        controls=[
            txt_issue,
            btn_issue
        ]
    )

    ## COLUMN: Date
    col_date = ft.Column(
        controls=[
            lbl_issue,
            row_date
        ]
    )

    ## COLUMN: Class Taken
    col_class = ft.Column(
        controls=[
            lbl_class,
            drop_class
        ]
    )

    ## ROW: Submit
    row_submit = ft.Row(
        controls=[
            btn_submit
        ], alignment=ft.MainAxisAlignment.CENTER
    )



    ## COL: Main Column
    col_main = ft.Column(
        controls=[
            row_title,
            col_template,
            ft.Divider(),
            col_inputs,
            ft.Divider(),
            col_date,
            col_class,
            ft.Divider(),
            row_submit
        ]
    )

    ## CONTAINER: Main Container
    con_main = ft.Container(
        content=col_main
    )

    ## --> INTERFACE <-- ##

    page.add(con_main)

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")