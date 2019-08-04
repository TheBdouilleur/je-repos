from tkinter import *
# from tkinter.messagebox import *
# import tkinter.filedialog
import os


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry("700x600+100+50")
        self.title("Files manager for Bdouilleurs")
        self.iconbitmap("C:/Users/hubert et Agnès/Documents\The Bdouilleur2 space\Missions in python\Pythonsignev.ico")
        self.config(bg='#B9CFFF')
        self.minsize(700, 600)

        self.files_dir = []
        self.path = "C:/Users/hubert et Agnès/Documents\The Bdouilleur2 space"
        self.dir_image = PhotoImage(file="image_file.png")
        self.py_image = PhotoImage(file='py_file.png')
        self.txt_image = PhotoImage(file='txt_file.png')
        self.x_can = 20
        self.y_can = 20
        self.files = []
        self.dir = []

        self.frame = Frame(self, bd=0, relief=SUNKEN, width=300, bg='#B9CFFF')
        self.file_list = Listbox(self.frame, font=('Courrier', 10), height=40, width=40)
        self.file_list.bind('<Double-Button-1>', self.click)

        self.bar = Entry(self, font=('Courrier', 10), fg='black')

        self.arow = PhotoImage(file="arow.png")
        self.return_button = Button(self.frame, image=self.arow, font=('Courrier', 20), height=15, width=50, bg='white')
        self.return_button.config(activebackground='white', command=self.return_b)

        self.can = Canvas(self, width=50, height=700, bg='white')

        self.return_button.grid(row=0, column=0)
        self.file_list.grid(row=1, column=0, columnspan=15)
        self.frame.pack(side=LEFT, fill=Y)
        self.bar.pack(side=TOP, fill=X)
        self.can.pack(fill=BOTH)
        self.new_path(self.path)

    def new_path(self, path):
        self.can.delete(ALL)
        self.file_list.delete(0, END)
        self.x_can = 20
        self.y_can = 20
        self.files_dir = os.listdir(path)
        for i in self.files_dir:
            if os.path.isfile(os.path.join(path, i)):
                self.files.append(i)
            else:
                self.dir.append(i)

        for i in range(len(self.dir)):
            self.file_list.insert(i + 1, self.dir[i])
            self.file_image(self.dir_image, self.dir[i])

        for i in range(len(self.files)):
            new_path = os.path.join(path, self.files[i])
            ext = new_path.split('.')[-1]
            if ext == 'txt':
                image = self.txt_image
                self.file_image(image, self.files_dir[i])
            elif ext == 'pdf':
                pass
                # image =
            elif ext == 'py':
                image = self.py_image
                self.file_image(image, self.files_dir[i])
            else:
                self.can.create_text(self.x_can, self.y_can, text=self.files[i])
                self.y_can += 40

        self.path = path
        self.bar.delete(0, END)
        self.bar.insert(0, self.path)

    def return_b(self):
        self.path = os.path.dirname(self.path)
        self.new_path(self.path)

    def click(self, event=None):
        selection = self.file_list.curselection()
        selection = self.file_list.get(selection)
        path = os.path.join(self.path, selection)
        self.new_path(path)

    def file_image(self, image, text):
        if self.y_can >= 540:
            self.x_can += 200
            self.y_can = 20
        self.can.create_image(self.x_can, self.y_can, image=image)
        self.x_can += len(text) + 50
        self.can.create_text(self.x_can, self.y_can, text=text)
        self.y_can += 40
        self.x_can -= len(text) + 50



win = Interface()
win.mainloop()
