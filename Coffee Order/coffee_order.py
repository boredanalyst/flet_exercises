import flet as ft
from datetime import date as dt


## Main Function

def main(page: ft.Page):
    ## Page Details
    page.title = "Coffee Order"
    page.window.height = 550
    page.window.width = 550
    page.theme_mode = ft.ThemeMode.LIGHT


    ## >> FUNCTIONS << ##

    ## --> Validate the quantity text field value
    def validateQuantity(e) -> None:
        if str.isdecimal(txt_qnt.value):
            txt_qnt.error = None
            page.update()
        else: 
            txt_qnt.error = "Please provide a valid quantity."
            page.update()

    ## --> Compile the order
    def compileOrder(e) -> str:
        dict_order = {
            "coffee_type" : [],
            "coffee_size" : [],
            "coffee_temp" : [],
            "quantity" : None
                      }
        
        ## Get the quantity 
        ## Putting this at the top to make sure it won't waste time with more checks than necessary.
        if txt_qnt.value == False or txt_qnt.value == "": 
            txt_qnt.error = "You cannot leave this field empty."
            page.update()
            return
        else:
            dict_order["quantity"] = txt_qnt.value

        ## Get the coffee type
        if chk_americano.value == True:
            dict_order["coffee_type"].append(chk_americano.label)
        
        if chk_capuccino.value == True:
            dict_order["coffee_type"].append(chk_capuccino.label)
        
        if chk_mocha.value == True:
            dict_order["coffee_type"].append(chk_mocha.label)

        ## Get the coffee style
        if chk_small.value == True:
            dict_order["coffee_size"].append(chk_small.label)
        
        if chk_medium.value == True:
            dict_order["coffee_size"].append(chk_medium.label)
        
        if chk_large.value == True:
            dict_order["coffee_size"].append(chk_large.label)

        ## Get the coffee temperature
        if chk_hot.value == True:
            dict_order["coffee_temp"].append(chk_hot.label)
        
        if chk_cold.value == True:
            dict_order["coffee_temp"].append(chk_cold.label)

        ## Write the order into a text file

        with open('Coffee Order\\order.txt', 'w') as order:
            order.write('--- ORDER ---\n')
            order.write(f'ORDER RECEIVED: {dt.today()}\n')
            order.write(f'COFFEE TYPE: {dict_order["coffee_type"]}\n')
            order.write(f'COFFEE SIZE: {dict_order["coffee_size"]}\n')
            order.write(f'COFFEE TEMPERATURE: {dict_order["coffee_temp"]}\n')
            order.write(f'QUANTITY: {dict_order["quantity"]}\n')

        page.show_dialog(alt_submit)

        for checkbox in frm_checkboxes:
            checkbox.value = False
            page.update()
        
        for textfield in frm_textfield:
            textfield.value = ""
            page.update()

        print("Order recorded successfully.")

    ## >> CONTENT << ##
    
    ## --> Title
    lbl_title = ft.Text(
        value="CoffeeMax",
        size=30,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD)
    
    ## --> Question 1
    lbl_q1 = ft.Text(
        value="What is your order?",
        size=15
    )

    ## --> Americano Checkbox
    chk_americano = ft.Checkbox(
        label="Americano"
    )

    ## --> Capuccino Checkbox
    chk_capuccino = ft.Checkbox(
        label="Capuccino"
    )

    ## --> Mocha Checkbox
    chk_mocha = ft.Checkbox(
        label="Mocha"
    )

    ## --> Question 2
    lbl_q2 = ft.Text(
        value="What is the size of your order?",
        size=15
    )

    ## --> Small Checkbox
    chk_small = ft.Checkbox(
        label="Small"
    )

    ## --> Medium Checkbox
    chk_medium = ft.Checkbox(
        label="Medium"
    )

    ## --> Large Checkbox
    chk_large = ft.Checkbox(
        label="Large"
    )

    ## --> Question 3
    lbl_q3 = ft.Text(
        value="Do you prefer hot or cold coffee?",
        size=15
    )

    ## --> Hot Checkbox
    chk_hot = ft.Checkbox(
        label="Hot",
        shape=ft.BeveledRectangleBorder(radius=10),
        border_side=ft.BorderSide(width=1,color=ft.Colors.BLACK)
    )

    chk_cold = ft.Checkbox(
        label="Cold",
        shape=ft.BeveledRectangleBorder(radius=10),
        border_side=ft.BorderSide(width=1,color=ft.Colors.BLACK)
    )

    ## --> Question 4
    lbl_q4 = ft.Text(
        value="How many do you need?",
        size=15
    )

    ## --> Quantity Text Field
    txt_qnt = ft.TextField(
        label="Quantity",
        border=ft.InputBorder.UNDERLINE,
        on_change=validateQuantity
    )

    ## --> Submit Button
    btn_submit = ft.Button(
        content="Submit Order",
        icon=ft.Icons.SEND,
        on_click=compileOrder
    )

    ## >> WRAPPERS << ##

    ## --> Coffee Choices Row
    row_coffee_type = ft.Row(
        controls=[
            chk_americano,
            chk_capuccino,
            chk_mocha
        ]
    )

    ## --> Size Choices Row
    row_size = ft.Row(
        controls=[
            chk_small,
            chk_medium,
            chk_large
        ]
    )

    ## -->> Temperature Row 
    row_temp = ft.Row(
        controls=[
            chk_hot,
            chk_cold
        ]
    )

    ## -->> Quantity Row
    row_qnt = ft.Row(
        controls=[
            txt_qnt
        ]
    )

    ## -->> Submit Row
    row_submit = ft.Row(
        controls=[
            btn_submit
        ], 
        alignment = ft.CrossAxisAlignment.END
    )

    ## --> Main Column
    col_main = ft.Column(
        controls=[
            lbl_title,
            ft.Divider(),
            lbl_q1,
            row_coffee_type,
            lbl_q2,
            row_size,
            lbl_q3,
            row_temp,
            lbl_q4,
            row_qnt,
            ft.Divider(),
            row_submit
        ]
    )

    ## --> Main Container
    con_main = ft.Container(
        content=col_main
    )

    ## >> DIALOGS << ##

    alt_submit = ft.AlertDialog(
        title=ft.Text("Done!", size = 15),
        content=ft.Text("Order has been submitted successfully."),
        alignment = ft.Alignment.CENTER,
        open=False
    )

    ## >> CONSTRUCTING THE PAGE << ##
    frm_checkboxes = [chk_americano, 
                      chk_capuccino, 
                      chk_mocha, 
                      chk_cold, 
                      chk_hot, 
                      chk_small, 
                      chk_medium,
                      chk_large]
    frm_textfield = [
        txt_qnt
    ]
    page.add(con_main)




if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully")