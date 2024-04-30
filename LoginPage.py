from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
from user import admin
from user.user import run_user
from user.admin import run_admin
from support_app import destroy_window
with open('json_file\\users_login.json') as f:
    user_data = json.load(f)

class LoginPage:
    def login_function(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
      
        for user_info in user_data['users']:
            if user_info['username'] == entered_username and user_info['password'] == entered_password:
                if user_info['type'] == 'admin':
                    new_window = Toplevel(self.window)
                    run_admin( new_window,user_info)
                    self.window.withdraw() 
                elif user_info['type'] == 'user':
                    new_window = Toplevel(self.window)
                    run_user( new_window,user_info)
                    self.window.withdraw() 
                else:
                    print("Unknown user type.")
                self.error_message_label.config(text='') 
                return
            self.error_message_label.config(text='Invalid username or password.', fg='red')
            print("Invalid username or password.")

    def __init__(self, window):
        self.window = window
        self.window.geometry('965x606+50+50')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Trang đăng nhập')
        self.window.iconbitmap('images//changepw.ico')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\backgroundbook.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo

        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#1974d3', width=950, height=600)
        self.lgn_frame.place(x=250, y=150)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Chào mừng độc giả"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('times new roman', 25, "bold"), bg="#1974d3",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=340, y=30, width=300, height=50)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\huit.png')
        width, height = self.side_image.size
        new_width = width // 3
        new_height = height //3
        self.side_image = self.side_image.resize((new_width, new_height))

# Tạo đối tượng PhotoImage từ hình ảnh đã thu nhỏ
        photo = ImageTk.PhotoImage(self.side_image)

# Tạo label để hiển thị hình ảnh thu nhỏ
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=200)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\CHUONG.png')
     

        width, height = self.sign_in_image.size
        new_width = width // 4
        new_height = height // 4
        self.sign_in_image = self.sign_in_image.resize((new_width, new_height))

# Tạo hình tròn bằng cách cắt ảnh
        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)

# Áp dụng mask để cắt ảnh thành hình tròn
        self.sign_in_image = Image.composite(self.sign_in_image, Image.new("RGBA", (new_width, new_height), 0), mask)

# Tạo đối tượng PhotoImage từ hình ảnh đã thu nhỏ
        photo = ImageTk.PhotoImage(self.sign_in_image)


# Tạo label để hiển thị hình ảnh thu nhỏ
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.sign_in_image_label.image = photo

# Đặt vị trí cho label
        self.sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#1974d3", fg="white",
                                    font=("times new roman", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#1974d3", fg="#4f4e4d",
                                    font=("times new roman", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#6b6a69",
                                    font=("times new roman ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#ffcc98", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
       
        self.login = Button(self.lgn_frame, text='Đăng nhập', command=self.login_function ,font=("times new roman", 14, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#8865ff', fg='white')
        self.login.place(x=580, y=450)
        self.error_message_label = Label(self.lgn_frame, text='', bg="#1974d3")
        self.error_message_label.place(x=580, y=427)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#1974d3", fg="#4f4e4d",
                                    font=("times new roman", 13, "bold"))
        self.password_label.place(x=550, y=363)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#1974d3", fg="#6b6a69",
                                    font=("times new roman", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.config(disabledbackground="#ffffff")
        self.password_entry.place(x=580, y=390, width=244)
        

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#ffcc98", highlightthickness=0)
        self.password_line.place(x=550, y=416)
       
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#1974d3')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=388)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\open_eye.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\close_eye.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#1974d3"
                                  , borderwidth=0, background="#1974d3", cursor="hand2")
        self.show_button.place(x=824, y=390)



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

    def update_show_password(self, *args):
        self.password_entry.config(show=self.show_password.get())
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()