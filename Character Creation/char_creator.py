import flet as ft

## plotting the main function

def main(page: ft.Page):
    page.title = "Character Creation Screen"
    page.width = 500
    page.height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"

    ## Add the field for character name

    char_name = ft.TextField(value="", label="Enter your character's name")

    ## Reset the character stats

    def resetStats() -> None:
        txt_points.value = 10

        char_hp.value = 0
        char_hp.color = ft.Colors.WHITE

        char_str.value = 0
        char_str.color = ft.Colors.WHITE

        char_def.value = 0
        char_def.color = ft.Colors.WHITE

        char_int.value = 0
        char_int.color = ft.Colors.WHITE

        char_agi.value = 0
        char_agi.color = ft.Colors.WHITE

        page.update()

    ## Create the buttons for classes / jobs

    def chooseWarrior(e) -> None:
        tem_warrior = '''You were the only survivor when your village was attacked by demons. You went to the capital and joined the army to get fight the demon army in your journey for justice.'''
        txt_synopsis.value = tem_warrior

        resetStats()

        ## increase char str
        char_str.value = str(int(char_str.value) + 3)
        char_str.color = ft.Colors.AMBER

        page.update()
    btn_job_warrior = ft.Button(content="Warrior", on_click=chooseWarrior)

    def chooseVanguard(e) -> None:
        tem_vanguard = '''After working as a church guard for years, you've received a new task; journey to the Holy City and finish achieve sainthood.'''
        txt_synopsis.value = tem_vanguard

        resetStats()

        ## increase char hp
        char_hp.value = str(int(char_hp.value) + 3)
        char_hp.color = ft.Colors.AMBER

        page.update()
    btn_job_vanguard = ft.Button(content="Vanguard", on_click=chooseVanguard)

    def chooseMage(e) -> None:
        tem_mage = '''You were expelled from the Magic Academy after a false accusation. Now, you're on your way to prove your innocence and exact revenge to the people who wronged you.'''
        txt_synopsis.value = tem_mage

        resetStats()

        ## increase char int
        char_int.value = str(int(char_int.value) + 3)
        char_int.color = ft.Colors.AMBER

        page.update()
    btn_job_mage = ft.Button(content="Mage", on_click=chooseMage)

    def chooseThief(e) -> None:
        tem_thief = '''Due to a fateful encounter with a military officer, you left behind petty theft and now aims to find out the secrets of the government as a spy.'''
        txt_synopsis.value = tem_thief

        resetStats()

        ## increase char int
        char_agi.value = str(int(char_agi.value) + 3)
        char_agi.color = ft.Colors.AMBER

        page.update()
    btn_job_thief = ft.Button(content="Thief", on_click = chooseThief)

    row_job = ft.Row(
        controls=[btn_job_warrior,
                btn_job_vanguard, 
                btn_job_mage,
                btn_job_thief], 
                alignment = ft.MainAxisAlignment.CENTER)

    ## Increasing functions 

    def incHp(e) -> None:
        if int(txt_points.value) > 0:
            char_hp.value = str(int(char_hp.value) + 1)
            txt_points.value = str(int(txt_points.value) - 1)
            page.update()

    def incStr(e) -> None:
        if int(txt_points.value) > 0:
            char_str.value = str(int(char_str.value) + 1)
            txt_points.value = str(int(txt_points.value) - 1)
            page.update()
        

    def incDef(e) -> None:
        if int(txt_points.value) > 0:
            char_def.value = str(int(char_def.value) + 1)
            txt_points.value = str(int(txt_points.value) - 1)
            page.update()
        
    def incInt(e) -> None:
        if int(txt_points.value) > 0:
            char_int.value = str(int(char_int.value) + 1)
            txt_points.value = str(int(txt_points.value) - 1)
            page.update()

    def incAgi(e) -> None:
        if int(txt_points.value) > 0:
            char_agi.value = str(int(char_agi.value) + 1)
            txt_points.value = str(int(txt_points.value) - 1)
            page.update()
    
    ## Decreasing functions

    def decHp(e) -> None:
        if int(char_hp.value) == 0:
            pass
        else:
            char_hp.value = str(int(char_hp.value) - 1)
            txt_points.value = str(int(txt_points.value) + 1)

    def decStr(e) -> None:
        if int(char_str.value) == 0:
            pass
        else:
            char_str.value = str(int(char_str.value) - 1)
            txt_points.value = str(int(txt_points.value) + 1)

    def decDef(e) -> None:
        if int(char_def.value) == 0:
            pass
        else:
            char_def.value = str(int(char_def.value) - 1)
            txt_points.value = str(int(txt_points.value) + 1)

    def decInt(e) -> None:
        if int(char_int.value) == 0:
            pass
        else:
            char_int.value = str(int(char_int.value) - 1)
            txt_points.value = str(int(txt_points.value) + 1)

    def decAgi(e) -> None:
        if int(char_agi.value) == 0:
            pass
        else:
            char_agi.value = str(int(char_agi.value) - 1)
            txt_points.value = str(int(txt_points.value) + 1)

    ## Available points for distribution

    txt_points = ft.Text(value="10", weight = ft.FontWeight.BOLD, size = 15)

    row_points = ft.Row(
        controls = [
            ft.Text(value="Available Points"),
            txt_points
        ], alignment = ft.MainAxisAlignment.CENTER
    )


    ## create the text synopsis

    txt_synopsis = ft.Text(value="You are a new adventurer raring to go. Your potential is only waiting to be realized.")

    col_synopsis = ft.Column(
        controls=[
            ft.Text(value="SYNOPSIS", text_align= ft.TextAlign.CENTER, size=15, weight = ft.FontWeight.BOLD)
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ## Create the fields for the stats

    char_hp = ft.Text(value="0")
    char_str = ft.Text(value="0")
    char_def = ft.Text(value="0")
    char_int = ft.Text(value="0")
    char_agi = ft.Text(value="0")

    ## Creating the buttons for fields

    ### HP
    btn_hp_inc = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, on_click = incHp)
    btn_hp_dec = ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click = decHp)
    row_hp = ft.Row(
        controls=[
            ft.Text(value="HP", text_align=ft.TextAlign.LEFT),
            btn_hp_dec, 
            char_hp,
            btn_hp_inc
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ### STR
    btn_str_inc = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, on_click = incStr)
    btn_str_dec = ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click = decStr)
    row_str = ft.Row(
        controls=[
            ft.Text(value="Strength"),
            btn_str_dec, 
            char_str,
            btn_str_inc
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ### DEF
    btn_def_inc = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, on_click = incDef)
    btn_def_dec = ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click = decDef)
    row_def = ft.Row(
        controls=[
            ft.Text(value="Defense"),
            btn_def_dec, 
            char_def,
            btn_def_inc
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ### INT
    btn_int_inc = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, on_click = incInt)
    btn_int_dec = ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click = decInt)
    row_int = ft.Row(
        controls=[
            ft.Text(value="Intelligence"),
            btn_int_dec, 
            char_int,
            btn_int_inc
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ### AGI
    btn_agi_inc = ft.IconButton(icon=ft.Icons.ARROW_FORWARD_IOS, on_click = incAgi)
    btn_agi_dec = ft.IconButton(icon=ft.Icons.ARROW_BACK_IOS, on_click = decAgi)
    row_agi = ft.Row(
        controls=[
            ft.Text(value="Agility"),
            btn_agi_dec, 
            char_agi,
            btn_agi_inc
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ## Creating the interface for the stats

    col_stats = ft.Column(controls=[
        row_hp,
        row_str,
        row_def,
        row_int,
        row_agi
    ])

    ## building the UI

    my_col = ft.Column(controls=[
            ft.Text(value="Create your character", size=20, weight = ft.FontWeight.BOLD),
                ft.Divider(),
            char_name,
            row_job,
            col_synopsis,
            txt_synopsis,
                ft.Divider(),
            row_points,
            col_stats], 
            alignment = ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER) 


    page.add(
        ft.Container(content=my_col, alignment = ft.Alignment.CENTER)
    )

if __name__ == '__main__':
    ft.run(main)
    print("Program has been successfully initiated.")