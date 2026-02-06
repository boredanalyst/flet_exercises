import flet as ft


def main(page: ft.Page)-> None:
    page.title = "Inbox"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    ## creating the buttons
    btn_inbox = ft.IconButton(icon = ft.Icons.MAIL_OUTLINE, tooltip="Messages", badge=ft.Badge(label="3", small_size=10))
    btn_request = ft.IconButton(icon = ft.Icons.PAGES_OUTLINED, tooltip = "Orders", badge=ft.Badge(label="", small_size=10, bgcolor = ft.Colors.AMBER))
    btn_notif = ft.IconButton(icon = ft.Icons.NOTIFICATIONS_OUTLINED, tooltip = "Notifications", badge = ft.Badge(label="10", small_size=10))

    ## creating the row
    row_navi = ft.Row(controls=[
        btn_inbox,
        btn_request,
        btn_notif
    ], alignment= ft.MainAxisAlignment.CENTER)


    page.add(
        ft.Container(content=row_navi, alignment = ft.Alignment.CENTER)
    )

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")