import flet as ft
import time
import asyncio

def main(page: ft.Page):

    ## Page details
    page.title = "Running tracker"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.VerticalAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    ## page dimensions
    page.window.width = 300
    page.window.height = 400
    page.window.resizable = False

    ## variables for data
    val_seconds = 0
    val_calorie = 0
    val_km = 0

    switch_running = False

    ### Functions
    async def startRunning(e):
        nonlocal switch_running, val_seconds

        if switch_running == False:
            switch_running = True
            print("You have started running.")
            page.show_dialog(ban_running)
            while switch_running == True:
                await asyncio.sleep(1)
                val_seconds += 1
                print(f'You have been running for {val_seconds} seconds.')
                lbl_time.value = val_seconds
                page.update()
        else:
            page.pop_dialog()
            switch_running = False
            print("You have stopped running.")
            print(f'You have ran for {val_seconds} seconds!')
            pass

    ## Banner for running
    ban_running = ft.Banner(
        leading = ft.Icon(ft.Icons.INFO_OUTLINE),
        content = ft.Text("You have started running!"),
        actions = [ft.Button(content="Dismiss")],
        open = True
    )

    ## Running Tracker
    lbl_time = ft.Text(value = val_seconds, size=50, weight = ft.FontWeight.BOLD, text_align = ft.TextAlign.CENTER, color = ft.Colors.BLACK)
    sublbl_time = ft.Text(value = "seconds", size = 20, color = ft.Colors.BLACK)

    ## sub-label
    lbl_km = ft.Text(value = val_km, size = 20, color = ft.Colors.BLACK)
    sublbl_km = ft.Text(value = "km", size = 15, weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK)

    lbl_cal = ft.Text(value = val_calorie, size = 20, color = ft.Colors.BLACK)
    sublbl_cal = ft.Text(value = "kcal", size = 15, weight = ft.FontWeight.BOLD, color = ft.Colors.BLACK)

    ## title
    lbl_title = ft.Text(value="Running Tracker", size = 30, text_align = ft.TextAlign.CENTER)

    ## building the components 

    col_time = ft.Column(controls=[
        lbl_time,
        sublbl_time
    ], horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment = ft.MainAxisAlignment.CENTER)

    row_time = ft.Container(ft.Row(controls=[
        col_time
    ], alignment = ft.MainAxisAlignment.CENTER), bgcolor = ft.Colors.GREEN_200, padding = 10, margin = 0)

    row_km = ft.Container(content = ft.Row(controls=[
        lbl_km,
        sublbl_km
    ], alignment = ft.MainAxisAlignment.CENTER), bgcolor = ft.Colors.BLUE_100, padding = 10, margin = 0)

    row_cal = ft.Container(content = ft.Row(controls=[
        lbl_cal,
        sublbl_cal
    ], alignment = ft.MainAxisAlignment.CENTER), bgcolor = ft.Colors.BLUE_100, padding = 10, margin = 0)

    row_title = ft.Container(content = ft.Row(controls=[
        lbl_title
    ], alignment = ft.MainAxisAlignment.CENTER))

    row_subdata = ft.Row(controls=[
        row_km,
        row_cal
    ], alignment = ft.MainAxisAlignment.CENTER, spacing = 0)

    ## Buttons 

    btn_start = ft.Button(content="Start/Stop", 
                          color = ft.Colors.BLACK, 
                          bgcolor = ft.Colors.GREEN_200, 
                          style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius = 5)),
                          on_click = startRunning)
    btn_stop = ft.Button(content="Stop", 
                         color = ft.Colors.BLACK, 
                         bgcolor = ft.Colors.GREY, 
                         style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius = 5)))

    row_buttons = ft.Row(controls=[
        btn_start,
        btn_stop
    ], alignment = ft.MainAxisAlignment.CENTER)



    ## building the main column

    col_main = ft.Column(controls=[
        row_title,
        row_time,
        row_subdata,
        row_buttons
    ])

    ## building the container

    page.add(ft.Container(
        content = col_main
    ))


if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")