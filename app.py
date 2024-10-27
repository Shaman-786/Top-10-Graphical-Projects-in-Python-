# Importing the required modules  
from tkinter import *  # Importing all widgets and modules from Tkinter  
from PIL import Image, ImageTk  # Importing the Image & ImageTk modules from PIL  
import os  # Importing the os module  
import webbrowser  # Importing the webbrowser module  

# ---------------------------- Defining functions ----------------------------  

def display_info(*args):  
    """ This function checks the selected key in 
        the option menu and displays the information 
        about that selected option for the user. 
    """  
    for key in MENU:
        if selected_option.get() == key:  
            displayed_info.set(INFO[list(MENU.keys()).index(key)])  

def execute_command():  
    """ This function uses the os module to execute the 
        system shutdown command with the appropriate argument 
        for the selected option from the menu 
    """  
    for key in MENU:
        if selected_option.get() == key:  
            os.system("shutdown {}".format(MENU[key]))  

def cancel():  
    """ This function closes the application """  
    gui_root.destroy()  

def help():  
    """ This function opens the official website for support """  
    webbrowser.open("https://support.microsoft.com/en-us/windows")  

# ---------------------------- Main function ----------------------------  

if __name__ == "__main__":  
    # Creating the main window  
    gui_root = Tk()  
    gui_root.title("Shut Down Windows - JAVATPOINT")  
    gui_root.geometry("600x325+650+250")  
    gui_root.resizable(0, 0)  
    gui_root.config(bg="#FFFAF0")  

    # Setting the application icon
    try:
        gui_root.iconbitmap("E:/Python/image/windows.ico")
    except Exception as e:
        print(f"Icon file not found: {e}")
  
    # Frames for better organization  
    heading_frame = Frame(gui_root, bg="#FFFAF0")  
    menu_frame = Frame(gui_root, bg="#FFFAF0")  
    buttons_frame = Frame(gui_root, bg="#FFFAF0")  
    heading_frame.pack()  
    menu_frame.pack(expand=True, fill="both")  
    buttons_frame.pack(side=RIGHT)  

    # Importing images  
    image_one = None
    image_two = None
    try:
        image_one = ImageTk.PhotoImage(Image.open("E:/Python/image/download.png").resize((400, 75), Image.LANCZOS))  
    except Exception as e:
        print(f"Image file not found: {e}")

    try:
        image_two = ImageTk.PhotoImage(Image.open("E:/Python/image/images.jpeg").resize((50, 50), Image.LANCZOS))  
    except Exception as e:
        print(f"Image file not found: {e}")

    # Header frame  
    if image_one:  # Only create label if the image is loaded successfully
        image_label_one = Label(heading_frame, image=image_one, bg="#FFFAF0")  
        image_label_one.pack(pady=15)  
    else:
        image_label_one = Label(heading_frame, text="Image not found", bg="#FFFAF0")
        image_label_one.pack(pady=15)

    # Menu frame with options  
    MENU = {  
        'Sign Out': '/l',  
        'Shut down': '/s /t 1',  
        'Restart': '/r /t 1'  
    }  

    INFO = [  
        'Closes all apps and signs you out.',  
        'Closes all apps and turns off the PC.',  
        'Closes all apps, turns off the PC, and then turns it on again.'  
    ]  

    selected_option = StringVar(value='Shut down')  
    displayed_info = StringVar(value=INFO[1])  

    if image_two:  # Only create label if the image is loaded successfully
        image_label_two = Label(menu_frame, image=image_two, bg="#FFFAF0")  
    else:
        image_label_two = Label(menu_frame, text="Image not found", bg="#FFFAF0")
        
    heading_label = Label(menu_frame, text="What do you want the computer to do?", bg="#FFFAF0", fg="#000000")  
    info_label = Label(menu_frame, textvariable=displayed_info, bg="#FFFAF0", fg="#000000")  

    dropdown = OptionMenu(menu_frame, selected_option, *MENU.keys(), command=display_info)  
    dropdown.config(width=45, bg="#F8F8FF")  

    if image_two:  # Add the image label only if the image was successfully loaded
        image_label_two.grid(row=0, column=0, padx=20, pady=10, rowspan=2)
    heading_label.grid(row=0, column=1, padx=10, pady=10, sticky=W)  
    info_label.grid(row=2, column=1, padx=10, pady=10, sticky=W)  
    dropdown.grid(row=1, column=1, padx=10, sticky=W)  

    # Buttons frame  
    ok_button = Button(buttons_frame, text="OK", width=12, relief=GROOVE, bg="#9BFF92", fg="#000000", activebackground="#C0FEBA", command=execute_command)  
    cancel_button = Button(buttons_frame, text="Cancel", width=12, relief=GROOVE, bg="#F29C9D", fg="#000000", activebackground="#FFD7D8", command=cancel)  
    help_button = Button(buttons_frame, text="Help", width=12, relief=GROOVE, bg="#A9EFFF", fg="#000000", activebackground="#D9F8FF", command=help)  

    ok_button.grid(row=0, column=0, padx=2, pady=10)  
    cancel_button.grid(row=0, column=1, padx=2, pady=10)  
    help_button.grid(row=0, column=2, padx=2, pady=10)  

    # Running the application  
    gui_root.mainloop()
