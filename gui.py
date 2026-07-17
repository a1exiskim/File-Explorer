import tkinter as tk
from tkinter import ttk
import os
import os.path 

class GUI:
    def __init__(self):
       # initialize the main window 
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.configure(bg = 'FFFFFF')
       
        # configure row/column weights on the root window so the interface can resize itself
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1) 
        self.root.grid_rowconfigure(0, weight=1)

        # create panel 3
        self.panel3 = tk.Frame(self.root, bg = '#8FBAEF')
        self.panel3.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.panel3_title = tk.Label(self.panel3, text = 'Selected Directory:', fg = '#FFFFFF')
       
        self.panel3.grid_rowconfigure(0, weight=1)
        self.panel3.grid_columnconfigure(0, weight=1)
        self.pnael3.grid_rowconfigure(1, weight = 5) # space for actual selected directory
        
        self.panel3_title.grid(row=0, column=0, sticky='nsew')

        # create panel 1
        self.panel1 = tk.Frame(self.root, bg='#A6A6A6')
        self.panel1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.panel1_title= tk.Label(self.panel1, text = 'Directory Tree', fg = '#FFFFFF')
       
        self.panel1.grid_rowconfigure(0, weight=1)
        self.panel1.grid_columnconfigure(0, weight=1)
        self.panel1.grid_rowconfigure(1, weight=5) # space for directory tree
        
        self.panel1_title.grid(row=0, column=0, sticky='nsew')

        # create panel 2
        self.panel2 = tk.Frame(self.root, bg = '#63976F')
        self.panel2.grid(row=1, column = 1, sticky='nsew', padx=5, pady=5)
        self.panel2_title = tk.Label(self.panel2, text = 'Files', fg = '#FFFFFF')
       
        self.panel2.grid_rowconfigure(0, weight=1)
        self.panel2.grid_columnconfigure(0, weight=1)
        self.panel2.grid_rowconfigure(1, weight=5) # space for files
        
        self.panel2_title.grid(row=0, column=0, sticky='nsew')

        self.tree = ttk.Treeview(self.panel1)
        self.initial_path = self.initial_path


    def create_directory_tree(self):
        pass