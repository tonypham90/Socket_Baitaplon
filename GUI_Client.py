import tkinter
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Client Application")
# minimum size of window
window.minsize(width=700, height=500)
window.maxsize(width=700, height=500)


# Segment with function and command

def getIP():
    # messagebox.showinfo("Due. you get to wrong")
    # lable["text"] = ["already click"]
    # messagebox.showinfo("I got click")
    text = Ip_input.get()
    print('I got click')
    hostLable.configure(text=text)


# -----------------------------

# Head window with connection button, input IP and status
# Connect button

# Header segment
frameMain = ttk.Frame(window)
frameMain.pack(fill="both")
hostLable = Label(frameMain, text="Host's IP: ")
hostLable.configure(text="Host's IP: ")
hostLable.pack(side=tkinter.LEFT, pady=15)

Ip_input = Entry(frameMain, width=10, text="192.168.0.1")
Ip_input.pack(side=tkinter.LEFT, pady=4)

connButton = Button(frameMain, text="Connect")
connButton.pack(side=tkinter.LEFT, pady=10)

status = Label(frameMain, text="Status: Disconnected", font="Arial 12")
status.pack(side="right", pady=2)

# Segment for framework
frameWindow = ttk.Notebook(window)
frameWindow.pack(pady=15)

# create background of frames:
procRun_frame = Frame(frameWindow, height=500, width=700, bg="light grey")
procRun_frame.pack(fill="both", expand=1)

app_Running_frame = Frame(frameWindow, height=500, width=700, bg="light pink")
app_Running_frame.pack(fill="both", expand=1)

Key_note_frame = Frame(frameWindow, height=500, width=700, bg="Purple")
Key_note_frame.pack(fill="both", expand=1)

Print_screen_frame = Frame(frameWindow, height=500, width=700, bg="light green")
Print_screen_frame.pack(fill="both", expand=1)

Regitry_edit_frame = Frame(frameWindow, height=500, width=700, bg="light blue")
Regitry_edit_frame.pack(fill="both", expand=1)

About_frame = Frame(frameWindow, height=500, width=700)
About_frame.pack(fill="both", expand=1)

# add frame to window

frameWindow.add(procRun_frame, text="Process Running")
frameWindow.add(app_Running_frame, text="App Running")
frameWindow.add(Key_note_frame, text="Key Note")
frameWindow.add(Print_screen_frame, text="Print Screen")
frameWindow.add(Regitry_edit_frame, text="Register Editor")
frameWindow.add(About_frame, text="About")

# ----------------------------
head = Label(About_frame, text="Team member:", font='Arial 16 bold').pack()
text_member = """1. Phạm Tuấn Anh - 21880005: GUI Design - Process Running
2. Ngô Hoàng Vân Anh - 21880003: Socket - Keynote
3. Nguyễn Hải Hà - 218800xx: Registry Editor
4. ---- ---- Bảo - 218800xx: Print Screen
5: Nguyễn Thái Nga - 218800xx; App Running"""


mem1 = Label(About_frame, text=text_member,justify = CENTER, font='Arial 12 italic').pack()

# mainloop keep window still running on window
window.mainloop()
