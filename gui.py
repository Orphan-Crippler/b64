from tkinter import *
from tkinter import ttk, messagebox
from base64 import b64encode, b64decode


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
        ans = b64decode(dec.encode())
        text.delete(1.0, "end")
        text.insert(1.0, str(ans)[2:-1])
        return
    except Exception as x:
        messagebox.showerror(title="ERROR!", message=x)


root = Tk()
root.title("Base64 Encode/Decode")
root.resizable(FALSE, FALSE)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
twoframe = ttk.Frame(root, padding="3 3 12 12")
twoframe.grid(column=1, row=0, sticky=("N, W, E, S"))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = Text(mainframe, width=100, height=15)
ys = ttk.Scrollbar(mainframe, orient="vertical", command=text.yview)
text["yscrollcommand"] = ys.set
ys.grid(column=1, row=0, sticky="ns", pady=5)
text.grid(column=0, row=0, sticky="N", pady=5)
buttonL = ttk.Button(twoframe, text="Encode", command=encode)
buttonR = ttk.Button(twoframe, text="Decode", command=decode)
buttonL.grid(column=1, row=0, sticky="N", pady=5)
buttonR.grid(column=1, row=1, sticky="N", pady=10)
text.focus()

root.mainloop()
