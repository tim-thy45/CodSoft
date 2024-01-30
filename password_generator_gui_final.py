from tkinter import *
import string
import random

def generator():
    passwordField.delete(0, END)
    sa = string.ascii_lowercase
    ca = string.ascii_uppercase
    ns = string.digits
    sc = string.punctuation

    all_chars = sa + ca + ns + sc
    pl = int(length_Box.get())

    if choice.get() == 1:
        passwordField.insert(0, ''.join(random.sample(sa + ca, pl)))

    if choice.get() == 2:
        passwordField.insert(0, ''.join(random.sample(sa + ca + ns, pl)))

    if choice.get() == 3:
        passwordField.insert(0, ''.join(random.sample(all_chars, pl)))
    if choice.get() == 0:
        passwordField.insert(0, "#Enter Strength#")


root = Tk()
root.config(bg='blue2')
root.title('Password Generator')
root.geometry('300x400')

# Change the fonts
font_label = ('Helvetica', 14, 'bold')
font_radio_button = ('Helvetica', 12)
font_spinbox = ('Helvetica', 12)
font_button = ('Helvetica', 12)
font_entry = ('Helvetica', 12)

choice = IntVar()

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='blue2', fg='gold')
passwordLabel.grid(pady=10)

passwordLabel = Label(root, text='Password Strength', font=font_label, bg='blue2', fg='gold')
passwordLabel.grid(pady=10)

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=font_radio_button,
                              bg='gold', activebackground='RoyalBlue1')
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=font_radio_button,
                                bg='gold', activebackground='RoyalBlue1')
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=font_radio_button,
                                bg='gold', activebackground='RoyalBlue1')
strongradioButton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=font_label, bg='blue2', fg='gold')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=font_spinbox)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate', font=font_button, command=generator, bg='gold',
                        activebackground='RoyalBlue1')
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=font_entry)
passwordField.grid(pady=15)

root.mainloop()
