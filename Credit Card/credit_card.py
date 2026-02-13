## This is a credit card payment information page

## importing the files
import flet as ft
from datetime import datetime as dt

## constructing the main function
def main(page: ft.Page):
    ## --> PAGE DETAILS <-- ##
    page.title = "Credit Card Payment"
    page.window.width = 400
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=50

    ## --> FUNCTIONS <-- ##
    
    ## --> CONTENT <-- ##
    
    ## TITLE: Paymment
    lbl_title = ft.Text(
        value="Credit Card Info",
        size=15,
        weight=ft.FontWeight.BOLD
    )

    ## ----------

    ## LABEL: Holder Name
    lbl_holname = ft.Text(
        value="Credit Card Holder Name",
        size=13,
        weight=ft.FontWeight.BOLD
    )

    ## FIELD: Holder Name
    txt_holname = ft.TextField(
        expand=True
    )

    ## ----------

    ## EXPANSE: Note About Name
    exp_name_note = ft.ExpansionPanelList(
        controls=[
            ft.ExpansionPanel(
            header=ft.Container(
                content=ft.Text(value = "Reminder", size=10, color=ft.Colors.GREEN_900, weight=ft.FontWeight.BOLD),
                padding=10),
            content=ft.Container(
                content=ft.Text(size=8, value = "Please provide the name as it appears in the card."),
                padding=5
            )
            )
        ],
        spacing=10
    )

    ## ----------
    
    ## LABEL: Card Number 
    lbl_card_number = ft.Text(
        value="Credit Card Number", 
        size=13,
        weight=ft.FontWeight.BOLD
    )

    ## FIELD: Credit Card Number
    txt_card_number = ft.TextField(
        password=True,
        can_reveal_password=True
    )

    ## LABEL: CSV
    lbl_csv = ft.Text(
        value="CSV",
        size=13,
        weight=ft.FontWeight.BOLD
    )

    ## FIELD: CSV
    txt_csv = ft.TextField(
        password=True,
        can_reveal_password=True
    )

    ## ---------

    ## BUTTIN: Submit
    btn_submit = ft.Button(
        content=ft.Text("Submit"),
        icon=ft.Icons.SEND,
        expand=True,
        bgcolor=ft.Colors.BLUE_ACCENT,
        color=ft.Colors.WHITE,
        icon_color=ft.Colors.WHITE
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

    ## COLUMN: Card Holder Name
    col_holname = ft.Column(
        controls=[
            lbl_holname,
            txt_holname,
            exp_name_note
        ]
    )

    ## COLUMN: Card Number
    col_number = ft.Column(
        controls=[
            lbl_card_number,
            txt_card_number
        ],
        expand=1
    )

    ## COLUMN: CSV
    col_csv = ft.Column(
        controls=[
            lbl_csv,
            txt_csv
        ], expand=1
    )

    ## ROW: Card Details
    row_card_details = ft.Row(
        controls=[
            col_number,
            col_csv
        ], expand=True
    )

    ## ----------

    ## ROW: Submit Button
    row_submit = ft.Row(
        controls=[
            btn_submit
        ]
    )

    ## ----------
    
    ## COLUMN: Main Column
    col_main = ft.Column(
        controls=[
            row_title,
            ft.Divider(),
            col_holname,
            row_card_details,
            ft.Divider(),
            row_submit
        ]
    )

    ## ----------

    ## CONTAINER: Main Container
    con_main = ft.Container(
        content=col_main
    )

    ## --> INTERACE <-- ##
    page.add(con_main)

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")