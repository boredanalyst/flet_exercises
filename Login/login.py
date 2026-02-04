import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.width = 10

    ## adding the components
    user_name = ft.TextField(value="", label="Your username", width=1000, margin=10)
    password = ft.TextField(value="", label="Your password", width=1000, password=True, margin=10)

    ## adding the components

    page.add(
        ft.Column(
            controls=[
                ft.Text(value="Login", text_align = ft.TextAlign.CENTER),
                user_name,
                password
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == '__main__':
    ft.run(main)
    print("Program successfully initiated")