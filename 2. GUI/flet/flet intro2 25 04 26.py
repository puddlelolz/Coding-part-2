#import flet as fn #when using flet i need to import it first

#def yes(page: fn.Page): #this is the main function where i will put all my code
    #pass

#fn.app(target=yes) #call the function and run the app
#nothingness is what i got from line 1 until line 6 

import flet as fn #when using flet i need to import it first

def yes(page: fn.Page): #this is the main function where i will put all my code
    page.theme_mode = fn.ThemeMode.DARK #this how you change the theme to dark mode

    page.window_width = 100 #to change the width
    page.window_height = 100 #to change the height

    page.title = "intro ahh" #to change the title of the app

    text = fn.TextField(    #text field is to add a text box
        label="my first flet project, kinda nervous", #appeat on top of the text box
        value = "this app is made using flet",  #the text inside the box before changed to what the user want to type
        border = fn.InputBorder.UNDERLINE #to change the style of the box
        )  
    text2 = fn.Text(
        "text field but no box and cant edit",
        size = 30,
        color = fn.Colors.RED_900,
        bgcolor = fn.Colors.ORANGE_800,
        weight = fn.FontWeight.BOLD
    ) 


    page.add(text2)
    page.add(text) #add the text field to the page
    page.update() #something we need -Mr Gayuh to update ofc
#the window at width and height are not working (dissapointment)

fn.app(target=yes) #call the function and run the app
#nothingness is what i got from line 1 until line 6 