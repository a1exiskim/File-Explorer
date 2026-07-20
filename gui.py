import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import os.path 
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        '''initializes the GUI'''
        
        # initialize the main window 
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.configure(bg = '#FFFFFF')
       
        # configure row/column weights on the root window so the interface can resize itself
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1) 
        self.root.grid_rowconfigure(0, weight=1) # panel 3
        self.root.grid_rowconfigure(1, weight=5) # panel 1 & 2

        # ensure panel 1 is one colour
        style = ttk.Style()
        style.configure("Treeview", background='#A6A6A6', fieldbackground='#A6A6A6')


        # load icons for Treeview
        folder_image = Image.open("folder.jpeg")
        folder_image = folder_image.resize((20, 20))
        self.folder_icon = ImageTk.PhotoImage(folder_image)

        file_image = Image.open("file.jpg")
        file_image = file_image.resize((20, 20))
        self.file_icon = ImageTk.PhotoImage(file_image)


        # create panel 3
        self.panel3 = tk.Frame(self.root, bg = '#8FBAEF')
        self.panel3.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.panel3_title = tk.Label(self.panel3, text = 'Directory Summary:', bg = '#8FBAEF', fg = '#FFFFFF')
       
        self.panel3.grid_rowconfigure(0, weight=1)
        self.panel3.grid_columnconfigure(0, weight=1)
        self.panel3.grid_rowconfigure(1, weight = 5) # space for directory summary
        
        self.panel3_title.grid(row=0, column=0, sticky='nsew')

        self.directory_summary_label = tk.Label(self.panel3, text='')
        self.directory_summary_label.grid(row=1, column=0, sticky='nsew')

        # create panel 1
        self.panel1 = tk.Frame(self.root, bg='#A6A6A6')
        self.panel1.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.panel1_title= tk.Label(self.panel1, text = 'Directory Tree', bg='#A6A6A6', fg = '#FFFFFF')
       
        self.panel1.grid_rowconfigure(0, weight=1)
        self.panel1.grid_columnconfigure(0, weight=1)
        self.panel1.grid_rowconfigure(1, weight=1) # space for 'choose folder' button
        self.panel1.grid_rowconfigure(2, weight=5) # space for directory tree

        self.panel1.configure(bg='red') #temp
        
        self.panel1_title.grid(row=0, column=0, sticky='nsew')
        
        self.choose_folder_button = tk.Button(self.panel1, text='Choose Folder', command=self.choose_folder, bg='#A6A6A6')
        self.choose_folder_button.grid(row=1, column=0, sticky='nsew')

        self.tree = ttk.Treeview(self.panel1)
        self.tree.grid(row=2, column=0, sticky='nsew')

        self.tree.bind('<<TreeviewSelect>>', self.tree_item_selection)

        # create panel 2
        self.panel2 = tk.Frame(self.root, bg = '#63976F')
        self.panel2.grid(row=1, column = 1, sticky='nsew', padx=5, pady=5)
        self.panel2_title = tk.Label(self.panel2, text = 'Files', bg = '#63976F', fg = '#FFFFFF')
       
        self.panel2.grid_rowconfigure(0, weight=1)
        self.panel2.grid_columnconfigure(0, weight=1)
        self.panel2.grid_rowconfigure(1, weight=5) # space for files
        
        self.panel2_title.grid(row=0, column=0, sticky='nsew')

        self.initial_path = None 

        self.path_dictionary = {}

    
    def choose_folder(self):
        '''gathers all the main directories from the os for user to choose from'''
        
        select_folder = filedialog.askdirectory() # returns file path as string

        if select_folder != "":
            self.initial_path = select_folder 
            self.display_folder_contents(self.initial_path)
            self.display_directory_summary()
       

    def get_selected_folder_contents(self, path):
        '''gathers the selected directory's contents'''

        folders = []
        files = []
        contents = os.listdir(path) # returns list of names of contents in folder 

        # check if contents are folder or file 
        for item in contents:
            path_to_check = os.path.join(self.initial_path, item) # joins content name with selected folder's path

            if os.path.isdir(path_to_check): 
                folders.append(item) # if path_to_check leads to a another folder, append to list of folders
            else:
                files.append(item) # if path_to_check does not lead to another folder, must be a file, so append to list of files

        return folders, files


    def display_folder_contents(self, path):
        '''displays the selected directory along with its subdirectories and files underneath'''

        self.tree.delete(*self.tree.get_children()) # remove old directory's contents

        folders, files = self.get_selected_folder_contents(path)

        directory_name = os.path.basename(path) # get the name of the selected directory from its path
        root_node = self.tree.insert('', 'end', text=directory_name)

        self.path_dictionary[root_node] = path

        for folder in folders:
            folder_to_check = os.path.join(path, folder)
            folder_node = self.tree.insert(root_node, 'end', text=folder, image=self.folder_icon)
            self.path_dictionary[folder_node] = folder_to_check

        for file in files:
            file_to_check = os.path.join(path, file)
            file_node = self.tree.insert(root_node, 'end', text=file, image=self.file_icon)
            self.path_dictionary[file_node] = file_to_check

    def display_directory_summary(self):
        '''displays metadata of current selected directory in panel 3'''

        folders, files = self.get_selected_folder_contents()  
        selected_directory = os.path.basename(self.initial_path)
        self.directory_summary_label.config(
            text= f"Selected Directory: {selected_directory}\nPath: {self.initial_path}\nNumber of Folders: {len(folders)}\nNumber of Files: {len(files)}")

        
    def tree_item_selection(self, event):
        '''Handles actions performed after a user selects a node in the directory tree.
           Retrieves the selected node's path, determines whether it is a directory,
           and obtains the contents of the selected directory for further processing.'''
        
        item_selected = self.tree.selection() # returns a tuple
        print(item_selected)
        item_node_id = item_selected[0] # item selected is only ever one item, we can extract the id from the 0th index
        
        item_node_path = self.path_dictionary.get(item_node_id)

        if os.path.isdir(item_node_path):
            folders, files = self.get_selected_folder_contents(item_node_path)
            self.display_subdirectory(item_node_id, folders)

    
    def display_subdirectory(self, selected_node, subfolders_to_display):
        '''inserts each subfolder underneath its parent folder'''
        
        for subfolder in subfolders_to_display:
            selected_node_path = self.path_dictionary.get(selected_node)
            full_node_path = os.path.join(selected_node_path, subfolder)
            subfolder_node = self.tree.insert(selected_node, 'end', text=subfolder , image=self.folder_icon)
            self.path_dictionary[subfolder_node] = full_node_path


gui = GUI()
gui.root.mainloop()