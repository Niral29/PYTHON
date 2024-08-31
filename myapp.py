from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")
    



myapp=Tk()
myapp.title("OS is yours")
myapp.config(bg="yellow")
restart_Button=Button(myapp,text="Restart",command=restart)
restart_Button.place(x=150,y=60,width=150,height=60)

Shutdown_Button=Button(myapp,text="Shut-down",command=shutdown)
Shutdown_Button.place(x=150,y=150,width=150,height=60)


myapp.mainloop()