
from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
colorBg="f0f8ff"
with open('json_file\\users_login.json') as f:
    user_data = json.load(f)

class adminPage:

    def __init__(self, master,user_info):
        self.window = master
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.create_header()
        self.create_sidebar()
        self.create_main_content()
        self.current_user = user_info
        self.window.grid_rowconfigure(0, weight=0)  # Header không nên mở rộng khi cửa sổ được chỉnh kích thước
        self.window.grid_rowconfigure(1, weight=1)  # Nhưng main frame và sidebar nên mở rộng
        self.window.grid_columnconfigure(0, weight=0)  # Sidebar không nên mở rộng
        self.window.grid_columnconfigure(1, weight=1)  # Main frame nên mở rộng

    def create_sidebar(self):
        sidebar_frame = Frame(self.window, width=200, bg='#a0a0a0')
        #sidebar_frame.grid(row=1, column=0, sticky='ns')
        sidebar_frame.pack(fill='y', side='left')
        # tải và hiển thị avatar người dùng
        self.pil_image = Image.open('images\\CHUONG.png')

        width, height = self.pil_image.size
        new_width = width // 8
        new_height = height // 8
        self.pil_image = self.pil_image.resize((new_width, new_height))
# Tạo hình tròn bằng cách cắt ảnh
        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)
# Áp dụng mask để cắt ảnh thành hình tròn
        self.pil_image = Image.composite(self.pil_image, Image.new("RGBA", (new_width, new_height), 0), mask)
# Tạo mặt nạ hình tròn để hình ảnh
        self.avatar_img = ImageTk.PhotoImage(self.pil_image)  
        avatar_label = Label(sidebar_frame, image=self.avatar_img, bg='#a0a0a0')
        avatar_label.image = self.avatar_img  # Lưu hình ảnh để tránh bị Python hủy
        avatar_label.pack(side='left', pady=10)
        settings_menu = Menu(self.window, tearoff=0)
        settings_menu.add_command(label="Đổi mật khẩu", command=self.replace_password)
        settings_menu.add_command(label="Xem thông tin tài khoản", command=self.view_account_info)

        self.settings_button_text = StringVar()
        self.settings_button_text.set('Cài đặt ▼') 
        sidebar_frame.grid_columnconfigure(0, weight=1)  # Cần thiết để các nút mở rộng khi cửa sổ được chỉnh kích thước

        settings_button = Button(sidebar_frame, textvariable=self.settings_button_text, command=lambda: self.settings_menu_show_hide(settings_menu, settings_button))
        settings_button.pack(pady=10)
        settings_button.grid(row=0, sticky='nsew')
        user_management_button = Button(sidebar_frame, text="Quản lý người dùng", command=self.manage_users)
        user_management_button.grid(row=1, sticky='nsew')
        book_management_button = Button(sidebar_frame, text="Quản lý sách", command=self.manage_books)
        book_management_button.grid(row=2, sticky='nsew')

    def create_header(self):
# tạo header frame
        header_frame = Frame(self.window, height=100, bg='#a0a0a0')
        header_frame.pack(fill='x')
        #header_frame.grid(row=0, column=0, columnspan=2, sticky='we')  # grid thay cho pack



        # tải và hiển thị avatar người dùng
        # self.avatar_img = PhotoImage(file='images\\CHUONG.png')  
        # avatar_label = Label(header_frame, image=self.avatar_img)
        # avatar_label.pack(side='left', padx=10)
        # tạo dropdown menu cho các lựa chọn thể loại sách
        book_genre_var = StringVar()
        book_genre_var.set('Chọn thể loại sách')  # giá trị mặc định
        book_genres = ['Tiểu thuyết', 'Văn học', 'Khoa học', 'Truyện tranh']  # thay đổi danh sách này theo nhu cầu của bạn
        book_genre_optionmenu = OptionMenu(header_frame, book_genre_var, *book_genres)
        book_genre_optionmenu.pack(side='left', padx=10)

        # tạo hộp nhập vào cho tìm kiếm sách
        book_search_entry = Entry(header_frame)
        book_search_entry.pack(side='left', padx=10)



    def view_account_info(self):
    # Code to view account info goes here
         pass



    def settings_menu_show_hide(self, settings_menu, settings_button):
     if self.settings_button_text.get() == 'Cài đặt ▼':
        x_off = settings_button.winfo_rootx()
        y_off = settings_button.winfo_rooty() + settings_button.winfo_height()
        settings_menu.post(x_off, y_off)
        self.settings_button_text.set('Cài đặt ▲')
     else:
        settings_menu.unpost()
        self.settings_button_text.set('Cài đặt ▼')

    def create_menu_setting(self,sidebar_frame):
        sidebar_frame.update()
        desired_width = int(sidebar_frame.winfo_width() * 0.8)
        settings_menu = Menu(self.window, tearoff=0)
        settings_menu.add_command(label="Đổi mật khẩu", command=self.change_password)
        settings_menu.add_command(label="Xem thông tin tài khoản", command=self.view_account_info)
        
        settings_button = Button(sidebar_frame, text="Cài đặt", 
                             command=lambda: settings_menu.post(sidebar_frame.winfo_rootx(), 
                                                                sidebar_frame.winfo_rooty()+130)) #+ sidebar_frame.winfo_height()-200))
        settings_button.pack(pady=10,padx=10)

    def create_main_content(self):
        self.main_frame = Frame(self.window)
        self.main_frame.pack(expand=True)
       # self.main_frame.grid(row=1, column=1, sticky='nsew')
        self.home_page()

    def home_page(self):
        self.clear_main_content()
        Label(self.main_frame, text="Đây là trang chính cho admin", font=("Helvetica", 40)).pack(expand=True)

    def manage_users(self):
        self.clear_main_content()
        Label(self.main_frame, text="Trang quản lý người dùng", font=("Helvetica", 40)).pack(expand=True)

    def manage_books(self):
        self.clear_main_content()
        Label(self.main_frame, text="Trang quản lý sách", font=("Helvetica", 40)).pack(expand=True)

    def clear_main_content(self):
        for widget in self.main_frame.winfo_children():
                        widget.destroy()
    def replace_password(self):
        self.window = Toplevel()
        window_width = 350
        window_height = 350
        s_width = self.window.winfo_screenwidth()
        s_height = self.window.winfo_screenheight()
        p_top = int(s_height / 4 - window_height / 4)
        p_right = int(s_width / 2 - window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{p_right}+{p_top}')
        self.window.title('Đổi mật khẩu')
        self.window.iconbitmap('images\\changepw.ico')
        self.window.configure(background='#f8f8f8')
        self.window.resizable(0, 0)

    # ====== Username ====================
        username_entry = Entry(self.window, fg="#a7a7a7", font=("arial semibold", 12), highlightthickness=2)
        username_entry.insert(0, self.current_user['username'])  # Set the default value
        username_entry.config(state='disabled')
        username_entry.place(x=40, y=30, width=256, height=34)
        username_lbel = Label(self.window, text='Tài khoản Username ', fg="#89898b", bg='#f8f8f8',
                         font=("arial", 11, 'bold'))
        username_lbel.place(x=40, y=0)

    # ====  New Password ==================
        old_password_entry = Entry(self.window, fg="#a7a7a7", font=("arial semibold", 12), show='•', highlightthickness=2)
        old_password_entry.place(x=40, y=110, width=256, height=34)
        old_password_entry.config(highlightbackground="black", highlightcolor="black")
        old_password_label = Label(self.window, text='Nhập lại Mật khẩu cũ', fg="#89898b", bg='#f8f8f8', font=("arial", 12, 'bold'))
        old_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
        new_password_entry = Entry(self.window, fg="#a7a7a7", font=("arial semibold", 12), show='•', highlightthickness=2)
        new_password_entry.place(x=40, y=190, width=256, height=34)
        new_password_entry.config(highlightbackground="black", highlightcolor="black")
        new_password_label = Label(self.window, text='Mật khẩu mới', fg="#89898b", bg='#f8f8f8',
                                   font=("arial", 12, 'bold'))
        new_password_label.place(x=40, y=160)
      
        error_message_label = Label(self.window, text='', bg='#f8f8f8')
        error_message_label.place (x=40, y=230)
    # ======= Update password Button ============
        update_pass = Button(self.window, fg='#f8f8f8',command=lambda: self.change_password_inFile(old_password_entry,new_password_entry,error_message_label), text='Cập nhật mật khẩu', bg='#1b87d2', font=("arial bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
        update_pass.place(x=40, y=255, width=256, height=50)
    def change_password_inFile(self, old_pass_entry, new_pass_entry,error_message_label):
        old_pass = old_pass_entry.get()
        new_pass = new_pass_entry.get()

        # kiểm tra mật khẩu cũ có khớp với mật khẩu hiện tại không
        if old_pass == self.current_user['password']:
            # cập nhật mật khẩu
            self.current_user['password'] = new_pass
            # cập nhật trong database
            for user in user_data['users']:
                if user['username'] == self.current_user['username']:
                    user['password'] = new_pass

            # Lưu lại database
            with open('json_file\\users_login.json', 'w') as f:
                json.dump(user_data, f)
            error_message_label.config(text='Mật khẩu được cập nhật thành công.', fg='green')
            print("sasasa")
        else:
            error_message_label.config(text='Mật khẩu cũ không đúng.', fg='red')     
 


def run_admin(window,user_info):
   # window = Tk()
    adminPage(window,user_info)

def page():
    window = Tk()
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    adminPage(window,   {
            "username": "user3",
            "password": "password3",
            "type": "admin"
        })
    window.mainloop()

if __name__ == '__main__':
    page()