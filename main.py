import tkinter
import customtkinter
import pyautogui
from time import sleep
import easyPWD_Generate as pg
import threading
n=0
"""
print("be ready")
sleep(5)
print("rq")
sleep(2)
"""

def rp(f):

    pyautogui.hotkey('win')
    sleep(0.1)
    if(f):
        pyautogui.typewrite("rewards.bing.com")
        sleep(0.1)
        pyautogui.hotkey('enter')
    else:
        pyautogui.typewrite(pg.generatepwd(len=30))
        sleep(0.1)
        pyautogui.hotkey('enter')
        sleep(2)
        pyautogui.hotkey('Alt', 'F4')
        sleep(0.5)
def program():
    global bl,n
    for i in range(n):
        rp(i==(n-1))
    bl=True
    button.configure(state="normal")
    entry.configure(state="normal")
    button.configure(fg_color="green",hover_color="green",text="start")
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
entry = customtkinter.CTkEntry(app, placeholder_text="number")
bl=True
def button_function():
    global  entry,bl,n
    
    if(entry.get().isdecimal() and bl):
        n=int(entry.get())
    
        button.configure(fg_color="red",hover_color="red",text="runnig")
        entry.configure(state="disable")
        button.configure(state="disable")
        bl=False
        
        
        
        my_thread = threading.Thread(target=program)
        my_thread.start()
        my_thread.join()
    
    else:
        
        print("stop")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="start", command=button_function)
button.configure(fg_color="green",hover_color="green",text="start")
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
app.mainloop()
