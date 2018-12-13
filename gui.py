import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text = "Hello World!")
w.pack()

root.mainloop()