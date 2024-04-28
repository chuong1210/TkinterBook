from tkinter import *
from PIL import ImageTk

#Functionlity
def user_enter(event):
    if username_entry.get()=='Username here':
        username_entry.delete(0, END)

def password_enter(event):
    if password_entry.get()== 'Password here':
        password_entry.delete(0, END)

def hide():
    open_eye.config(file = 'close_eye.png')
    password_entry.config(show='*')
    eye_button.config(command=show)

def show():
    open_eye.config(file='open_eye.png')
    password_entry.config(show='')
    eye_button.config(command=hide)

#GUI part

login_window = Tk()
login_window.geometry('965x606+50+50')
login_window.resizable(0, 0)
login_window.title('Task Manager - login page')
bg_image = ImageTk.PhotoImage(file = 'codettes.png')

bg_label = Label(login_window, image=bg_image)
bg_label.place(x = 0, y = 0)

heading = Label(login_window, text = "USER LOGIN", bg = 'white', font = ('Arial', 35, 'bold'),
                fg = 'midnight blue')
heading.place(x=600, y = 50)

username_entry = Entry(login_window, width=25, font = ('Arial', 16, 'bold'), bd = 0, fg='midnight blue',
                       bg='white')
username_entry.place(x=600, y = 150)
username_entry.insert(0, 'Username here')

username_entry.bind('<FocusIn>', user_enter)

password_entry = Entry(login_window, width=25, font = ('Arial', 16, 'bold'), bd = 0,
                       bg='white', fg ='midnight blue')
password_entry.place(x=600, y = 230)
password_entry.insert(0, 'Password here')

password_entry.bind('<FocusIn>', password_enter)

open_eye = PhotoImage(file = 'open_eye.png', )
eye_button = Button(login_window, image = open_eye, border=0, bg = 'white',
                    activebackground='white', cursor='hand2', command= hide)
eye_button.place(x = 880, y = 230)

forget_button = Button(login_window, text = 'Forgot password', font = ('Arial', 12, 'bold'),
                       fg='midnight blue', border=0, bg = 'white', activebackground='white',
                       cursor='hand2', activeforeground='midnight blue')
forget_button.place(x = 760, y = 260)

login_button = Button(login_window, text = 'Login', font = ('Open Sans', 14, 'bold'),
                      fg= 'midnight blue', bg='magenta3', activeforeground='white',
                      activebackground= 'magenta3', cursor='hand2', bd = 0, width = 19)
login_button.place(x = 620, y = 300)

orlabel = Label(login_window, text='--------------- Or -----------------', font = ('Arial', 16),
                bg = 'white', fg = 'midnight blue')
orlabel.place(x = 600, y = 350)

facebook_logo = PhotoImage(file = 'facebook.png')
fb_label = Label(login_window, image = facebook_logo, bg='white', cursor='hand2')
fb_label.place(x = 640, y = 400)

google_logo = PhotoImage(file = 'google.png')
google_label = Label(login_window, image = google_logo, bg='white', cursor='hand2')
google_label.place(x = 780, y = 400)


signup_label = Label(login_window, text='Don`t have an account?', font = ('Arial', 12, 'bold'),
                bg = 'white', fg = 'midnight blue')
signup_label.place(x = 560, y = 450)

register_button = Button(login_window, text = 'Register now!', font = ('Arial', 12, 'bold'),
                      fg= 'red', bg='white', activeforeground='white',
                      activebackground= 'white', cursor='hand2', bd = 0, width = 12)
register_button.place(x = 760, y = 450)


login_window.mainloop()
