import flet as ft
import csv
import random
import string
from datetime import date as dt

def main(page: ft.Page):
    ## --> Page Details <-- ##
    page.window.height = 750
    page.window.width = 500
    page.padding=40
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Class Enrolment"
    page.window.center()

    ## --> Variables <-- ##

    ## Dictionary for user
    dic_user = {
        "record_code":None,
        "student_name" : None,
        "student_id" : None,
        "graduating" : False,
        "classes" : []
        }
    
    letters = string.ascii_uppercase

    ## --> Functions <-- ##

    ## Identify whether the user is graduating or not
    def toGraduate(e):
        dic_user["graduating"] = chk_graduating.value

    ## Get the user's name and student ID
    def recordUser(e):
        ## validate name field
        if txt_name.value == "":
            page.show_dialog(alt_missing_data)
            return
        elif txt_stud_id.value == "":
            page.show_dialog(alt_missing_data)
            return
        
        dic_user["student_name"] = txt_name.value
        dic_user["student_id"] = txt_stud_id.value

        ## Generate a record code
        code_number = random.randint(0000,9999)
        letter_a = letters[random.randint(0,len(letters))]
        letter_b = letters[random.randint(0,len(letters))]
        full_code = f'{letter_a}{letter_b}{code_number}'
        dic_user["record_code"] = full_code

        ## Write onto a text file
        with open(f"Class Enrolment\\{dic_user["record_code"]}_ENROLMENTRECORD.txt", "w") as record:
            record.write("### ENROLMENT RECORD ###\n")
            record.write(f'CODE: {dic_user["record_code"]}\n')
            record.write(f'STUDENT: {dic_user["student_name"]}\n')
            record.write(f'STUDENT ID: {dic_user["student_id"]}\n')
            record.write(f'GRADUATING: {dic_user["graduating"]}\n')
            record.write(f'TIMESTAMP: {dt.today()}\n')
        
        ## Closing the feedback loop
        page.show_dialog(alt_enroll)

        ## Resetting everything
        txt_name.value = ""
        txt_stud_id.value = ""
        lst_philo_150.leading=ft.Icons.ADD
        lst_philo_108.leading=ft.Icons.ADD
        lst_philo_110.leading=ft.Icons.ADD
    
    ## Get the record for the class.
    def recordClass(e):
        if e.control.leading == ft.Icons.CHECK_ROUNDED:
            e.control.leading = ft.Icons.ADD
            dic_user["classes"].remove(e.control.title)
            print(dic_user["classes"])
        elif e.control.leading == ft.Icons.ADD:
            dic_user["classes"].append(e.control.title)
            dic_user["classes"] = list(set(dic_user["classes"]))
            e.control.leading=ft.Icons.CHECK_ROUNDED
            print(dic_user["classes"])
            page.show_dialog(alt_class_added)

        

    ## --> Content <-- ##
    
    ## Main Title
    lbl_title = ft.Text(
        value="Enroll Courses",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    ## Label: Student Information
    lbl_stud_info = ft.Text(
        value="Student Information",
        size=20,
        weight=ft.FontWeight.BOLD
    )

    ## Checkbox: Graduating?
    chk_graduating = ft.Checkbox(
        label="Are you graduating?",
        label_position=ft.LabelPosition.LEFT,
        on_change=toGraduate
    )

    ## Textfield: Name
    txt_name = ft.TextField(
        label="Your name"
    )

    ## Textfield: Student Number
    txt_stud_id = ft.TextField(
        label="Your Student ID"
    )

    ## Label: Classes
    lbl_classes = ft.Text(
        value="Available Classes",
        size=15,
        weight=ft.FontWeight.BOLD
    )

    ## ListTile: Philosophy 108:
    lst_philo_108 = ft.ListTile(
            leading=ft.Icons.ADD,
            title="Philosophy 108: Speculative Thought",
            subtitle="Dr. Isaac Soberano",
            on_click=recordClass
        )

    ## Card: Philosophy 108
    crd_philo_108 = ft.Card(
        content=lst_philo_108
    )

    ## ListTile: Philosophy 110:

    lst_philo_110 = ft.ListTile(
            leading=ft.Icons.ADD,
            title="Philosophy 110: Ancient Philosophy",
            subtitle="Dr. Maria Naval",
            on_click=recordClass
        )

    ## Card: Philosophy 110
    crd_philo_110 = ft.Card(
        content=lst_philo_110
    )

    ## ListTile: Philosophy 150:
    lst_philo_150 = ft.ListTile(
            leading=ft.Icons.ADD,
            title="Philosophy 150: Epistemology",
            subtitle="Dr. Albert Schweiss",
            on_click=recordClass
        )

    ## Card: Philosophy 150
    crd_philo_150 = ft.Card(
        content=lst_philo_150
    )

    ## Button: Submit Button
    btn_submit = ft.Button(
        icon=ft.Icons.SEND,
        content=ft.Text("Enroll"),
        on_click=recordUser
    )

    
    ## Alert Dialog: Missing Field Data
    alt_missing_data = ft.AlertDialog(
        title=ft.Text("Error"),
        icon=ft.Icons.WARNING,
        content=ft.Text("Name or Student ID is missing."),
        open=False
    )


    ## Alert Dialog: Successful Class Addition
    alt_class_added = ft.AlertDialog(
        title=ft.Text("Success!"),
        icon=ft.Icons.CHECK_CIRCLE,
        content=ft.Text("Class added successfully!"),
        open=False
    )

    ## Alert Dialog: Successful Enrolment
    alt_enroll = ft.AlertDialog(
        title=ft.Text("Success!"),
        icon=ft.Icons.CHECK_CIRCLE,
        content=ft.Text("You have been successfully enrolled!"),
        open=False
    )


    ## --> WRAPPERS <-- ##

    ## Column: Student Information
    col_stud_info = ft.Column(
        controls=[
            lbl_stud_info,
            txt_name,
            txt_stud_id,
            chk_graduating
        ]
    )

    ## Column: Available Classes
    col_class = ft.Column(
        controls=[
            lbl_classes,
            crd_philo_110,
            crd_philo_108,
            crd_philo_150
        ]
    )

    ## Row: Button Row
    row_submit = ft.Row(
        controls=[
            btn_submit
        ], alignment=ft.MainAxisAlignment.END
    )

    ## Main Column
    col_main = ft.Column(
        controls=[
            lbl_title,
            ft.Divider(),
            col_stud_info,
            ft.Divider(),
            col_class,
            ft.Divider(),
            row_submit
        ]
    )

    ## Main Container
    con_main = ft.Container(
        content=col_main
    )

    ## --> CONSTRUCTING THE PAGE <-- ##
    page.add(con_main)


if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")