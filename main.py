import flet as ft
import component
import controlsNavRail


global myPage

def main(page: ft.Page):

    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # add application's root control to the page
    # create application instance
    app1 = component.Prompt(page)
    # help(app1)
    # add application's root control to the page
    page.add(
        ft.Row(
            [
                controlsNavRail.getNavRail(page, [app1]),
                ft.VerticalDivider(width=1),
                ft.Column([ app1 
                
                ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
        )
    )

    # page.add(app1)

# ft.app(target=main)
ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER, web_renderer="html")