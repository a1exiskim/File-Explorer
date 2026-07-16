import _tkinter as tk
import os
import os.path 

class GUI:
    def __init__(self):
       # initialize the main window 
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.configure(bg = 'FFFFFF')
        self.panel_one = tk.Button(self.root, 
                                   text = 'Multiple level directory tree for navigation', 
                                   width = '900', 
                                   height = '500')
       
       
        # configure row/column weights on the root window so the interface can resize itself
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=5)

        # create panel 3
        self.panel3 = tk.Label(self.root, text = 'Info Display', bg = '#8FBAEF', fg = 'white')
        self.panel3.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

        # create panel 1
        self.panel1 = tk.Label(self.root, text = 'Directory Tree', bg='#A6A6A6', fg = 'white')
        self.panel1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # create panel 2
        self.panel2 = tk.Label(self.root, text = 'List of Files', bg = ''"#63976F", fg = 'white')
        self.panel2.grid(row=1, column = 1, sticky='nsew', padx=5, pady=5)


