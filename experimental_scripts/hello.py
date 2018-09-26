import tkinter as tk
root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter! \n Oh Man wish I had seen this earlier!!!")
w.pack()

root.mainloop()


#see https://www.python-course.eu/tkinter_labels.php

import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, text="Hello", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()