import flet as fn


def pt(page: fn.Page):
    page.title = "something to do app"
    page.window.width = 1234
    page.window.height = 1000
    page.theme_mode =fn.ThemeMode.DARK
    
fn.app(target=pt)