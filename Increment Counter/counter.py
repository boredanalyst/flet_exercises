import flet as ft


## adding the main page for all the functions

def main(page: ft.Page) -> None:
    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"

    text_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def decrement(e) -> None:
        print("value decreased")
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e) -> None:
        print("value increased")
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    page.add(
        ft.Row(controls=
            [ft.IconButton(ft.Icons.ARROW_BACK, on_click = decrement),
             text_number,
             ft.IconButton(ft.Icons.ARROW_FORWARD, on_click = increment)],
             alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully")