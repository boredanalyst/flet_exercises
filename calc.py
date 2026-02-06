## This imports the library

import flet as ft

## sets up some classes

@ft.control
class NumberButton(ft.Button):
    bgcolor: ft.Colors = ft.Colors.WHITE
    color: ft.Colors = ft.Colors.BLACK_87

@ft.control
class OpsButton(ft.Button):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class CtrlButton(ft.Button):
    bgcolor: ft.Colors = ft.Colors.BLUE
    color: ft.Colors = ft.Colors.WHITE

## sets up the Calculator App class thru the ft.Container class

@ft.control
class Calculator(ft.Container):
    def init(self):

        self.firstval = None
        self.secondval = None
        self.operation = None
        self.result = ft.Text(value="0", color = ft.Colors.WHITE, size=15)
        result_txt  = ft.Text(value="0", color = ft.Colors.WHITE, size=15)

        self.operator = ""
        self.width=350
        self.bgcolor=ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(20)
        self.padding=20
        self.content= ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Text(value="CALCULATOR", color = ft.Colors.WHITE)
                    ]),

                    ft.Row(controls=[self.result]),

                    ft.Row(controls=[
                        NumberButton("1", on_click=self.numbtn_click),
                        NumberButton("2", on_click=self.numbtn_click),
                        NumberButton("3", on_click=self.numbtn_click),
                        OpsButton("+", on_click=self.opbtn_click)
                    ]),

                    ft.Row(controls=[
                        NumberButton("4", on_click=self.numbtn_click),
                        NumberButton("5", on_click=self.numbtn_click),
                        NumberButton("6", on_click=self.numbtn_click),
                        OpsButton("-", on_click=self.opbtn_click)
                    ]),
                    
                    ft.Row(controls=[
                        NumberButton("7", on_click=self.numbtn_click),
                        NumberButton("8", on_click=self.numbtn_click),
                        NumberButton("9", on_click=self.numbtn_click),
                        OpsButton("x", on_click=self.opbtn_click)
                    ]),

                    ft.Row(controls=[
                        CtrlButton("C"),
                        NumberButton("0"),
                        CtrlButton("=", on_click=self.equbtn_click),
                        OpsButton("/", on_click=self.opbtn_click)
                    ]
                    )
                ]
            )
        
    def numbtn_click(self, e):
        data = e.control.content
        if self.firstval == None:
            self.firstval = int(data)
            print(self.firstval)
        else:
            self.secondval = int(data)
            print(self.secondval)

    def opbtn_click(self, e):
        data = e.control.content
        match data:
            case "+":
                self.operation = "add"
            case "-":
                self.operation = "subtract"
            case "x":
                self.operation = "multiply"
            case "/":
                self.operation = "divide"
        print(f'{self.operation}')

    def equbtn_click(self, e):
        ## check first if the operations button is available.
        if self.operation == None:
            print("No operation selected")
        else:
            ops = self.operation
            match ops:
                case "add":
                    self.result.value = self.firstval + self.secondval
                    print(self.firstval + self.secondval)
                    self.firstval = self.result
                    self.secondval = None
                case "subtract":
                    self.result.value = self.firstval - self.secondval
                    print(self.firstval - self.secondval)
                    self.firstval = self.result
                    self.secondval = None
                case "multiply":
                    self.result.value = self.firstval * self.secondval
                    print(self.firstval * self.secondval)
                    self.firstval = self.result
                    self.secondval = None
                case "divide":
                    self.result.value = self.firstval / self.secondval
                    print(self.firstval / self.secondval)
                    self.firstval = self.result
                    self.secondval = None
        
        self.update()

## sets up the UI

def main(page: ft.Page):
    ## setting up the page
    page.window.width = 330
    page.window.height =350
    page.title = "My first flet app"
    calc = Calculator()

    page.add(calc)




ft.run(main)