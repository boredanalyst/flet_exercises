import flet as ft
import pandas as pd

def main(page: ft.Page) -> None:
    ## --> PAGE DETAILS <-- ##
    page.title = "Ticket Submission"
    page.window.width = 400
    page.window.height = 500
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT

    ## --> VARIABLES <-- ##

    ## --> FUNCTIONS <-- ##
    
    ## Validate fields
    def validateText(e) -> None:
        if txt_email.value == "":
            page.show_dialog(alt_missing)
            return
        elif txt_pass.value == "":
            page.show_dialog(alt_missing)
            return
        
    def checkRecords(e) -> None:
        ## Parse the accounts csv file
        csv = pd.read_csv(r'Ticket System\docs\accounts.csv')

        user_email = txt_email.value
        pass_word = txt_pass.value

        csv = csv[csv["email"] == user_email]

        if len(csv) > 0:
            print("Email found")
        else:
            page.show_dialog(alt_invalid)
            return
        
        print(csv)
        print(f'EMAIL ADDRESS: {csv["email"][0]}')
        print(f'PASSWORD: {csv["password"][0]}')
        
    ## Submit Button
    def submitRecord(e) -> None:
        validateText(e)
        checkRecords(e)

    ## --> CONTENT <-- ##
    
    ## Title: Welcome to Tixet
    lbl_tixet = ft.Text(
        value="Welcome to Tixet",
        text_align=ft.TextAlign.CENTER,
        size=30,
        weight=ft.FontWeight.BOLD
    )

    ## Label: Input your details
    lbl_input = ft.Text(
        value="Input your details"
    )

    ## --> WRAPPER <-- ##
    
    ## Column: Title
    col_title = ft.Column(
        controls=[
            lbl_tixet,
            lbl_input
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    ## Column: Body
    
    ## Label: Email Address
    lbl_email = ft.Text(
        value="Email Address",
        weight=ft.FontWeight.BOLD
    )

    ## TextField: Email Address
    txt_email = ft.TextField(
        label="Provide a valid email address."
    )

    ## Label: Password
    lbl_pass = ft.Text(
        value="Password",
        weight=ft.FontWeight.BOLD
    )

    ## TextField: Password
    txt_pass = ft.TextField(
        label="Provide your password",
        password=True,
        can_reveal_password=True
    )

    ## Button: Submit
    btn_submit = ft.Button(
        on_click=submitRecord,
        content=ft.Text("Submit"),
        icon=ft.Icons.SEND,
        expand=1,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.Colors.BLUE_400,
            color=ft.Colors.WHITE,
            icon_color=ft.Colors.WHITE
        )
    )

    ## Alert Dialog: Missing Fields
    alt_missing = ft.AlertDialog(
        content=ft.Text("Missing Email or Password."),
        icon=ft.Icons.WARNING,
        title=ft.Text("Missing Data", weight=ft.FontWeight.BOLD),
        open=False
    )

    ## Alert Dialog: Invalid Email or Password
    alt_invalid = ft.AlertDialog(
        content=ft.Text("Wrong Account Details"),
        icon=ft.Icons.WARNING,
        title=ft.Text("Invalid Email or Password", weight=ft.FontWeight.BOLD),
        open=False
    )

    ## --> WRAPPERS <-- ##

    ## Row: Submit Button
    row_submit = ft.Row(
        controls=[
            btn_submit
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        margin=10
    )
    
    ## Column: Main Column:
    col_main = ft.Column(
        controls=[
            col_title,
            ft.Divider(),
            lbl_email,
            txt_email,
            lbl_pass,
            txt_pass,
            row_submit
        ]
    )

    ## Container: Main Container:
    con_main = ft.Container(
        content=col_main,
        alignment=ft.Alignment.CENTER
    )

    ## --> CONSTRUCTING THE PAGE <-- ##
    page.add(con_main)


if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")