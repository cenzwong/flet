import flet as ft

def getNavRail(page, listOfInterface):

    def switch_app(e):
        # print("Selected destination:", e.control.selected_index)
        # print()
        if e.control.selected_index == 0:
            listOfInterface[0].controls[0].visible = True
            print("app1")
        elif e.control.selected_index == 1:
            listOfInterface[0].controls[0].visible = False
            print("app2")
        elif e.control.selected_index == 2:
            print("app3")
        listOfInterface[0].update()
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        # leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=switch_app,
    )
    
    return rail