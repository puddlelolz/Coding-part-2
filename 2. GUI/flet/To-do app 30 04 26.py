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

    all_tasks = fn.Column()
    complete_tasks = fn.Column()
    incomplete_tasks = fn.Column()

    def update_task_visibility(task: fn.Checkbox):
        if task.value:
            if task in incomplete_tasks.controls:
                incomplete_tasks.controls.remove(task)
            if task not in complete_tasks.controls:
                complete_tasks.controls.append(task)
        else:
            if task in complete_tasks.controls:
                complete_tasks.controls.remove(task)
            if task not in incomplete_tasks.controls:
                incomplete_tasks.controls.append(task)

    def on_task_change(e):
        update_task_visibility(e.control)
        page.update()

    def add_task(e):
        task = fn.Checkbox(label=box.value, value=False, on_change=on_task_change)
        all_tasks.controls.append(task)
        incomplete_tasks.controls.append(task)
        box.value = ""
        page.update()

    button = fn.ElevatedButton(
        "add to list",
        on_click=add_task
    )

    three_tabs = [
        fn.Tab("All"),
        fn.Tab("Complete"),
        fn.Tab("Incomplete")
    ]

    T = fn.Tabs(
        selected_index=0,
        length=3,
        expand=True,
        content=fn.Column(
            expand=True,
            controls=[
                fn.TabBar(tabs=three_tabs),
                fn.TabBarView(
                    expand=True,
                    controls=[
                        fn.Column(expand=True, controls=[all_tasks]),
                        fn.Column(expand=True, controls=[complete_tasks]),
                        fn.Column(expand=True, controls=[incomplete_tasks]),
                    ],
                ),
            ],
        ),
    )

    text = fn.Text(
        "made by puddle",
        size=10,
        color=fn.Colors.ORANGE_900,
        weight=fn.FontWeight.BOLD
    )

    page.add(box, button, text, T)
    page.update()
fn.app(target=pt)