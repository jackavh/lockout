import os

import tkinter as tk
from tkinter import filedialog, Text

import lockout as lock


bg = '#A6CFE2'
bg2= '#A6CFA2'
fg = '#0B0C11'
tx = '#FFFFFF'
count = '00:00:00'
root = tk.Tk()
root.title('Lockout')
canvas = tk.Canvas(root, height=400, width=650, bg=bg)
canvas.pack()

# Frame for countdown
cframe = tk.Frame(root, bg=bg)
cframe.place(relwidth=1, relheight=0.8, relx=0, rely=0)

# Frame for buttons
bframe = tk.Frame(root, bg=fg)
bframe.place(relwidth=1, relheight=0.2, relx=0, rely=0.8)

# Close button
closeB = tk.Button(bframe, text="Close", padx=50, pady=20, fg=fg, bg=bg, relief='flat')
closeB.pack(side=tk.RIGHT, padx=20)

# Lock button
lockB = tk.Button(bframe, text="Lock", padx=50, pady=20, fg=fg, bg=bg, relief='flat')
lockB.pack(side=tk.RIGHT, padx=10)

# Countdown frame
cdown = tk.Label(cframe, bg=bg, text=count, font=("Arial", 36), width=350, height=480)
cdown.pack()

root.mainloop()


def test():
    root = tk.Tk()
    apps = []


    def addApp():

        for widget in frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                                filetypes=(("executables", "*exe"), ("all files", "*.*")))
        apps.append(filename)
        print(filename)
        for app in apps:
            label = tk.Label(frame, text=app, bg='gray')
            label.pack()


    def runApps():
        for app in apps:
            os.startfile(app)


    canvas = tk.Canvas(root, height=400, width=650, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    """
    relwidth: multiple of 1 of canvas size
    relx: attachment point % of canvas size
    """
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = tk.Button(frame, text="Open File", padx=10, pady=5,
                         fg="white", bg="#263D42", command=addApp)
    openFile.pack()

    runApps = tk.Button(frame, text="Run Apps", padx=10, pady=5,
                         fg="white", bg="#263D42", command=runApps)
    runApps.pack()

    root.mainloop()