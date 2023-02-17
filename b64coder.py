from tkinter import *
from tkinter import ttk, messagebox
from base64 import b64encode, b64decode

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


def about():
    messagebox.showinfo(message="Base 64 Encoder/Decoder\nCreated By: J.Low")


def quit():
    exit()


# Setting up Main Form
root = Tk()
root.iconbitmap("encrypt.ico")
root.title("Base64 Encode/Decode")
root.resizable(FALSE, FALSE)

# Working on implementing Filebar
m = Menu(root)
f_edit = Menu(m, tearoff=0)
m.add_cascade(menu=f_edit, label="File")
f_edit.add_command(label="New", underline=1)
f_edit.add_command(label="Open", underline=1)
f_edit.add_command(label="Save", underline=1)
f_edit.add_command(label="Save As")
f_edit.add_separator()
f_edit.add_command(label="Close", underline=1)
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
m_edit.add_command(
    label="Find", command=lambda: root.event_generate("<<OpenFindDialog>>")
)
root["menu"] = m


def launchFindDialog(*args):
    messagebox.showinfo(message="I hope you find what you are looking for!")


root.bind("<<OpenFindDialog>>", launchFindDialog)

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
menu.add_command(label="Clear", command=clear)

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
encbutt = ttk.Button(twoframe, text="Encode", command=encode)
decbutt = ttk.Button(twoframe, text="Decode", command=decode)
clearbutt = ttk.Button(twoframe, text="Clear", command=clear)
encbutt.grid(column=1, row=0, sticky="N", pady=5)
decbutt.grid(column=1, row=1, sticky="N", pady=10)
clearbutt.grid(column=1, row=2, sticky="S", pady=10)

# Insert instructions into textbox and bring it into focus when starting up
text.insert(
    "1.0",
    "\n\nBase64 Encoder/Decoder\nCreated By J.Low\n\nEnter or paste text to Encode/Decode here.\n\nThen press the appropriate button on the right.",
)
text.focus()

# Run application
root.mainloop()
