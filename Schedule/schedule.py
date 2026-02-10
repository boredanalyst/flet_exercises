import flet as ft


def main(page: ft.Page) -> None:
    ## --> PAGE DETAILS <-- ## 
    page.window.height = 800
    page.window.width = 700
    page.padding = 50
    page.title = "Class Schedules"
    page.theme_mode = ft.ThemeMode.LIGHT

    ## --> FUNCTIONS <-- ##

    ## --> CONTENT <-- ##

    ## LABEL: Title
    lbl_title = ft.Text(
        value="Class Schedules",
        weight=ft.FontWeight.BOLD,
        size=40
    )

    ## LABEL: YOUR NAME
    lbl_name = ft.Text(
        value="Your name"
    )

    ## TEXTFIELD: YOUR NAME
    txt_name = ft.TextField(
        label="Provide your name",
        expand=True
    )

    ## LABEL: Program
    lbl_program = ft.Text(
        value="Your Program"
    )

    ## DROPDOWN: Program
    drop_program = ft.Dropdown(
        options=[
            ft.DropdownOption(
                key="psych", text="Psychology"
            ),
            ft.DropdownOption(
                key="socio", text="Sociology"
            ),
            ft.DropdownOption(
                key="anthro", text="Anthropology"
            )
        ], expand=True
    )

    ## BUTTON: Enroll
    btn_enroll = ft.IconButton(
        icon=ft.Icons.ADD
    )

    ## TABLE: Class Schedules
    tbl_sched = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Course Code", weight=ft.FontWeight.BOLD, size=15)),
            ft.DataColumn(ft.Text("Department", weight=ft.FontWeight.BOLD, size=15)),
            ft.DataColumn(ft.Text("Class Description", weight=ft.FontWeight.BOLD, size=15)),
            ft.DataColumn(ft.Text("Actions", weight=ft.FontWeight.BOLD, size=15))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Anthro 100")),
                    ft.DataCell(ft.Text("Anthropology")),
                    ft.DataCell(ft.Text("General Anthropology")),
                    ft.DataCell(btn_enroll)
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Anthro 103")),
                    ft.DataCell(ft.Text("Anthropology")),
                    ft.DataCell(ft.Text("Primatology")),
                    ft.DataCell(btn_enroll)
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Geog 133")),
                    ft.DataCell(ft.Text("Geography")),
                    ft.DataCell(ft.Text("Geography of the Tropics")),
                    ft.DataCell(btn_enroll)
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Geog 171")),
                    ft.DataCell(ft.Text("Geography")),
                    ft.DataCell(ft.Text("Transport Geography")),
                    ft.DataCell(btn_enroll)
                ]
            )
        ]
    )

    ## --> CONTAINER <-- ##

    ## ROW: Name
    row_name = ft.Row(
        controls=[
            lbl_name,
            txt_name
        ]
    )

    ## ROW: Program
    row_program = ft.Row(
        controls=[
            lbl_program,
            drop_program
        ]
    )

    ## COLUMN: Main
    col_main = ft.Column(
        controls=[
            lbl_title,
            ft.Divider(),
            row_name,
            row_program,
            ft.Divider(),
            tbl_sched
        ]
    )
    
    ## CONTAINER: Main
    con_main = ft.Container(
        content=col_main
    )

    ## --> CONSTRUCTING THE PAGE <-- ##

    page.add(con_main)

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")
