import flet as ft
import time

def main(page: ft.Page) -> None:
    page.title = "Login Screen"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.width = 10

    ## functions 

    def errorLogin(e) -> None:
        page.show_dialog(ban_login_error)

    ## text fields
    inp_user_name = ft.TextField(label="Enter your username", border_radius=10)
    inp_password = ft.TextField(label="Enter your password", border_radius=10, password=True, can_reveal_password=True)

    ## buttons 

    btn_submit = ft.Button(content="Log in", bgcolor=ft.Colors.BLUE, on_click = errorLogin)

    ## banners 

    ban_login_error = ft.Banner(
        content = ft.Text("Login details invalid."),
        actions = [ft.Button(content="Dismiss")],
        open = True
    )


    ## building the components
    row_label = ft.Row(controls=[
        ft.Text(value="Log in", size=30, weight=ft.FontWeight.BOLD)
    ], alignment = ft.MainAxisAlignment.CENTER)

    row_username = ft.Row(controls=[
        inp_user_name
    ], alignment = ft.MainAxisAlignment.CENTER)

    row_password = ft.Row(controls=[
        inp_password
    ], alignment = ft.MainAxisAlignment.CENTER)

    row_submit = ft.Row(controls=[
        btn_submit
    ], alignment = ft.MainAxisAlignment.CENTER)

    col_main = ft.Column(controls=[
        row_label,
        row_username,
        row_password,
        row_submit
    ], alignment= ft.MainAxisAlignment.CENTER)

    ## building the main container
    page.add(ft.Container(content=col_main, alignment = ft.Alignment.CENTER))


if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")