import flet as ft

def main(page: ft.Page) -> None:
    page.title = "Inbox Labels"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.spacing = 30

    btn_unread = ft.Button(badge = ft.Badge(label="3", bgcolor=ft.Colors.RED), content="Unread", icon = ft.Icons.EMAIL, style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_read = ft.Button(content="Read", icon = ft.Icons.MARK_EMAIL_READ, style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_spam = ft.Button(badge = ft.Badge(label="10", bgcolor=ft.Colors.RED), content="Spam", icon = ft.Icons.CANCEL, style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_trash = ft.Button(badge = ft.Badge(label="4", bgcolor=ft.Colors.RED), content="Trash", icon = ft.Icons.DELETE, style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))
    btn_exit = ft.Button(content="Exit", icon = ft.Icons.EXIT_TO_APP, style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)))

    col_label = ft.Column(controls=[
        btn_unread,
        btn_read,
        btn_spam,
        btn_trash,
        btn_exit
    ], expand= True)

    page.add(
        ft.Container(content=col_label, alignment = ft.Alignment.CENTER)
    )

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")