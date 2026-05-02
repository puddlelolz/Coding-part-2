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
    button = fn.ElevatedButton(
        "add to list",
        bgcolor=fn.Colors.ORANGE_800,
        color = fn.Colors.RED_900
    )

    page.add(box, button)
    page.update()
fn.app(target=pt)