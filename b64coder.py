from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
from base64 import b64encode, b64decode
import os

fileName = ""

# File Functions
def nFile():
    global fileName
    msg_save = messagebox.askquestion(
        "Save Document?", "Would you like to Save the current document?", icon="warning"
    )

    if msg_save == "yes":
        sFileAs()
        clear()
    else:
        fileName = ""
        clear()


def oFile():
    global fileName

    if text != "":
        clear()

    f = filedialog.askopenfile(mode="r")
    fileName = f.name
    fn = open(f.name, "r").read()
    text.insert(1.0, fn)
    f.close()


def sFile():
    global fileName

    if fileName == "":
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
    # Needs implementation
    messagebox.showwarning("TODO", "Needs to be implemented...")


# Setting up Main Form
root = Tk()

if "nt" == os.name:
    root.iconbitmap("encrypt.ico")
else:
    pass

root.title("Base64 Encode/Decode")
root.resizable(FALSE, FALSE)

# Working on implementing Filebar
m = Menu(root)
root["menu"] = m

f_edit = Menu(m, tearoff=0)
m.add_cascade(menu=f_edit, label="File")
f_edit.add_command(label="New", underline=1, command=nFile)
f_edit.add_command(label="Open", underline=1, command=oFile)
f_edit.add_command(label="Save", underline=1, command=sFile)
f_edit.add_command(label="Save As", command=sFileAs)
f_edit.add_separator()
f_edit.add_command(label="Exit", underline=2, command=quit)

m_edit = Menu(m, tearoff=0)
m.add_cascade(menu=m_edit, label="Edit")
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
m_edit.add_command(label="Find", command=find)
m_edit.add_separator()
m_edit.add_command(label="Clear", underline=1, command=nFile)

e_edit = Menu(m, tearoff=0)
m.add_cascade(menu=e_edit, label="Code")
e_edit.add_command(label="Encode", command=encode)
e_edit.add_command(label="Decode", command=decode)

# Setting up Frames
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
twoframe = ttk.Frame(root, padding="3 3 3 3")
twoframe.grid(column=1, row=0, sticky=("N, W, E, S"))
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
text = Text(mainframe, width=100, height=15)
ys = ttk.Scrollbar(mainframe, orient="vertical", command=text.yview)
text["yscrollcommand"] = ys.set
ys.grid(column=1, row=0, sticky="ns", pady=5)
text.grid(column=0, row=0, sticky="N", pady=5)

# Insert instructions into textbox and bring it into focus when starting up
text.insert(
    "1.0",
    "\n\nBase64 Encoder/Decoder\nCreated By J.Low\n\nEnter or paste text to Encode/Decode here.\n\nThen selct Encode/Decode from the Code Menu or Right Click and select from the context menu.",
)
text.focus()

# Run application
root.mainloop()
