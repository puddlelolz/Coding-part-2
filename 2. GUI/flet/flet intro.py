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
    page.update() #something we need -Mr Gayuh to update ofc
#the window at widht and height are not working (dissapointment)

fn.app(target=yes) #call the function and run the app
#nothingness is what i got from line 1 until line 6 