from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
from base64 import b64encode, b64decode
import os

fileName = "Startup"

# File Functions
def nFile():
    global fileName
    if fileName == "":
        pass
    else:
        msg_save = messagebox.askquestion(
            "Save Document?",
            "Would you like to Save the current document?",
            icon="warning",
        )

        if msg_save == "yes":
            sFileAs()
            clear()
            Text.insert(1.0, "")
        else:
            fileName = ""
            clear()
            Text.insert(1.0, "")


def oFile():
    global fileName

    if fileName != "":
        clear()
    elif fileName != "Startup":
        clear()
    else:
        sFileAs()

    f = filedialog.askopenfile(mode="r")
    fileName = f.name
    fn = open(f.name, "r").read()
    text.insert(1.0, fn)
    f.close()


def sFile():
    global fileName

    if fileName == "":
        sFileAs()
    elif fileName == "Startup":
        sFileAs()
    else:
        f = open(fileName, "w")
        txtSav = str(text.get(1.0, END))
        f.write(txtSav)
        f.close()


def sFileAs():
    global fileName
    f = filedialog.asksaveasfile(mode="w", defaultextension="")

    if f is None:
        return

    fileName = f.name
    txtSav = str(text.get(1.0, END))
    f.write(txtSav)
    f.close()


def quit():
    exit()


# Encode and Decode Functions
def encode():
    enc = text.get(1.0, "end-1c")
    try:
        ans = b64encode(enc.encode())
        text.delete(1.0, "end")
        text.insert(1.0, str(ans)[2:-1])
        return
    except Exception as x:
        messagebox.showerror(title="ERROR!", message=x)


def decode():
    dec = text.get(1.0, "end")
    try:
        ans = b64decode(dec.encode()).decode("utf-8")
        text.delete(1.0, "end")
        text.insert(1.0, ans)
        return
    except Exception as x:
        messagebox.showerror(title="ERROR!", message=x)


# Textbox context commands
def clear():
    text.delete(1.0, "end")


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate("<<Copy>>")


def paste():
    text.event_generate("<<Paste>>")


def find():
    pass


# Setting up Main Form
root = Tk()

if "nt" == os.name:
    root.iconbitmap("encrypt.ico")
else:
    pass

root.title("Base64 Encode/Decode")
root.resizable(TRUE, TRUE)

# Working on implementing Filebar
m = Menu(root)
root["menu"] = m

f_edit = Menu(m, tearoff=0)
m.add_cascade(menu=f_edit, label="File", underline=0)
f_edit.add_command(label="New", underline=0, command=nFile)
f_edit.add_command(label="Open", underline=0, command=oFile)
f_edit.add_command(label="Save", underline=0, command=sFile)
f_edit.add_command(label="Save As", command=sFileAs)
f_edit.add_separator()
f_edit.add_command(label="Exit", underline=1, command=quit)

m_edit = Menu(m, tearoff=0)
m.add_cascade(menu=m_edit, label="Edit", underline=0)
m_edit.add_command(
    label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>")
)
m_edit.add_command(
    label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>")
)
m_edit.add_command(
    label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>")
)
m_edit.add_separator()
m_edit.add_command(label="Find", underline=0, command=find)
m_edit.add_separator()
m_edit.add_command(label="Clear", underline=0, command=nFile)

e_edit = Menu(m, tearoff=0)
m.add_cascade(menu=e_edit, label="Code", underline=0)
e_edit.add_command(label="Encode", underline=0, command=encode)
e_edit.add_command(label="Decode", underline=0, command=decode)

# Setting up Frames
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Setting up Context Menu
menu = Menu(root, tearoff=0)
menu.add_command(label="Cut", command=cut)
menu.add_command(label="Copy", command=copy)
menu.add_command(label="Paste", command=paste)
menu.add_separator()
menu.add_command(label="Encode", command=encode)
menu.add_command(label="Decode", command=decode)
menu.add_separator()
menu.add_command(label="Clear", command=nFile)

# Check for right click on PC/Linux or Option/Click on macOS
if root.tk.call("tk", "windowingsystem") == "aqua":
    root.bind("<2>", lambda e: menu.post(e.x_root, e.y_root))
    root.bind("<Control-1>", lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind("<3>", lambda e: menu.post(e.x_root, e.y_root))

# Setup Textbox and Buttons
text = Text(mainframe, width=100, height=20, wrap="none")
ys = ttk.Scrollbar(mainframe, orient="vertical", command=text.yview)
xs = ttk.Scrollbar(mainframe, orient="horizontal", command=text.xview)
text["yscrollcommand"] = ys.set
text["xscrollcommand"] = xs.set
ys.grid(column=1, row=0, sticky="ns")
xs.grid(column=0, row=1, sticky="we")
text.grid(column=0, row=0, sticky="N W E S")

# Insert instructions into textbox and bring it into focus when starting up
text.insert(
    "1.0",
    "\n\nBase64 Encoder/Decoder\nCreated By J.Low\n\nEnter or paste text to Encode/Decode here.\n\nThen select Encode/Decode from the Code Menu or Right Click and select from the context menu.",
)
text.focus()

# Run application
root.mainloop()
