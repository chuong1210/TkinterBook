from tkinter import *
from PIL import Image, ImageTk

class RegistrationPage:
    def __init__(self, master):
        self.window = master
        LoginPage = Frame(self.window)
        RegistrationPage = Frame(self.window)

        for frame in (LoginPage, RegistrationPage):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
         frame.tkraise()
         frame.update()

        show_frame(LoginPage)

        # All the code you provided here, replacing RegistrationPage with self.window
        self.design_frame5 = Listbox(RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
        self.design_frame5.place(x=0, y=0)

        self.design_frame6 = Listbox(RegistrationPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
        self.design_frame6.place(x=676, y=0)

        self.design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
        self.design_frame7.place(x=75, y=106)

        self.design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
        self.design_frame8.place(x=676, y=106)

# ==== Full Name =======
        name_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        name_entry.place(x=284, y=150, width=286, height=34)
        name_entry.config(highlightbackground="black", highlightcolor="black")
        name_label = Label(self.design_frame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        name_label.place(x=280, y=120)

# ======= Email ===========
        email_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        email_entry.place(x=284, y=220, width=286, height=34)
        email_entry.config(highlightbackground="black", highlightcolor="black")
        email_label = Label(self.design_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        email_label.place(x=280, y=190)

# ====== Password =========
        password_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
        password_entry.place(x=284, y=295, width=286, height=34)
        password_entry.config(highlightbackground="black", highlightcolor="black")
        password_label = Label(self.design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
        password_label.place(x=280, y=265)


        def password_command2():
         if password_entry.cget('show') == '•':
           password_entry.config(show='')
         else:
          password_entry.config(show='•')


        self.checkButton = Checkbutton(self.design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
        self.checkButton.place(x=290, y=330)


# ====== Confirm Password =============
        confirmPassword_entry = Entry(self.design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
        confirmPassword_entry.place(x=284, y=385, width=286, height=34)
        confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
        confirmPassword_label = Label(self.design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
        confirmPassword_label.place(x=280, y=355)

# ========= Buttons ====================
        SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
        SignUp_button.place(x=1100, y=175)

        SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
        SignUp_line.place(x=1100, y=203)

# ===== Welcome Label ==================
        welcome_label = Label(self.design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
        welcome_label.place(x=130, y=15)

# ========= Login Button =========
        login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
        login_button.place(x=845, y=175)

# ==== SIGN UP down button ============
        signUp2 = Button(self.design_frame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2')
        signUp2.place(x=285, y=435, width=286, height=50)

# ===== password icon =========
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(self.design_frame8, image=photo, bg='#f8f8f8')
        password_icon_label.image = photo
        password_icon_label.place(x=255, y=300)

# ===== confirm password icon =========
        confirmPassword_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(confirmPassword_icon)
        confirmPassword_icon_label = Label(self.design_frame8, image=photo, bg='#f8f8f8')
        confirmPassword_icon_label.image = photo
        confirmPassword_icon_label.place(x=255, y=390)

# ===== Email icon =========
        email_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(email_icon)
        emailIcon_label = Label(self.design_frame8, image=photo, bg='#f8f8f8')
        emailIcon_label.image = photo
        emailIcon_label.place(x=255, y=225)

# ===== Full Name icon =========
        name_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(name_icon)
        nameIcon_label = Label(self.design_frame8, image=photo, bg='#f8f8f8')
        nameIcon_label.image = photo
        nameIcon_label.place(x=252, y=153)

# ===== picture icon =========
        picture_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(picture_icon)
        picture_icon_label = Label(self.design_frame8, image=photo, bg='#f8f8f8')
        picture_icon_label.image = photo
        picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
        side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(self.design_frame7, image=photo, bg='#1e85d0')
        side_image_label.image = photo
        side_image_label.place(x=50, y=10)


# Use your class like this:

def page():
    window = Tk()
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    RegistrationPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()