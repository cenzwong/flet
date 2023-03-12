import flet as ft
import ai21_func

class Prompt(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.update()

    def build(self):
        self.new_task = ft.TextField(label="input", hint_text="Words to be rewritten...", expand=True)
        self.new_button = ft.FloatingActionButton(icon=ft.icons.SEND, on_click=self.send_clicked)
        self.new_dropdown = ft.Dropdown(
                                    width=100,
                                    options=[
                                        ft.dropdown.Option("general"),
                                        ft.dropdown.Option("formal"),
                                        ft.dropdown.Option("casual"),
                                        ft.dropdown.Option("long"),
                                        ft.dropdown.Option("short"),
                                    ],
                                )
        self.container_text = ft.Container()
        self.response = ft.Column()
        

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        self.new_dropdown,
                        self.new_button,
                    ],
                ),
                self.container_text,
            ],
        )

    def send_clicked(self, e):
        
        def button_clicked(e):
            # print(help(e.control))
            self.page.set_clipboard(e.control.text)
        
        print(self.new_task.value, self.new_dropdown.value)
        ai21_response = ai21_func.ai21_rewrite(self.new_task.value, self.new_dropdown.value)
        for suggestions in ai21_response:
            mypredict_text = ft.ListTile(
                    leading=ft.IconButton(icon = ft.icons.ALBUM, on_click=button_clicked, data=0),
                    title=ft.FilledTonalButton(text=suggestions["text"], on_click=button_clicked),
                    # trailing=ft.PopupMenuButton(
                    #     icon=ft.icons.MORE_VERT,
                    #     items=[
                    #         ft.PopupMenuItem(text="Item 1"),
                    #         ft.PopupMenuItem(text="Item 2"),
                    #     ],
                    # ),
                )
            self.response.controls.append(mypredict_text)
        self.container_text.content = self.response

        self.new_task.value = ""
        self.update()


# import flet as ft
# import ai21_func

# class Prompt(ft.UserControl):
#     def build(self):
#         self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
#         self.new_button = ft.FloatingActionButton(icon=ft.icons.SEND, on_click=self.send_clicked)
#         self.response = ft.Column()

#         # application's root control (i.e. "view") containing all other controls
#         return ft.Column(
#             width=600,
#             controls=[
#                 ft.Row(
#                     controls=[
#                         self.new_task,
#                         self.new_button,
#                     ],
#                 ),
#                 self.response,
#             ],
#         )

#     def send_clicked(self, e):
#         ai21_response = ai21_func.ai21_rewrite(self.new_task.value, "formal")
#         for suggestions in ai21_response:
#             self.response.controls.append(ft.Checkbox(label=suggestions["text"]))

#         self.new_task.value = ""
#         self.update()