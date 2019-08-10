from tkinter import *
# from tkinter.messagebox import *
# import tkinter.filedialog
import os


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry("900x600+100+50")
        self.title("Files manager for Bdouilleurs")
        self.iconbitmap("C:/Users/hubert et Agnès/Documents\The Bdouilleur2 space\Missions in python\Pythonsignev.ico")
        self.config(bg='#B9CFFF')
        self.minsize(700, 600)

        self.files_dir = []
        self.path = "C:/Users/hubert et Agnès/Documents\The Bdouilleur2 space"
        self.dir_image = PhotoImage(file="image_file.png")
        self.py_image = PhotoImage(file='py_file.png')
        self.txt_image = PhotoImage(file='txt_file.png')
        self.pdf_image = PhotoImage(file='pdf_file.png')
        self.avi_image = PhotoImage(file='avi_file.png')
        self.x_can = 30
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
        self.files = []
        self.dir = []
        print(path)
        self.x_can = 30
        self.y_can = 20
        self.files_dir = os.listdir(path)
        print(self.files_dir)
        for i in self.files_dir:
            if os.path.isfile(os.path.join(path, i)):
                self.files.append(i)
            else:
                self.dir.append(i)

        for i in range(len(self.files)):
            if len(self.files[i]) > 20:
                turn = len(self.files[i])%20
                # for t in range(turn+1):
                new_path = os.path.join(path, self.files[i])
                ext = new_path.split('.')[-1]
                ext = "." + ext
                s = self.files[i]
                s.replace(ext, '')
                s = s[:20] + '\n' + s[20:]
                self.files[i] = s

        self.can.delete(ALL)
        self.file_list.delete(0, END)
        for i in range(len(self.dir)):
            self.file_list.insert(i + 1, self.dir[i])
            self.file_image(self.dir_image, self.dir[i])

        for i in range(len(self.files)):
            new_path = os.path.join(path, self.files[i])
            ext = new_path.split('.')[-1]
            if ext == 'txt':
                image = self.txt_image
            elif ext == 'pdf':
                image = self.pdf_image
            elif ext == 'py':
                image = self.py_image
            elif ext == 'avi':
                image = self.avi_image
            else:
                image = None
            self.file_image(image, self.files[i])

        self.path = path
        self.bar.delete(0, END)
        self.bar.insert(0, self.path)

    def return_b(self):
        self.path = os.path.dirname(self.path)
        self.new_path(self.path)

    def click(self, event=None):
        selection = self.file_list.curselection()
        selection = self.file_list.get(selection)
        self.path = os.path.join(self.path, selection)
        self.new_path(self.path)

    def file_image(self, image, text):
        if image == None:
            self.can.create_text(self.x_can + 30 + len(text), self.y_can, text=text)
            self.y_can += 40
        else:
            if self.y_can >= 540:
                self.x_can += 200
                self.y_can = 20
            self.can.create_image(self.x_can, self.y_can, image=image)
            self.x_can += 60
            self.can.create_text(self.x_can + len(text), self.y_can, text=text)
            self.y_can += 40
            self.x_can -= 60


win = Interface()
win.mainloop()
