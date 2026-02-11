import flet as ft
from datetime import datetime as dt
import pandas as pd



## Function loaded upon opening the app
def displayClock(page: ft.Page, e) -> None:
    e.value = dt.today().strftime("%H:%M:%S") ## Display the time upon loading
    page.update()
    
## Main function for building the page
def main(page:ft.Page) -> None:
    ## --> PAGE DETAILS <-- ##
    page.window.width = 700
    page.window.height = 800
    page.padding=100
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Clock In System"



    ## --> FUNCTIONS <-- ##

    ## Validate the existence of the account
    def validateEmployee(e) -> None:
        ## Check if the text fields have values

        if txt_emp_id.value == "":
            page.show_dialog(alt_missing_cred)
            return
        elif txt_emp_pin.value == "":
            page.show_dialog(alt_missing_cred)
            return
        
        ## Loading the employee data from the csv file
        df = pd.read_csv(r'C:\Users\Louis Garcia\OneDrive\Desktop\Projects\Flet Tutorial\ClockIn\data\employees.csv')
        
        ## filter the dataframe
        df = df[df["employee_id"] == txt_emp_id.value]
        
        if len(df) == 1: ## check if there is EXACTLY one account in the database
            print("Account found")
            correct_password = df["employee_pin"][0]
            print(correct_password)
            if str(txt_emp_pin.value) == str(correct_password): ## checking the if the inputted PIN is correct
                page.show_dialog(alt_correct_cred)

                ## Appending the clockin/clockout buttons, and table
                col_main.controls.append(col_append)
                txt_emp_id.disabled = True
                txt_emp_pin.disabled = True
            else:
                page.show_dialog(alt_invalid_cred)
        elif len(df) > 1:
            print("Multiple accounts found.")
            print("Please contact administrator.")
        else:
            page.show_dialog(alt_invalid_cred)
        
    def clockIn(e) -> None:
        record_type = "CLOCK IN"
        emp_id = txt_emp_id.value
        timestamp = dt.now().strftime("%H:%M:%S")

        cell_type = ft.DataCell(ft.Text(record_type))
        cell_emp_id = ft.DataCell(ft.Text(emp_id))
        cell_timestamp = ft.DataCell(ft.Text(timestamp))

        tbl_timein.rows.append(
            ft.DataRow(
                cells=[
                    cell_type,
                    cell_emp_id,
                    cell_timestamp
                ]
            )
        )

        page.show_dialog(alt_record_success)

    def clockOut(e) -> None:
        record_type = "CLOCK OUT"
        emp_id = txt_emp_id.value
        timestamp = dt.now().strftime("%H:%M:%S")

        cell_type = ft.DataCell(ft.Text(record_type))
        cell_emp_id = ft.DataCell(ft.Text(emp_id))
        cell_timestamp = ft.DataCell(ft.Text(timestamp))

        tbl_timein.rows.append(
            ft.DataRow(
                cells=[
                    cell_type,
                    cell_emp_id,
                    cell_timestamp
                ]
            )
        )

        page.show_dialog(alt_record_success)



    ## --> CONTENT <-- ##
    
    ## LABEL: Clock
    lbl_clock = ft.Text(
        value="0:00",
        weight=ft.FontWeight.BOLD,
        size=40
    )

    ## --------------------------

    ## LABEL: Employee ID
    lbl_emp_id = ft.Text(
        value="Employee ID",
        weight=ft.FontWeight.BOLD
    )

    ## TEXTFIELD: Employee ID
    txt_emp_id = ft.TextField(
        value="",
        hint_text="Provide your Employee ID",
        expand=True
    )

    ## LABEL: Employee PIN
    lbl_emp_pin = ft.Text(
        value="Employee PIN",
        weight=ft.FontWeight.BOLD
    )

    ## TEXTFIELD: Employee PIN
    txt_emp_pin = ft.TextField(
        value="",
        hint_text="Provide your Employee PIN",
        expand=True,
        password=True,
        can_reveal_password=True
    )

    ## --------------------------

    ## BUTTON: Log In
    btn_login  = ft.Button(
        content="Log In",
        icon=ft.Icons.LOGIN,
        expand=True,
        on_click=validateEmployee
    )

    ## --------------------------

    ## BUTTON: CLOCK IN
    btn_clock_in = ft.Button(
        content="Clock In",
        icon=ft.Icons.PUNCH_CLOCK,
        on_click=clockIn
    )

    ## BUTTON: CLOCK OUT
    btn_clock_out = ft.Button(
        content="Clock Out",
        icon=ft.Icons.PUNCH_CLOCK,
        on_click=clockOut
    )

    ## --------------------------

    ## TABLE: CLOCK IN / OUT RECORDS
    tbl_timein = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("TYPE",weight=ft.FontWeight.BOLD)),
            ft.DataColumn(label=ft.Text("TIMESTAMP", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(label=ft.Text("EMPLOYEE ID", weight=ft.FontWeight.BOLD))
        ], 
        rows=[],
        expand=True
    )

    ## --------------------------

    ## ALERT: Success

    alt_record_success = ft.AlertDialog(
        title=ft.Text("Success!"),
        content=ft.Text("Record successfully captured."),
        icon=ft.Icons.CHECK
    )

    ## ALERT: Missing Credentials

    alt_missing_cred = ft.AlertDialog(
        title=ft.Text("Error"),
        content=ft.Text("Missing Employee ID / PIN"),
        icon=ft.Icons.WARNING
    )

    ## ALERT: Invalid Credentials

    alt_invalid_cred = ft.AlertDialog(
        title=ft.Text("Error"),
        content=ft.Text("Invalid Employee ID / PIN"),
        icon=ft.Icons.WARNING
    )

    ## ALERT: Correct Credentials

    alt_correct_cred = ft.AlertDialog(
        title=ft.Text("Success"),
        content=ft.Text("Account Found!"),
        icon=ft.Icons.CHECK
    )

    ## --> WRAPPERS <-- ##

    ## COLUMN: Clock Display
    col_clock = ft.Column(
        controls=[
            lbl_clock
        ], alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    ## COLUMN: Employee Info
    col_emp_info = ft.Column(
        controls=[
            lbl_emp_id,
            txt_emp_id,
            lbl_emp_pin,
            txt_emp_pin
        ]
    )
    
    ## ROW: Login Button
    row_login = ft.Row(
        controls=[
            btn_login
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    ## ROW: CLOCK IN / OUT
    row_clock_in_out = ft.Row(
        controls=[
            btn_clock_in,
            btn_clock_out
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    ## ROW: Clock Records Table
    row_records = ft.Row(
        controls=[
            tbl_timein
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ## COLUMN: Appended Column
    col_append = ft.Column(
        controls=[
            row_clock_in_out,
            row_records
        ]
    )

    ## COLUMN: Main
    col_main = ft.Column(
        controls=[
            col_clock,
            ft.Divider(),
            col_emp_info,
            row_login,
            ft.Divider()
        ], spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    ## CONTAINER: Main
    con_main = ft.Container(
        content=col_main, 
        alignment = ft.Alignment.CENTER
    )


    ## --> CONSTRUCTING THE PAGE <-- ##
    page.add(con_main)
    displayClock(page, e=lbl_clock)

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")