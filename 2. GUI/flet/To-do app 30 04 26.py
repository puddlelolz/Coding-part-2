import flet as fn


def pt(page: fn.Page):
    page.title = "something to do app"
    page.window.width = 1234
    page.window.height = 1000
    page.theme_mode =fn.ThemeMode.DARK


    box = fn.TextField(
        label="what do you plan to do today?",
        value="input what to do here",
        border=fn.InputBorder.OUTLINE#hellooooo
    )
    def add_task(e):
        task = fn.Checkbox(label= box.value, value=False)
        task_list.controls.append(task)
        box.value = ""
        page.update()

    button = fn.ElevatedButton(
        "add to list",
        bgcolor=fn.Colors.ORANGE_800,
        color = fn.Colors.RED_900,
        on_click= add_task
    )

    task_list = fn.Column()

    tabs = fn.Tabs(
        selected_index=0,
        tabs=[
            fn.Tab(text="All"),
            fn.Tab(text="Complete"),
            fn.Tab(text="Incomplete"),
        ],
    )

    page.add(box, button, tabs, task_list )
    page.update()
fn.app(target=pt)