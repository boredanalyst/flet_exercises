import flet as ft

def main(page: ft.Page) -> None:
    ## --> PAGE DETAILS <-- ##
    page.window.height = 500
    page.window.width = 500
    page.title = "Note Taker"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50

    ## --> FUNCTIONS <-- ##

    def showDatePicker(e):
        page.show_dialog(dt_insert_date)
    
    def chooseDate(e):
        time_chosen = e.control.value.strftime('%m/%d/%Y')
        txt_note.value += time_chosen
    
    ## --> CONTENT <-- ##

    ## BUTTON: FILE
    btn_save = ft.IconButton(
        icon=ft.Icons.SAVE,
        tooltip="File Options"
    )

    ## TITLE: Main Heading
    lbl_title = ft.Text(
        value="Note Taker",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    ## LABEL: Label for Textfield
    lbl_note = ft.Text(
        value="Your Note",
        weight=ft.FontWeight.BOLD
    )

    ## TEXTFIELD: For Notes
    txt_note = ft.TextField(
        multiline=True,
        height=500,
        icon=ft.Icons.TEXT_FIELDS
    )

    ## BUTTON: Choose Date
    btn_date = ft.IconButton(
        icon=ft.Icons.CALENDAR_TODAY,
        on_click=showDatePicker,
        tooltip="Insert Date"
    )

    ## DATEPICKER: Insert Date
    dt_insert_date = ft.DatePicker(
        on_change=chooseDate
    )

    ## --> WRAPPER <-- ##
    
    ## COLUMN: Sidebar
    col_btn = ft.Column(
        controls=[
            btn_save,
            btn_date
        ], alignment= ft.CrossAxisAlignment.BASELINE
    )

    ## COLUMN: Body
    col_body = ft.Column(
        controls=[
            lbl_title,
            ft.Divider(),
            lbl_note,
            txt_note
        ]
    )

    ## ROW: Main
    row_main = ft.Row(
        controls=[
            col_btn,
            col_body
        ], vertical_alignment = ft.CrossAxisAlignment.START
    )

    ## CONTAINER: Main Container
    con_main = ft.Container(
        content=row_main
    )
    

    ## --> CONSTRUCTING THE PAGE <-- ##
    page.add(con_main)


if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")