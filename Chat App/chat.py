import flet as ft

def main(page: ft.Page):
    
    ## --> PAGE DETAILS <-- ##
    page.title = "Chattie"
    page.window.width = 500
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.LIGHT

    ## --> CONTENT <-- ##

    ## Title: Chattie
    lbl_title = ft.Text(
        value="Chattie",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    ## ListTile: Emma Chat
    lst_emma = ft.Container(
        content = ft.ListTile(
        leading=ft.CircleAvatar(content=ft.Text("EW"), bgcolor=ft.Colors.AMBER),
        title=ft.Text(value="Emma Warren", weight=ft.FontWeight.BOLD),
        subtitle=ft.Text(value="How are you doing today boo?", size=10)
    ), padding=5,
    bgcolor=ft.Colors.GREY_200,
    border_radius=10
    )

    ## ListTile: Mason Chat
    lst_mason = ft.Container(
        content = ft.ListTile(
        trailing=ft.CircleAvatar(content=ft.Text("MF", color=ft.Colors.WHITE), bgcolor=ft.Colors.ORANGE_900),
        title=ft.Text(value="Mason Fielding", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        subtitle=ft.Text(value="Much better. The doctor discharged me.", size=10, color=ft.Colors.WHITE)
    ), padding=5,
    bgcolor=ft.Colors.BLUE_900,
    border_radius=10
    )

    ## ListTile: Emma Chat 2
    lst_emma_2 = ft.Container(
        content = ft.ListTile(
        leading=ft.CircleAvatar(content=ft.Text("EW"), bgcolor=ft.Colors.AMBER),
        title=ft.Text(value="Emma Warren", weight=ft.FontWeight.BOLD),
        subtitle=ft.Text(value="That's great! But remember to rest still.", size=10)
    ), padding=5,
    bgcolor=ft.Colors.GREY_200,
    border_radius=10
    )

    ## ListTile: Mason Chat 2
    lst_mason_2 = ft.Container(
        content = ft.ListTile(
        trailing=ft.CircleAvatar(content=ft.Text("MF", color=ft.Colors.WHITE), bgcolor=ft.Colors.ORANGE_900),
        title=ft.Text(value="Mason Fielding", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        subtitle=ft.Text(value="Haha, yeah. Will do.", size=10, color=ft.Colors.WHITE)
    ), padding=5,
    bgcolor=ft.Colors.BLUE_900,
    border_radius=10
    )

    ## --> WRAPPERS <-- ##

    ## Row: Title
    row_title = ft.Row(
        controls=[
            lbl_title
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    ## Row: Emma Chat
    row_emma = ft.Row(
        controls=[
            lst_emma
        ]
    )



    ## Column: Body
    col_body = ft.Column(
        controls=[
            lst_emma,
            lst_mason,
            lst_emma_2,
            lst_mason_2
        ]
    )

    ## Column: Main
    col_main = ft.Column(
        controls=[
            row_title,
            ft.Divider(),
            col_body
        ]
    )



    ## Container: Main
    con_main = ft.Container(
        content=col_main
    )

    ## --> CONSTRUCTING THE PAGE <-- ##
    page.add(con_main)


if __name__ == '__main__':
    ft.run(main)
    print("Program ran initiated successfully.")