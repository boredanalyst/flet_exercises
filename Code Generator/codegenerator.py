## import libraries

import flet as ft
import random as rand
import string
from datetime import datetime as dt
import string

## Create the main function
def main(page: ft.Page) -> None:
    ## --> PAGE DETAILS <-- ##
    page.title = "Code Generator"
    page.window.width = 400
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=20

    ## --> FUNCTIONS <-- ##

    def addCode(e) -> None:

        ## Generating the Code
        date_today = dt.today().strftime("%m%d%y")
        print(date_today)

        gen_code_A = string.ascii_uppercase[rand.randint(0,len(string.ascii_uppercase)-1)]
        print(gen_code_A)

        gen_code_B = string.ascii_uppercase[rand.randint(0,len(string.ascii_uppercase)-1)]
        print(gen_code_B)

        gen_code_1 = rand.randint(1001, 9999)
        print(gen_code_1)

        gen_code_full = f'{gen_code_A}{gen_code_B}{gen_code_1}'
        print(gen_code_full)

        ## Generating the list item control
        lst_generated_code = ft.ListTile(
            leading=ft.Icons.ABC,
            title=ft.Text(size=10, value=date_today, weight=ft.FontWeight.BOLD),
            subtitle=ft.Text(size=8, value=gen_code_full)
        )

        col_body.controls.append(lst_generated_code)

    ## --> CONTENT <-- ##

    ## TITLE: Label
    lbl_title = ft.Text(
        value="Code Generator",
        size=15,
        weight=ft.FontWeight.BOLD
    )

    ## LISTITEM: Sample Code
    lst_sample = ft.ListTile(
        title=ft.Text(value="DATE TODAY", weight=ft.FontWeight.BOLD, size=12),
        subtitle=ft.Text(value="AB356S", size=10),
        leading=ft.Icons.ABC,
        expand=True,
        bgcolor=ft.Colors.AMBER_100
    )

    ## --> WRAPPERS <-- ##

    ## ROW: Title
    row_title = ft.Row(
        controls=[
            lbl_title
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    ## ----------

    ## COLUMN: Body
    col_body = ft.Column(
        controls=[
            ft.Text(value="Generated Codes", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
            lst_sample
        ], expand=True
    )


    ## ----------

    ## COLUMN: Main Column
    col_main = ft.Column(
        controls=[
            row_title,
            ft.Divider(),
            col_body
        ]
    )


    ## ----------

    ## CONTAINER: Main Container
    con_main = ft.Container(
        content=col_main
    )

    ## --> INTERFACE <--
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        bgcolor=ft.Colors.LIME_ACCENT,
        on_click=addCode
    )
    page.add(con_main)

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")