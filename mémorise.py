#I will put my code here
from tkinter import *
from Memorise.Word import Word

# creer une fenetre
window = Tk()

# La modifier
window.title('Memorise')
window.iconbitmap('home.ico')
window.geometry("900x500")
window.minsize(400, 150)
window.config(background='#fec20a')

users = {'J-E 1': 'je in 1', 'i': 'i'}

# I make two variables for pass an username
password_try = StringVar()
username_try = StringVar()

width_image = 357
heigth_image = 210

# creer la boite
frame = Frame(window, bg="#fec20a")

# ajouter du text
text1 = Label(frame, text="Welcome on Mémorise !!", font=("Comic sans MS", 40), bg='#fec20a', fg='white')


can = Canvas(window, width=width_image, height=heigth_image, bd=0, highlightthickness=0)

# function which is the application
def appli():
    frame_sign.destroy()
    one = Word("When is the next week", 'next week', 'je in 1')
    print(one.calculate_m(720))
    print(one.calculate_m(168))
    print(one.calculate_m(5))



def account():
    for i in users:
        if password_try.get() in users[i]:
            appli()
        else:
            frame_sign.destroy()
            button_one()


# I make a new frame
frame_sign = Frame(window, bg='#fec20a')
text_username = Label(frame_sign, text="Username", font=("Comic sans MS", 40), bg='#fec20a', fg='white')
entry_username = Entry(frame_sign, font=("Comic sans MS", 40), bg='#fec20a', fg='white', textvariable=username_try)
text_password = Label(frame_sign, text="Password", font=("Comic sans MS", 40), bg='#fec20a', fg='white')
entry_password = Entry(frame_sign, font=("Comic sans MS", 40), bg='#fec20a', fg='white', textvariable=password_try)
button2 = Button(frame_sign, text="Open appli", font=("Comic sans MS", 40), bg='#fec20a', fg='white', command=account)


# fonction qui se compile quand on appuie sur le premier bouton
def button_one():
    # I clean the window
    frame.destroy()
    can.destroy()

    # And make in the frame two texts and to entry box
    text_username.pack()
    entry_username.pack()
    text_password.pack()
    entry_password.pack()
    button2.pack(pady=25, fill=X)

    # I draw the frame
    frame_sign.pack(expand=YES)


text1.pack()

# ajouter un bouton
button1 = Button(frame, text="Sign up", font=("Comic sans MS", 30), bg='white', fg='#fec20a', command=button_one)
button1.pack(pady=25, fill=X)

# creer une image
img = PhotoImage(file="eureka.png").zoom(80).subsample(64)
can.create_image(width_image / 2, heigth_image / 2, image=img)
can.pack(expand=YES)

# ajouter la boite
frame.pack(side=BOTTOM)

# affichage
window.mainloop()

