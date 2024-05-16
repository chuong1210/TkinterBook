
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image,ImageDraw
import json
import requests
from io import BytesIO
from book_detail import BookDetailWindow
from manage_table import ManageTable
import threading
from time import sleep
from tkinter import filedialog
colorBg="f0f8ff"
with open('json_file\\users_login.json') as f:
    user_data = json.load(f)


class adminPage:

    def __init__(self, master,user_info):
        self.window = master
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.title('Trang Admin')
        self.create_header()
        self.create_sidebar()
        self.create_header_line()

        self.main_frame = None

        self.create_main_content()
        self.current_user = user_info
        self.window.grid_rowconfigure(0, weight=0)  # Header không nên mở rộng khi cửa sổ được chỉnh kích thước
        self.window.grid_rowconfigure(1, weight=1)  # Nhưng main frame và sidebar nên mở rộng
        self.window.grid_columnconfigure(0, weight=0)  # Sidebar không nên mở rộng
        self.window.grid_columnconfigure(1, weight=1)  # Main frame nên mở rộng
        self.images = []
    
    def exit(self):
        exit_command = messagebox.askyesno("Xác nhận","Bạn có muốn đăng xuất không")
        messagebox.CANCEL
        if exit_command > 0:
            self.window.destroy()

    def create_sidebar(self):
        sidebar_frame = Frame(self.window, width=200, bg='#108690')
        #sidebar_frame.grid(row=1, column=0, sticky='ns')
        #sidebar_frame.pack(fill='y', side='left')
        sidebar_frame.place(relheight=1, relwidth=0.09)

        # tải và hiển thị avatar người dùng
        self.pil_image = Image.open('images\\CHUONG.png')

        width, height = self.pil_image.size
        new_width = width // 7
        new_height = height // 7
        self.pil_image = self.pil_image.resize((new_width, new_height))
# Tạo hình tròn bằng cách cắt ảnh
        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)
# Áp dụng mask để cắt ảnh thành hình tròn
        self.pil_image = Image.composite(self.pil_image, Image.new("RGBA", (new_width, new_height), 0), mask)
# Tạo mặt nạ hình tròn để hình ảnh
        self.avatar_img = ImageTk.PhotoImage(self.pil_image)  
        avatar_label = Label(sidebar_frame, image=self.avatar_img, bg='#108690',cursor='hand1')
        avatar_label.image = self.avatar_img  # Lưu hình ảnh để tránh bị Python hủy
        avatar_label.pack(side='top', pady=10)
        avatar_label.bind("<Button-1>", lambda e: self.create_main_content()) 
        settings_menu = Menu(self.window, tearoff=0)
        settings_menu.add_command(label="Đổi mật khẩu", command=self.replace_password,background='#108690')
        settings_menu.add_command(label="Xem thông tin tài khoản", command=self.view_account_info)

        self.settings_button_text = StringVar()
        self.settings_button_text.set('Cài đặt ▼') 
        sidebar_frame.grid_columnconfigure(0, weight=1)  # Cần thiết để các nút mở rộng khi cửa sổ được chỉnh kích thước

        settings_button = Button(sidebar_frame, fg='#fff',textvariable=self.settings_button_text, command=lambda: self.settings_menu_show_hide(settings_menu, settings_button),bg='#108690',height=2)
        settings_button.pack(side='top', fill='x', pady=10)
        # user_management_button = Button(sidebar_frame, fg='#fff', text="Quản lý người dùng", command=self.manage_users,bg='#108690',height=2)
        # user_management_button.pack(side='top', fill='x', pady=10)
        # book_management_button = Button(sidebar_frame,  fg='#fff',text="Quản lý sách", command=self.manage_books,bg='#108690',height=2)
        # book_management_button.pack(side='top', fill='x', pady=10)
        # book_management_button = Button(sidebar_frame,  fg='#fff',text="Quản lý nhà xuất bản", command=self.manage_books,bg='#108690',height=2)
        # book_management_button.pack(side='top', fill='x', pady=10)
        manage_button = Button(sidebar_frame, fg='#fff', text="Quản lý", command=self.manage_options, bg='#108690', height=2)
        manage_button.pack(side='top', fill='x', pady=10)

    def create_header(self):
# tạo header frame
        header_frame = Frame(self.window, height=200, bg='#108690')
        #header_frame.pack(fill='x')
        header_frame.place(rely=0, relx=0.09, relwidth=0.92, relheight=0.12)

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
        
        search_button = Button(header_frame, text="Tìm kiếm sách", 
                               command=lambda: self.threaded_function(book_search_entry))
        search_button.pack(side='left', padx=10)
        
        # self.button6 = Button(header_frame)
        # self.button6.place(relx=0.762, rely=0.300, width=96, height=45)
        # self.button6.configure(relief="flat")
        # self.button6.configure(overrelief="flat")
        # self.button6.configure(activebackground="#4cb5f5")
        # self.button6.configure(cursor="hand2")
        # self.button6.configure(foreground="#ffffff")
        # self.button6.configure(background="#4cb5f5")
        # self.button6.configure(font="-family {Poppins SemiBold} -size 10")
        # self.button6.configure(borderwidth="0")
        # self.button6.configure(text="""Đăng xuất""")
        # self.button6.configure(command=self.exit)

                       # ========== LOG OUT =======
        logout_button = Button(header_frame, text='Logout', bg='#4cb5f5', font=("Poppins SemiBold", 13, "bold"), bd=0,
                                            fg='#fff',
                                        cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff',
                                       command=self.exit)
        logout_button.place(relx=0.82, rely=0.300, width=96, height=45)

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
        if self.main_frame is not None and self.main_frame.winfo_exists():
            # Hủy bỏ nội dung cũ
            for widget in self.main_frame.winfo_children():
                widget.destroy()
        else:
            # Tạo main_frame mới nếu cần
            self.main_frame = Frame(self.window)
        self.main_frame.place(relx=0.093, rely=0.12, relwidth=0.912, relheight=0.845) 

        # creating background image widget
        self.bg_image = Image.open('images\\bgmain.jpg')
        self.bg_photo_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.main_frame, image=self.bg_photo_image)
        self.bg_label.place(x=0, y=0, relwidth=0.99, relheight=0.845)
        
        # creating overlying label widget
        self.home_label = Label(self.main_frame, text="Đây là trang admin", font=("Helvetica", 40), fg='#000')
        self.home_label.place(relx=0.5, rely=0.5, anchor='center') 
        self.display_all_books_json()

    # And bind this method to the window resize event:

    def home_page(self):
        self.clear_main_content()
        Label(self.main_frame, text="Đây là trang chính cho admin", font=("Helvetica", 40),relief='ridge').pack(expand=True)


    def manage_options(self):
        self.clear_main_content()

        user_picture = Image.open("images\\user-icon.png")
        user_picture = user_picture.resize((100, 100)) # giảm kích cỡ hình ảnh
        user_picture = ImageTk.PhotoImage(user_picture) 
        self.images.append(user_picture)
        Button(self.main_frame, image=self.images[-1], text='Quản lý người dùng',font='Verdana',
        compound=TOP, command=self.manage_users).place(relx=0.2, rely=0.3)

        book_picture = Image.open("images\\book.png")
        book_picture = book_picture.resize((100, 100)) # giảm kích cỡ hình ảnh
        book_picture = ImageTk.PhotoImage(book_picture)
        self.images.append(book_picture)
        Button(self.main_frame, image=self.images[-1], text='Quản lý sách',font='Verdana',
        compound=TOP, command=self.manage_books,height=200,width=200).place(relx=0.4, rely=0.3)


        publisher_picture = Image.open("images\\publisher.png")
        publisher_picture = publisher_picture.resize((100, 100)) # giảm kích cỡ hình ảnh
        publisher_picture = ImageTk.PhotoImage(publisher_picture)
        self.images.append(publisher_picture)
        Button(self.main_frame, image=self.images[-1], text='Quản lý nhà xuất bản',font='Verdana',
        compound=TOP, command=self.manage_publishers).place(relx=0.6, rely=0.3)

        # book_picture = PhotoImage(file="images\\book.png")
        # book_picture = book_picture.subsample(3, 3)  # giảm kích thước hình ảnh
        
    # def manage_users(self):
    #     self.clear_main_content()
    #     Label(self.main_frame, text="Trang quản lý người dùng", font=("Helvetica", 40)).pack(expand=True)
    # def manage_books(self):
    #     self.clear_main_content()
    #     Label(self.main_frame, text="Trang quản lý sách", font=("Helvetica", 40)).pack(expand=True)
    # def manage_publishers(self):
    #     self.clear_main_content()
    #     Label(self.main_frame, text="Trang quản lý nhà xuất bản", font=("Helvetica", 40)).pack(expand=True)


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
        username_entry = Entry(self.window, fg="#a7a7a7", font=("arial semibold", 12), highlightthickness=2,cursor="hand2")
        username_entry.insert(0, self.current_user['username'])  # Set the default value
        username_entry.config(state='disabled')
        username_entry.place(x=40, y=30, width=256, height=34)
        username_lbel = Label(self.window, text='Tài khoản Username ', fg="#89898b", bg='#f8f8f8',
                         font=("arial", 11, 'bold'))
        username_lbel.place(x=40, y=0)

    # ====  New Password ==================
        old_password_entry = Entry(self.window, fg="#280659", font=("arial semibold", 12), show='•', highlightthickness=3)
        old_password_entry.place(x=40, y=110, width=256, height=34)
        old_password_entry.config(highlightbackground="black", highlightcolor="black")
        old_password_label = Label(self.window, text='Nhập lại Mật khẩu cũ', fg="#000", bg='#f8f8f8', font=("arial", 12, 'bold'))
        old_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
        new_password_entry = Entry(self.window, fg="#280659", font=("arial semibold", 12), show='•', highlightthickness=3)
        new_password_entry.place(x=40, y=190, width=256, height=34)
        new_password_entry.config(highlightbackground="black", highlightcolor="black")
        new_password_label = Label(self.window, text='Mật khẩu mới', fg="#000", bg='#f8f8f8',
                                   font=("arial", 12, 'bold'))
        new_password_label.place(x=40, y=160)
      
        error_message_label = Label(self.window, text='', bg='#f8f8f8')
        error_message_label.place (x=40, y=230)
    # ======= Update password Button ============
        update_pass = Button(self.window, fg='#f8f8f8',command=lambda: self.change_password_inFile(old_password_entry,new_password_entry,error_message_label), text='Cập nhật mật khẩu', bg='#1b87d2', font=("arial bold", 14),
                         cursor='hand2', activebackground='#000181')
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

            # Lưu lại json file
            with open('json_file\\users_login.json', 'w') as f:
                json.dump(user_data, f)
            error_message_label.config(text='Mật khẩu được cập nhật thành công.', fg='green')
            print("sasasa")
        else:
            error_message_label.config(text='Mật khẩu cũ không đúng.', fg='red')     
 

    def create_header_line(self):
        # tạo một dòng phân cách giữa header và sidebar
        header_line = Frame(self.window, width=5, bg='black')
        header_line.place(relx=0.09, relheight=1)
    def threaded_function(self,book_entry):
        book_to_search = book_entry.get() 
        if book_to_search.strip() != '':
            response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + book_to_search)
            if response.status_code == 200:
                response_dict = response.json()
                for widget in self.main_frame.winfo_children(): # Clear all children widgets in main_frame
                    widget.destroy()

                row=0
                column=0
                for item in response_dict['items']:
                    book_info = item['volumeInfo']
                    book_frame = Frame(self.main_frame)
                    book_frame.grid(row=row, column=column, padx=10, pady=10)  # Use grid() instead of pack()
                

                    try:
                        img_url = book_info['imageLinks']['thumbnail']
                        img_response = requests.get(img_url)
                        img_data = img_response.content
                        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                    
                        cover_label = Label(book_frame, image=img,cursor='hand2')
                        cover_label.bind("<Button-1>", lambda e: self.show_book_detail(book_info,isOwner='api'))
                        cover_label.image = img
                        cover_label.pack()
                        title = book_info['title']
                        if len(title) > 40:  # Adjust value as needed
                            title = title[:37] + "..."
                            print(title,"dist")



                        info_label = Label(book_frame, text=f"Title: {title}\nAuthor: {', '.join(book_info['authors'])[:30]}", justify=LEFT)  # Cut authors if too long
                        info_label.pack()
                        column += 1
                        if column == 5:
                            column = 0
                            row += 1
                    except KeyError:
                        pass
            else:
                 self.display_all_books_json()

    def show_book_content(self, book_info):
        self.clear_main_content()
        title_label = Label(self.main_frame, text=book_info['title'], font=("Helvetica", 16))
        title_label.pack()
        # Tiếp theo là hiển thị nội dung của sách theo book_info['content'] hoặc tương tự
        content_label = Label(self.main_frame, text=book_info['description'], wraplength=self.main_frame.winfo_width())
        content_label.pack()
    def display_all_books_json(self):
    # Đọc file JSON
    
        with open('json_file\\books_detail.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    # Xóa nội dung hiện tại của main_frame
        self.clear_main_content()
    
        row = 0
        column = 0
        for book in data['books']:
            book_frame = Frame(self.main_frame)
            book_frame.grid(row=row, column=column, padx=10, pady=10)

    # Hiển thị hình ảnh sách nếu có
            if 'image_path' in book:
                img = Image.open(book['image_path'])

            # Resize hình ảnh
                max_height = 200  # Điều chỉnh giá trị này theo nhu cầu của bạn
                max_width = 200  # Điều chỉnh giá trị này theo nhu cầu của bạn
                width, height = img.size
                aspect_ratio = width / height

                if width > max_width:
                    width = max_width
                    height = width / aspect_ratio

                if height > max_height:
                    height = max_height
                    width = height * aspect_ratio

                img = img.resize((int(width), int(height)))

                photoImg =  ImageTk.PhotoImage(img)
                cover_label = Label(book_frame, image=photoImg,cursor='hand2')
                cover_label.image = photoImg  # Lưu hình ảnh để tránh bị Python hủy
                cover_label.pack()
                cover_label.bind("<Button-1>", lambda e, book=book: self.show_book_detail(book,isOwner='json'))


    # Hiển thị thông tin sách
            title = book['title']
            if len(title) > 40:  # Cắt tiêu đề nếu quá dài
                title = title[:37] + "..."
            author = book['authors']
            info_label = Label(book_frame, text=f"{title}\nAuthor: {author}", justify=LEFT)

            info_label.pack()

            column += 1
            if column == 5:
                column = 0
                row += 1
# def logout():
#     win = Toplevel()
#     win.withdraw()
#     win.deiconify()
#                 # ========== LOG OUT =======
# logout_button = Button(window, text='Logout', bg='#f6f6f9', font=("", 13, "bold"), bd=0,
#                                        fg='#7a7a7a',
#                                        cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
#                                        command=logout)
# logout_button.place(x=420, y=15)

    def show_book_detail(self, book,isOwner):
        BookDetailWindow(self.window, book,isOwner, self.show_book_content)
    def manage_users(self):
        self.clear_main_content()
        user_columns = ("username", "password","type")
        self.user_table = ManageTable(self.main_frame, "json_file\\users_login.json", "users", user_columns,"Độc gia")
        intermediate_frame = Frame(self.main_frame)
        intermediate_frame.pack(fill=BOTH, expand=True)

        # Corrected lines: replaced `book_table` with `user_table` here
        self.user_table.table_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.user_table.edit_card_frame.pack(side=LEFT, fill=Y)
    def select_image():
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                            filetypes=(("jpeg files", "*.jpg"),
                                                        ("all files", "*.*")))
        if file_path:
            # Do something with the selected file path
            print(file_path)

    def manage_books(self):
        self.clear_main_content()
        book_columns = ("title", "authors", "genre", "year", "pages","image_path")
        self.book_table = ManageTable(self.main_frame, "json_file\\books_detail.json", "books", book_columns,"Sách",allow_images=True)


        intermediate_frame = Frame(self.main_frame)
        intermediate_frame.pack(fill=BOTH, expand=True)

    # Đặt các frame con vào frame trung gian
        self.book_table.table_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        self.book_table.edit_card_frame.pack(side=LEFT, fill=Y)
        

    def manage_publishers(self):
        self.clear_main_content()
        publishers_columns = ("Pid", "name", "location", "founded_year", "website")
        self.publishers_table = ManageTable(self.main_frame, "json_file\\publishers.json", "publishers", publishers_columns,"Sách")
        # self.publishers_table.create_edit_card()

        intermediate_frame = Frame(self.main_frame)
        intermediate_frame.pack(fill=BOTH, expand=True)

    # Đặt các frame con vào frame trung gian
        self.publishers_table.table_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.publishers_table.edit_card_frame.pack(side=LEFT, fill=Y)        # Tương tự như manage_books, nhưng với file và data_key khác

 
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