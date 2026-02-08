import flet as ft

## Defining the main function
def main(page: ft.Page) -> None:
    ## --> DEFINING THE PAGE <-- ##
    page.title = "Hotel Booking"
    page.window.height = 500
    page.window.width = 500
    page.window.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    ## --> CONTENT <-- ##
    
    ## Label: Title
    lbl_title = ft.Text(
        value="Hotel Booking",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    ## Card: Hotel ABC
    crd_hotel_abc = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ListTile(
                        title=ft.Text(value="Hotel ABC", weight=ft.FontWeight.BOLD),
                        subtitle="$156.00 per night"
                    ),
                    ft.Divider(),
                    ft.Row(
                        controls=[
                            ft.Chip(
                                label=ft.Text("Amenities", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                leading=ft.Icon(ft.Icons.SHOWER),
                                color=ft.Colors.GREY_400
                            ),
                            ft.Chip(
                                label=ft.Text("Valet Services", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                leading=ft.Icon(ft.Icons.CAR_REPAIR),
                                color=ft.Colors.GREY_400
                            ),
                            ft.Chip(
                                label=ft.Text("Gym Area", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                leading=ft.Icon(ft.Icons.SPORTS_GYMNASTICS),
                                color=ft.Colors.GREY_400
                            )
                        ]
                    )
                ]
            ), padding=10
        )
    )

    ## Card: EFG Hotels
    crd_hotel_efg = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ListTile(
                        title=ft.Text(value="EFG Hotels", weight=ft.FontWeight.BOLD),
                        subtitle="$200.00 per night"
                    ),
                    ft.Divider(),
                    ft.Row(
                        controls=[
                            ft.Chip(
                                label=ft.Text("Amenities", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                leading=ft.Icon(ft.Icons.SHOWER),
                                color=ft.Colors.GREY_400
                            ),
                            ft.Chip(
                                label=ft.Text("Meals Included", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                leading=ft.Icon(ft.Icons.COOKIE),
                                color=ft.Colors.GREY_400
                            ),
                            ft.Chip(
                                label=ft.Text("Gym Area", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                leading=ft.Icon(ft.Icons.SPORTS_GYMNASTICS),
                                color=ft.Colors.GREY_400
                            )
                        ]
                    )
                ]
            ), padding=10
        )
    )

    ## --> WRAPPERS <-- ##

    ## column: Main 
    col_main = ft.Column(
        controls=[
            lbl_title,
            ft.Divider(),
            crd_hotel_abc,
            crd_hotel_efg
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
    print("Program initiated successfully.")