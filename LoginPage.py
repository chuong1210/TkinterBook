from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
from page.user import run_user
from page.admin import run_admin
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import json
from  tkcalendar import DateEntry
import re
from tkinter import messagebox       
import os
import sys
json_file_path = os.path.join('json_file', 'users_detail.json')
with open(json_file_path) as f:
    user_data = json.load(f)

class LoginPage:
    def login_function(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        for user_info in user_data['users']:
            if user_info['username'] == entered_username and user_info['password'] == entered_password:
                if user_info['type'] == 'admin':
                    new_window = Toplevel(self.window)
                    run_admin(new_window, user_info)
                    self.window.withdraw()
                elif user_info['type'] == 'user':
                    new_window = Toplevel(self.window)
                    run_user(new_window, user_info)
                    self.window.withdraw()
                else:
                    print("Unknown user type.")
                self.error_message_label.config(text='')
                return
            self.error_message_label.config(text='Tên đăng nhập hoặc mật khẩu không đúng.', fg='red')

    def __init__(self, window):
      
        self.window = window

        self.window.geometry('965x606+50+50')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Trang đăng nhập')
        self.window.iconbitmap(os.path.join('images', 'changepw.ico'))
   
        
        self.is_login_mode = True
        self.display_all()
    def display_all(self):

        self.bg_frame = Image.open(os.path.join('images','backgroundbook.jpg'))
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo

        self.bg_panel.pack(fill='both', expand='yes')
        self.lgn_frame = Frame(self.window, bg='#1974d3', width=950, height=600)
        self.lgn_frame.place(x=250, y=150)

        self.txt = "Chào mừng độc giả"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Roboto', 25, "bold"), bg="#1974d3",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=340, y=30, width=310, height=50)

        self.side_image = Image.open(os.path.join('images','huit.png'))

        width, height = self.side_image.size
        new_width = width // 3
        new_height = height //3
        self.side_image = self.side_image.resize((new_width, new_height))

        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=200)

        self.sign_in_image = Image.open(os.path.join('images','CHUONG.png'))

        width, height = self.sign_in_image.size
        new_width = width // 4
        new_height = height // 4
        self.sign_in_image = self.sign_in_image.resize((new_width, new_height))

        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)

        self.sign_in_image = Image.composite(self.sign_in_image, Image.new("RGBA", (new_width, new_height), 0), mask)

        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=100)

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#1974d3", fg="white", cursor="hand1",
                                   font=("Roboto", 15, "bold"))
        self.sign_in_label.place(x=600, y=240)

        self.sign_up_label = Label(self.lgn_frame, text="Sign Up", bg="#1974d3", fg="white", cursor="hand1",
                                   font=("Roboto", 15, "bold"))
        self.sign_up_label.place(x=690, y=240)
        self.sign_in_line = Canvas(self.lgn_frame, width=78, height=1, bg='#DFDFDF', cursor="hand1", highlightthickness=0)
        self.sign_in_line.place(x=598, y=268)

        self.sign_up_line = Canvas(self.lgn_frame, width=78, height=1, bg='#1974d3', highlightthickness=0, cursor="hand1")
        self.sign_up_line.place(x=690, y=268)
         
        if  self.is_login_mode ==True:
        

            self.sign_in_label.bind("<Button-1>", self.on_sign_in_click)
            self.sign_up_label.bind("<Button-1>", self.on_sign_up_click)   

            self.username_label = Label(self.lgn_frame, text="Username", bg="#1974d3", fg="#4f4e4d",
                                        font=("Roboto", 13, "bold"))
            self.username_label.place(x=550, y=300)

            self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                        font=("Roboto ", 12, "bold"), insertbackground='#6b6a69')
            self.username_entry.place(x=580, y=330, width=270)

            self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#ffcc98", highlightthickness=0)
            self.username_line.place(x=550, y=359)
            desired_size = (20, 20)
            self.username_icon = Image.open(os.path.join('images', 'username2.png')).resize(desired_size)
            photo = ImageTk.PhotoImage(self.username_icon)
            self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
            self.username_icon_label.image = photo
            self.username_icon_label.place(x=550, y=332)

            self.login = Button(self.lgn_frame, text='Đăng nhập', command=self.login_function, font=("Roboto", 14, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#8865ff', fg='white')
            self.login.place(x=552, y=450)
            self.error_message_label = Label(self.lgn_frame, text='', bg="#1974d3")
            self.error_message_label.place(x=580, y=427)

            self.password_label = Label(self.lgn_frame, text="Password", bg="#1974d3", fg="#4f4e4d",
                                        font=("Roboto", 13, "bold"))
            self.password_label.place(x=550, y=363)

            self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                        font=("Roboto", 12, "bold"), show="*", insertbackground='#6b6a69')
            self.password_entry.config(disabledbackground="#ffffff")
            self.password_entry.place(x=580, y=390, width=244)

            self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#ffcc98", highlightthickness=0)
            self.password_line.place(x=550, y=416)
            desired_size = (20, 20)

            self.password_icon = Image.open(os.path.join('images', 'password2.png')).resize(desired_size)

            photo = ImageTk.PhotoImage(self.password_icon)
            self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
            self.password_icon_label.image = photo
            self.password_icon_label.place(x=550, y=388)
            self.show_image = ImageTk.PhotoImage(file=os.path.join('images', 'open_eye.png'))

            

            self.hide_image = ImageTk.PhotoImage(file=os.path.join('images', 'close_eye.png'))


            self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                    activebackground="#1974d3"
                                    , borderwidth=0, background="#1974d3", cursor="hand2")
            self.show_button.place(x=824, y=390)
        else:
            self.clear_frame(self.lgn_frame)  # Clear the frame

            # ... (sign-up UI elements)

            # Remove the login button from sign up mode
            self.bg_frame = Image.open( os.path.join('images', 'backgroundbook.jpg'))
     
            photo = ImageTk.PhotoImage(self.bg_frame)
            self.bg_panel = Label(self.window, image=photo)
            self.bg_panel.image = photo

            self.bg_panel.pack(fill='both', expand='yes')
            self.lgn_frame = Frame(self.window, bg='#1974d3', width=950, height=600)
            self.lgn_frame.place(x=250, y=150)

            self.txt = "Chào mừng độc giả"
            self.heading = Label(self.lgn_frame, text=self.txt, font=('Roboto', 25, "bold"), bg="#1974d3",
                                fg='white',
                                bd=5,
                                relief=FLAT)
            self.heading.place(x=340, y=30, width=310, height=50)

            self.side_image = Image.open(  os.path.join('images', 'huit.png'))

            width, height = self.side_image.size
            new_width = width // 3
            new_height = height //3
            self.side_image = self.side_image.resize((new_width, new_height))

            photo = ImageTk.PhotoImage(self.side_image)
            self.side_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
            self.side_image_label.image = photo
            self.side_image_label.place(x=50, y=200)

            self.sign_in_image = Image.open( os.path.join('images', 'CHUONG.PNG'))
            width, height = self.sign_in_image.size
            new_width = width // 4
            new_height = height // 4
            self.sign_in_image = self.sign_in_image.resize((new_width, new_height))

            mask = Image.new("L", (new_width, new_height), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_width, new_height), fill=255)

            self.sign_in_image = Image.composite(self.sign_in_image, Image.new("RGBA", (new_width, new_height), 0), mask)

            photo = ImageTk.PhotoImage(self.sign_in_image)
            self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
            self.sign_in_image_label.image = photo
            self.sign_in_image_label.place(x=620, y=100)

            self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#1974d3", fg="white", cursor="hand1",
                                    font=("Roboto", 15, "bold"))
            self.sign_in_label.place(x=600, y=240)

            self.sign_up_label = Label(self.lgn_frame, text="Sign Up", bg="#1974d3", fg="white", cursor="hand1",
                                    font=("Roboto", 15, "bold"))
            self.sign_up_label.place(x=690, y=240)

        

            self.sign_up_line = Canvas(self.lgn_frame, width=78, height=1, bg='#fff', highlightthickness=0, cursor="hand1")
            self.sign_up_line.place(x=690, y=268)

            self.sign_in_label.bind("<Button-1>", self.on_sign_in_click)
            self.sign_up_label.bind("<Button-1>", self.on_sign_up_click)   
        

            self.username_label = Label(self.lgn_frame, text="Username", bg="#1974d3", fg="#4f4e4d",
                                        font=("Roboto", 13, "bold"))
            self.username_label.place(x=550, y=335)
            self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                        font=("Roboto ", 12, "bold"), insertbackground='#6b6a69')
            self.username_entry.place(x=550, y=360, width=270)
            self.username_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#ffcc98", highlightthickness=0)
            self.username_line.place(x=550, y=385)

            self.email_label = Label(self.lgn_frame, text="Email", bg="#1974d3", fg="#4f4e4d",
                                        font=("Roboto", 13, "bold"))
            self.email_label.place(x=550, y=275)
            self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                        font=("Roboto ", 12, "bold"), insertbackground='#6b6a69')
            self.email_entry.place(x=550, y=300, width=270)
            self.email_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#ffcc98", highlightthickness=0)
            self.email_line.place(x=550, y=325)

            self.password_label = Label(self.lgn_frame, text="Password", bg="#1974d3", fg="#4f4e4d",
                                        font=("Roboto", 13, "bold"))
            self.password_label.place(x=550, y=395)
            self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                        font=("Roboto", 12, "bold"), show="*", insertbackground='#6b6a69')
            self.password_entry.place(x=550, y=420, width=270)
            self.password_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#ffcc98", highlightthickness=0)
            self.password_line.place(x=550, y=445)
            self.birthday_label = Label(self.lgn_frame, text="Birthday", bg="#fff", fg="#4f4e4d",
                                        font=("Roboto", 13, "bold"))
            self.birthday_label.place(x=558, y=460)

            self.birthday_entry = DateEntry(self.lgn_frame, 
                                            date_pattern='dd/MM/yyyy',  # Set date format
                                            width=18,
                                            background='darkblue',
                                            foreground='white',
                                            borderwidth=3)
            self.birthday_entry.place(x=650, y=460) 
            self.login.place_forget() 


            self.signup_button = Button(self.lgn_frame, text='Sign Up', command=self.signup_function, font=("Roboto", 14, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#8865ff', fg='white')
            self.signup_button.place(x=535, y=500)

            self.back_to_login_button = Button(self.lgn_frame, text='Back to Login', command=self.back_to_login_function, font=("Roboto", 14, "bold"), width=25, bd=0,
                                bg='#3047ff', cursor='hand2', activebackground='#8865ff', fg='white')
            self.back_to_login_button.place(x=535, y=555)

            self.error_message_label = Label(self.lgn_frame, text='', bg="#1974d3", font=("Times", 24, "bold"))
            self.error_message_label.place(x=80, y=470)

    def on_sign_in_click(self,e):
   
        self.is_login_mode = True
        self.display_all()




    def on_sign_up_click(self,e):
        
        self.is_login_mode = False
        self.display_all()

  

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def display_signup_interface(self):
        self.bg_frame = Image.open( os.path.join('images', 'backgroundbook.jpg'))
     
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo

        self.bg_panel.pack(fill='both', expand='yes')
        self.lgn_frame = Frame(self.window, bg='#1974d3', width=950, height=600)
        self.lgn_frame.place(x=250, y=150)

        self.txt = "Chào mừng độc giả"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Roboto', 25, "bold"), bg="#1974d3",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=340, y=30, width=310, height=50)

        self.side_image = Image.open(  os.path.join('images', 'huit.png'))

        width, height = self.side_image.size
        new_width = width // 3
        new_height = height //3
        self.side_image = self.side_image.resize((new_width, new_height))

        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=200)

        self.sign_in_image = Image.open( os.path.join('images', 'CHUONG.PNG'))
        width, height = self.sign_in_image.size
        new_width = width // 4
        new_height = height // 4
        self.sign_in_image = self.sign_in_image.resize((new_width, new_height))

        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)

        self.sign_in_image = Image.composite(self.sign_in_image, Image.new("RGBA", (new_width, new_height), 0), mask)

        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=100)

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#1974d3", fg="white", cursor="hand1",
                                   font=("Roboto", 15, "bold"))
        self.sign_in_label.place(x=600, y=240)

        self.sign_up_label = Label(self.lgn_frame, text="Sign Up", bg="#1974d3", fg="white", cursor="hand1",
                                   font=("Roboto", 15, "bold"))
        self.sign_up_label.place(x=690, y=240)

      

        self.sign_up_line = Canvas(self.lgn_frame, width=78, height=1, bg='#fff', highlightthickness=0, cursor="hand1")
        self.sign_up_line.place(x=690, y=268)

        self.sign_in_label.bind("<Button-1>", self.on_sign_in_click)
        self.sign_up_label.bind("<Button-1>", self.on_sign_up_click)   
    

        self.username_label = Label(self.lgn_frame, text="Username", bg="#1974d3", fg="#4f4e4d",
                                    font=("Roboto", 13, "bold"))
        self.username_label.place(x=550, y=335)
        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                    font=("Roboto ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=550, y=360, width=270)
        self.username_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#ffcc98", highlightthickness=0)
        self.username_line.place(x=550, y=385)

        self.email_label = Label(self.lgn_frame, text="Email", bg="#1974d3", fg="#4f4e4d",
                                    font=("Roboto", 13, "bold"))
        self.email_label.place(x=550, y=275)
        self.email_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                    font=("Roboto ", 12, "bold"), insertbackground='#6b6a69')
        self.email_entry.place(x=550, y=300, width=270)
        self.email_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#ffcc98", highlightthickness=0)
        self.email_line.place(x=550, y=325)

        self.password_label = Label(self.lgn_frame, text="Password", bg="#1974d3", fg="#4f4e4d",
                                    font=("Roboto", 13, "bold"))
        self.password_label.place(x=550, y=395)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#00BFFF",
                                    font=("Roboto", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=550, y=420, width=270)
        self.password_line = Canvas(self.lgn_frame, width=270, height=2.0, bg="#ffcc98", highlightthickness=0)
        self.password_line.place(x=550, y=445)
        self.birthday_label = Label(self.lgn_frame, text="Birthday", bg="#fff", fg="#4f4e4d",
                                    font=("Roboto", 13, "bold"))
        self.birthday_label.place(x=558, y=460)

        self.birthday_entry = DateEntry(self.lgn_frame, 
                                        date_pattern='dd/MM/yyyy',  # Set date format
                                        width=18,
                                        background='darkblue',
                                        foreground='white',
                                        borderwidth=3)
        self.birthday_entry.place(x=650, y=460) 

        self.signup_button = Button(self.lgn_frame, text='Sign Up', command=self.signup_function, font=("Roboto", 14, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#8865ff', fg='white')
        self.signup_button.place(x=535, y=500)

        self.back_to_login_button = Button(self.lgn_frame, text='Back to Login', command=self.back_to_login_function, font=("Roboto", 14, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#8865ff', fg='white')
        self.back_to_login_button.place(x=535, y=555)

        self.error_message_label = Label(self.lgn_frame, text='', bg="#1974d3", font=("Times", 24, "bold"))
        self.error_message_label.place(x=80, y=470)

    def back_to_login_function(self):
        self.is_login_mode=True
        self.display_all()

    def signup_function(self):
        new_username = self.username_entry.get()
        new_email = self.email_entry.get()
        new_password = self.password_entry.get()
        birthday = self.birthday_entry.get_date().strftime('%d/%m/%Y')  

        # Kiểm tra định dạng email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            self.error_message_label.config(text='Email không đúng định dạng.', fg='red')
            return
        if not new_username:
            self.error_message_label.config(text='Vui lòng nhập username.', fg='red')
            return
        if not new_password:
            self.error_message_label.config(text='Vui lòng nhập password.', fg='red')
            return
        # Kiểm tra xem username đã tồn tại chưa
        for user_info in user_data['users']:
            if user_info['username'] == new_username:
                self.error_message_label.config(text='Username đã tồn tại.', fg='red')
                return

        # Thêm người dùng mới vào dữ liệu JSON
        new_user = {
            "username": new_username,
            "password": new_password,
            "email": new_email,
            "type": "user",
            "image_path":    os.path.join('images', 'backgroundbook.jpg'),
            "birthday":birthday
        }
        user_data['users'].append(new_user)
        json_file_path = os.path.join('json_file', 'users_detail.json')
        with open(json_file_path, 'w') as f:
            json.dump(user_data, f)
        self.username_entry.delete(0, END)  # Delete all text in username entry
        self.email_entry.delete(0, END)    # Delete all text in email entry
        self.password_entry.delete(0, END)  # Delete all text in password entry
        self.error_message_label.config(text='')

        messagebox.showinfo("Success", "Đăng kí thành công") 

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="#1974d3"
                                  , borderwidth=0, background="#1974d3", cursor="hand2")
        self.hide_button.place(x=824, y=390)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#1974d3"
                                  , borderwidth=0, background="#1974d3", cursor="hand2")
        self.show_button.place(x=824, y=390)
        self.password_entry.config(show='*')


def run_login():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Add the 'page' and 'images' directories to the Python path
    sys.path.append(os.path.join(script_dir, 'page'))
    sys.path.append(os.path.join(script_dir, 'images'))
    run_login()