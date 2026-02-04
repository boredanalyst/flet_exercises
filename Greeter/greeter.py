import flet as ft


def main(page: ft.Page) -> None:
    ## setting up the page
    page.title = "Greeter App"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    ## setting up some components
    greeter = ft.Text(value="Hello. What's your name?")
    name_field = ft.TextField(value="", label="Your Name", hint_text = "Please type in your name.")

    def submitName(e) -> None:
        greeter.value = f'Hello there {name_field.value}!'
        page.update()

    page.add(
        ft.Row(
            controls=[
                greeter,
                name_field,
                ft.Button(content="Submit", on_click=submitName)
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")