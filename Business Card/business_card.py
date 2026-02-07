import flet as ft

## MAIN FUNCTION
def main(page: ft.Page) -> None:

    #### Page Details
    page.title = "Erica Flores"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 600
    page.window.resizable = False


    #### Actual Content 

    ### Personal Details
    lbl_name = ft.Text(value = "Erica Flores", size = 30, weight = ft.FontWeight.BOLD)
    lbl_headline = ft.Text(value = "Graphic Designer / Video Editor / Social Media Strategist", size = 18)

    lbl_address = ft.Text(value = "Manila, Philippines", size = 15)
    lbl_bday = ft.Text(value = "26 years old", size = 15)
    lbl_title_summary = ft.Text(value = "SUMMARY", size = 15, weight = ft.FontWeight.BOLD)

    lbl_summary = ft.Text(value = "I am a content creator with 3+ years of experience in visual communication and social media management. I am skilled in Adobe Suite and Google Analytics.")
    
    ### Services

    ## Graphic Design Card
    crd_graphic = ft.Card(content = ft.Container(
        padding = 10,
        width = 250,
        alignment = ft.Alignment.CENTER,
        content = ft.Column(controls=[
            ft.Text("Graphic Design", size = 15, weight = ft.FontWeight.BOLD),
            ft.Text("I create visual content using Adobe", size = 10)
        ])
    ), bgcolor = ft.Colors.GREY_400)


    ## Video Editing Card
    crd_video = ft.Card(content = ft.Container(
        padding = 10,
        width = 250,
        alignment = ft.Alignment.CENTER,
        content = ft.Column(controls=[
            ft.Text("Video Editing", size = 15, weight = ft.FontWeight.BOLD),
            ft.Text("I edit video content", size = 10)
        ])
    ), bgcolor = ft.Colors.GREY_400)

    ## Content Writing Card
    crd_write = ft.Card(content = ft.Container(
        padding = 10,
        width = 250,
        alignment = ft.Alignment.CENTER,
        content = ft.Column(controls=[
            ft.Text("Content Writing", size = 15, weight = ft.FontWeight.BOLD),
            ft.Text("I write creative and technical works", size = 10)
        ])
    ), bgcolor = ft.Colors.GREY_400)

    ## Social Media Management Card
    crd_socmed = ft.Card(content = ft.Container(
        padding = 10,
        width = 250,
        alignment = ft.Alignment.CENTER,
        content = ft.Column(controls=[
            ft.Text("Social Media", size = 15, weight = ft.FontWeight.BOLD),
            ft.Text("I manage accounts and inboxes", size = 10)
        ])
    ), bgcolor = ft.Colors.GREY_400)

    ### Achievements

    ## Card for Designs
    crd_design  = ft.Card(
        content = ft.Container(
            width = 250,
            padding = 15,
            content = ft.Column(
            controls = [
                ft.Text("10 percent average increase in account followers.")
            ]
        )
    )
    )

    ## Card for Followers
    crd_increase = ft.Card(
        content = ft.Container(
            width = 250,
            padding = 15,
            content = ft.Column(
            controls = [
                ft.Text("10 percent average increase in account followers.")
            ]
        )
    )
    )


    #### Wrappers

    ### Wrappers for introduction

    ## Basic Info Row
    row_basic_info = ft.Row(controls=[
        lbl_address,
        lbl_bday
    ], alignment = ft.MainAxisAlignment.CENTER)

    ## Row Summary Title
    row_summary_title = ft.Row(controls=[
        lbl_title_summary,
    ]) ## This is just to set the title flushed to the LEFT

    ## Row for Summary
    row_summary = ft.Row(controls=[
        lbl_summary
    ], wrap=True) ## This is just to set the title flushed to the LEFT

    ## Intro Column
    col_intro = ft.Column(controls=[
        lbl_name,
        lbl_headline,
        ft.Divider(),
        row_basic_info,
        row_summary_title,
        row_summary,
        ft.Divider()
    ], alignment = ft.MainAxisAlignment.CENTER,
    horizontal_alignment= ft.CrossAxisAlignment.CENTER)


    ### Wrappers for Services

    ## First Card Set
    row_service_cardset_a = ft.Row(controls = [
        crd_graphic,
        crd_video
    ], wrap = True, expand = True)

    ## Second Card Set
    row_service_cardset_b = ft.Row(controls = [
        crd_write,
        crd_socmed
    ], wrap = True, expand = True)

    ### Wrappers for Achievements

    row_achievement = ft.Row(
        controls = [
            crd_design,
            crd_increase
        ], alignment = ft.MainAxisAlignment.CENTER
    )

    ### Main Wrappers

    ## Main Column
    col_main = ft.Column(controls = [
        col_intro,
        row_service_cardset_a,
        row_service_cardset_b,
        ft.Divider(),
        row_achievement
    ])

    ## Actual Container
    con_main = ft.Container(content=col_main,
                            alignment=ft.Alignment.CENTER)


    #### Adding everything to the page
    page.add(con_main)

if __name__ == '__main__':
    ft.run(main)
    print("Program initiated successfully.")