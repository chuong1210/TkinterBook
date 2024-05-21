
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
from bs4 import BeautifulSoup
from tkinter import scrolledtext
from gtts import gTTS
import os
import re


colorBg="f0f8ff"
with open('json_file\\users_detail.json') as f:
    user_data = json.load(f)


class adminPage:

    def __init__(self, master,user_info):
        self.window = master
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.title('Trang Admin')
        self.current_user = user_info
        self.first_chapter =1
        self.last_chapter=0
        
        self.create_header()
        self.create_sidebar()
        self.create_header_line()

        self.main_frame = None
        self.change_password_window = None 

        self.create_main_content()
        self.window.grid_rowconfigure(0, weight=0)  # Header không nên mở rộng khi cửa sổ được chỉnh kích thước
        self.window.grid_rowconfigure(1, weight=1)  # Nhưng main frame và sidebar nên mở rộng
        self.window.grid_columnconfigure(0, weight=0)  # Sidebar không nên mở rộng
        self.window.grid_columnconfigure(1, weight=1)  # Main frame nên mở rộng
        self.images = []
        self.camera_icon_pil = Image.open('images//camera-icon.png').resize((20, 20)) # Sử dụng PIL
        self.camera_icon = ImageTk.PhotoImage(self.camera_icon_pil)



    
    def exit(self):
        exit_command = messagebox.askyesno("Xác nhận","Bạn có muốn đăng xuất không")
        messagebox.CANCEL
        if exit_command > 0:
            self.window.destroy()
    def show_camera(self, event):
        avatar_copy = self.pil_image.copy()
        # Kết hợp ảnh camera lên ảnh avatar
        avatar_copy.paste(self.camera_icon_pil, (avatar_copy.width // 2 - self.camera_icon_pil.width // 2, avatar_copy.height // 2 - self.camera_icon_pil.height // 2), self.camera_icon_pil) # Đặt camera ở giữa avatar
        # Cập nhật Label cho avatar
        self.avatar_img = ImageTk.PhotoImage(avatar_copy) 
        self.avatar_label.config(image=self.avatar_img)
        self.avatar_label.image = self.avatar_img 
    # Hàm ẩn ảnh máy ảnh khi chuột rời đi
    def hide_camera(self, event):
        avatar_path = self.current_user['image_path']  # Lấy đường dẫn ảnh từ user_info
        try:
            self.pil_image = Image.open(avatar_path)
        except FileNotFoundError:
            # Sử dụng ảnh mặc định nếu không tìm thấy ảnh
            self.pil_image = Image.open('images\\CHUONG.png') 
    # Tải lại ảnh avatar
        self.pil_image = Image.open(avatar_path)
        width, height = self.pil_image.size
        new_width = width // 7
        new_height = height // 7
        self.pil_image = self.pil_image.resize((new_width, new_height))

            # Tạo hình tròn cho avatar
        mask = Image.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)
        self.pil_image = Image.composite(self.pil_image, Image.new("RGBA", (new_width, new_height), 0), mask)
        self.avatar_img = ImageTk.PhotoImage(self.pil_image) 

            # Cập nhật Label cho avatar
        self.avatar_label.config(image=self.avatar_img)
        self.avatar_label.image = self.avatar_img 
        print("sa")
    # Hàm thay đổi avatar
    def change_avatar(self, event):
        file_path = filedialog.askopenfilename(
            initialdir="/",
            title="Chọn ảnh đại diện",
            filetypes=(("Hình ảnh", "*.jpg *.jpeg *.png"), ("Tất cả tệp", "*.*"))
        )
        if file_path:
            # Cập nhật đường dẫn ảnh vào dữ liệu người dùng
            self.current_user['image_path'] = file_path

            # Cập nhật file JSON
            for user in user_data['users']:
                if user['username'] == self.current_user['username']:
                    user['image_path'] = file_path
            with open('json_file\\users_detail.json', 'w') as f:
                json.dump(user_data, f)

            # Tải lại ảnh avatar
            self.pil_image = Image.open(file_path)
            width, height = self.pil_image.size
            new_width = width // 7
            new_height = height // 7
            self.pil_image = self.pil_image.resize((new_width, new_height))

            # Tạo hình tròn cho avatar
            mask = Image.new("L", (new_width, new_height), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, new_width, new_height), fill=255)
            self.pil_image = Image.composite(self.pil_image, Image.new("RGBA", (new_width, new_height), 0), mask)
            self.avatar_img = ImageTk.PhotoImage(self.pil_image) 

            # Cập nhật Label cho avatar
            self.avatar_label.config(image=self.avatar_img)
            self.avatar_label.image = self.avatar_img 

    def create_sidebar(self):
        sidebar_frame = Frame(self.window, width=200, bg='#108690')
        #sidebar_frame.grid(row=1, column=0, sticky='ns')
        #sidebar_frame.pack(fill='y', side='left')
        sidebar_frame.place(relheight=1, relwidth=0.09)


        # tải và hiển thị avatar người dùng
        avatar_path = self.current_user['image_path']  # Lấy đường dẫn ảnh từ user_info
        try:
            self.pil_image = Image.open(avatar_path)
        except FileNotFoundError:
            # Sử dụng ảnh mặc định nếu không tìm thấy ảnh
            self.pil_image = Image.open('images\\CHUONG.png') 
                       # Ảnh máy ảnh
  
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
        self.avatar_label = Label(sidebar_frame, image=self.avatar_img, bg='#108690',cursor='hand1')
        self.avatar_label.image = self.avatar_img  # Lưu hình ảnh để tránh bị Python hủy
        self.avatar_label.pack(side='top', pady=10)
        self.avatar_label.bind("<Enter>", self.show_camera)
        self.avatar_label.bind("<Leave>", self.hide_camera)
        self.avatar_label.bind("<Button-1>", self.change_avatar)            # Bắt sự kiện hover và click

        settings_menu = Menu(self.window, tearoff=0)
        self.home_button = Button(sidebar_frame, fg='#fff', text="Trang chủ", command=self.create_main_content, bg='#108690', height=2,activebackground='#8865ff',activeforeground="#fff")
        self.home_button.pack(side='top', fill='x', pady=10)
        settings_menu.add_command(label="Đổi mật khẩu", command=self.replace_password,background='#108690')
        settings_menu.add_command(label="Xem thông tin tài khoản", command=self.view_account_info)

        self.settings_button_text = StringVar()
        self.settings_button_text.set('Cài đặt ▼') 
        sidebar_frame.grid_columnconfigure(0, weight=1)  # Cần thiết để các nút mở rộng khi cửa sổ được chỉnh kích thước

        settings_button = Button(sidebar_frame, fg='#fff',textvariable=self.settings_button_text, command=lambda: self.settings_menu_show_hide(settings_menu, settings_button),bg='#108690',height=2,activebackground='#8865ff',activeforeground="#fff")
        settings_button.pack(side='top', fill='x', pady=10)
        # user_management_button = Button(sidebar_frame, fg='#fff', text="Quản lý người dùng", command=self.manage_users,bg='#108690',height=2)
        # user_management_button.pack(side='top', fill='x', pady=10)
        # book_management_button = Button(sidebar_frame,  fg='#fff',text="Quản lý sách", command=self.manage_books,bg='#108690',height=2)
        # book_management_button.pack(side='top', fill='x', pady=10)
        # book_management_button = Button(sidebar_frame,  fg='#fff',text="Quản lý nhà xuất bản", command=self.manage_books,bg='#108690',height=2)
        # book_management_button.pack(side='top', fill='x', pady=10)
       
        manage_button = Button(sidebar_frame, fg='#fff', text="Quản lý", command=self.manage_options, bg='#108690', height=2, activebackground='#8865ff',activeforeground="#fff")
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
        greeting_text = f"Xin chào, { self.current_user['username']}"
        self.greeting_label = Label(header_frame, text=greeting_text, bg='#108690', fg='white', font=("Poppins SemiBold", 15, "bold"))
        self.greeting_label.place(x=990, y=38)

        logout_button = Button(header_frame, text='Logout', bg='#4cb5f5', font=("Poppins SemiBold", 13, "bold"), bd=0,
                                            fg='#fff',
                                        cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff',
                                       command=self.exit)
        logout_button.place(relx=0.88, rely=0.300, width=96, height=45)

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
        if self.change_password_window is not None and self.change_password_window.winfo_exists():
            # If the window already exists, just bring it to the front
            self.change_password_window.deiconify()
            self.change_password_window.lift()
            return
        self.change_password_window = Toplevel(self.window)  # Create as a child of adminPage
        window_width = 350
        window_height = 350
        s_width = self.change_password_window.winfo_screenwidth()
        s_height = self.change_password_window.winfo_screenheight()
        p_top = int(s_height / 4 - window_height / 4)
        p_right = int(s_width / 2 - window_width / 2)
        self.change_password_window.geometry(f'{window_width}x{window_height}+{p_right}+{p_top}')
        self.change_password_window.title('Đổi mật khẩu')
        self.change_password_window.iconbitmap('images\\changepw.ico')
        self.change_password_window.configure(background='#f8f8f8')
        self.change_password_window.resizable(0, 0)

        username_entry = Entry(self.change_password_window, fg="#a7a7a7", font=("arial semibold", 12), highlightthickness=2,cursor="hand2")
        username_entry.insert(0, self.current_user['username'])  # Set the default value
        username_entry.config(state='disabled')
        username_entry.place(x=40, y=30, width=256, height=34)
        username_lbel = Label(self.change_password_window, text='Tài khoản Username ', fg="#89898b", bg='#f8f8f8',
                         font=("arial", 11, 'bold'))
        username_lbel.place(x=40, y=0)

        old_password_entry = Entry(self.change_password_window, fg="#280659", font=("arial semibold", 12), show='•', highlightthickness=3)
        old_password_entry.place(x=40, y=110, width=256, height=34)
        old_password_entry.config(highlightbackground="black", highlightcolor="black")
        old_password_label = Label(self.change_password_window, text='Nhập lại Mật khẩu cũ', fg="#000", bg='#f8f8f8', font=("arial", 12, 'bold'))
        old_password_label.place(x=40, y=80)

        new_password_entry = Entry(self.change_password_window, fg="#280659", font=("arial semibold", 12), show='•', highlightthickness=3)
        new_password_entry.place(x=40, y=190, width=256, height=34)
        new_password_entry.config(highlightbackground="black", highlightcolor="black")
        new_password_label = Label(self.change_password_window, text='Mật khẩu mới', fg="#000", bg='#f8f8f8',
                                   font=("arial", 12, 'bold'))
        new_password_label.place(x=40, y=160)
      
        error_message_label = Label(self.change_password_window, text='', bg='#f8f8f8')
        error_message_label.place (x=40, y=230)
        update_pass = Button(self.change_password_window, fg='#f8f8f8',command=lambda: self.change_password_inFile(old_password_entry,new_password_entry,error_message_label), text='Cập nhật mật khẩu', bg='#1b87d2', font=("arial bold", 14),
                         cursor='hand2', activebackground='#000181')
        update_pass.place(x=40, y=255, width=256, height=50)
        

        def close_window():
            self.close_change_password_window()

            

        self.change_password_window.protocol("WM_DELETE_WINDOW", close_window)
    def close_change_password_window(self):
        # This method gets called when the change password window is closed
        self.change_password_window.withdraw()  # Hide the window instead of destroying it
        self.settings_button_text.set('Cài đặt ▼')  # Reset the button text
        self.change_password_window = None  # Reset the window reference
        

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
            with open('json_file\\users_detail.json', 'w') as f:
                json.dump(user_data, f)
            error_message_label.config(text='Mật khẩu được cập nhật thành công.', fg='green')
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
    def read_data(self,url):
 
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails

        soup = BeautifulSoup(response.content, 'html.parser')

        # paragraphs=data.find_all("p")
        #         for pa in paragraphs:
        #             print(pa.text)
        paragraphs = soup.find_all("p")
    
        scraped_text = "\n".join([p.get_text() for p in paragraphs])
        return scraped_text
    def get_chapter_range(self, book_info):
        # Bạn sẽ cần phương thức hoặc logic cụ thể để lấy chương đầu và cuối từ book_info hoặc một nguồn khác.
        # Ở đây tôi giả định chương đầu tiên và cuối cùng lưu trong book_info là 'first_chapter' và 'last_chapter'.
        first_chap = book_info.get('first_chapter', 1)  # Nếu không có thông tin, giả định là 1 bắt đầu từ chương đầu tiên.
        last_chap = book_info.get('chapter')  # Giả định bạn đã lấy được thông tin này từ một nơi nào đó.

        return (first_chap, last_chap)
    def change_chap(self, book_info, direction):
        content_url = book_info.get('content_url')
        current_chap_str = re.search(r"-(\d+)$", content_url)
        first_chap, last_chap = self.get_chapter_range(book_info) 
        self.last_chapter=int(last_chap)
        self.first_chapter = int(self.first_chapter)
        if current_chap_str:
            current_numberChap = int(current_chap_str.group(1))

            new_chap = self.first_chapter+ direction
            self.first_chapter=new_chap
            new_numberChap=current_numberChap+direction
            # Kiểm tra xem có phải là chương đầu tiên hoặc không còn chương tiếp theo
            if new_chap < 1:
                self.first_chapter=1
                new_numberChap=current_numberChap+1
                messagebox.showinfo("Thông báo", "Đã đến chương đầu tiên.")
                

                return
            elif new_chap >self.last_chapter:  # Giả sử bạn có hàm này để lấy số lượng chương cuối cùng
                messagebox.showinfo("Thông báo", "Đã đến chương cuối cùng.")
                self.first_chapter=book_info['chapter']

                new_numberChap=current_numberChap-1

                return
            print(new_chap)
            print(new_numberChap)
            # Cập nhật URL để cào chương mới
            new_content_url = re.sub(r"(\d+)$", str(new_numberChap), content_url)
            book_info["content_url"] = new_content_url

            # Cào và hiển thị nội dung chương mới
            self.show_book_content(book_info)
        else:
            messagebox.showerror("Lỗi", "URL không hợp lệ.")
    def show_book_content(self, book_info):

        self.clear_main_content()


        # Sử dụng một Text widget cho cả tiêu đề và nội dung
        content_text = Text(self.main_frame, wrap='word', font=("Helvetica Neue", 20),background="#eeeeee")
        
        # Insert the title into the Text widget
        content_text.insert('1.0', book_info['title'] + "\n", 'title')
        content_text.tag_configure('title', font=("Helvetica", 26), foreground="#fff", background="#00CDCD",justify="center",spacing1=10 ,spacing3=10)
        content_text.tag_add("center", "1.0", "end")
        button_frame = Frame(self.main_frame)
        button_frame.pack(side='top')

        # Nút Chap trước
        prev_chap_button = Button(button_frame, text="Chap trước", command=lambda: self.change_chap(book_info, -1))
        prev_chap_button.pack(side='left', padx=5, pady=5)

        # Nút Chap tiếp theo
        next_chap_button = Button(button_frame, text="Chap tiếp theo", command=lambda: self.change_chap(book_info, 1))
        next_chap_button.pack(side='left', padx=5, pady=5)
        content_url = book_info.get('content_url')

        if content_url:
            
            scraped_content = self.read_data(content_url)
            if scraped_content:
                # Thêm nội dung vào widget Text dưới tiêu đề
                content_text.insert('end', "\n" + scraped_content)
            else:
                content_text.insert('end', "\nError: Could not fetch book content.")
        else:
            content_text.insert('end', "\nError: Book content URL not found.")

        # Tạo Scrollbar và định cấu hình để nó hoạt động với widget Text
        scrollbar = Scrollbar(self.main_frame, command=content_text.yview)
        content_text['yscrollcommand'] = scrollbar.set

        # Đóng gói Scrollbar và để Text widget cuộn được
        scrollbar.pack(side='right', fill='y')
        content_text.pack(side='left', expand=True, fill='both')
        content_text.config(state='disabled')  # Disable editing of


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
        if self.window.winfo_exists():
            self.first_chapter=1
            self.last_chapter=book['chapter']
            BookDetailWindow(self.window, book, isOwner, self.show_book_content)
        else:
            # Show an error message if the adminPage window is closed
            messagebox.showerror("Error", "Cannot create BookDetailWindow. The parent window is closed.")
        # Close the book detail window when it is closed
    def manage_users(self):
        self.clear_main_content()
        user_columns = ("username", "password","type","email","image_path")
        self.user_table = ManageTable(self.main_frame, "json_file\\users_detail.json", "users", user_columns,"Độc gia",True)
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
        book_columns = ("title", "authors", "genre", "year", "pages","image_path","chapter","content_url")
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
            "username": "user1",
            "password": "password1",
            "type": "admin",
            "email": "user1@example.com", 
            "image_path": "images/publisher.png"
        })
    window.mainloop()

if __name__ == '__main__':
    page()