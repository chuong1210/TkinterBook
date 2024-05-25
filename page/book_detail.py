
from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
import requests
from io import BytesIO
from tkinter import messagebox

import threading
from time import sleep
from bs4 import BeautifulSoup


class BookDetailWindow:
    @staticmethod
    def format_authors(authors):
        # Nếu authors là một list, nối các tác giả lại bằng dấu phẩy
        if isinstance(authors, list):
            return ', '.join(authors)
        # Nếu author là một string, trả về lập tức
        elif isinstance(authors, str):
            return authors
        # Trả về rỗng nếu authors không phải list cũng không phải string
        else:
            return ""
    def __init__(self, master, book_info,is_Owner,on_read_callback=None):
        if not master.winfo_exists(): 
            # If the master is destroyed, show an error message 
            messagebox.showerror("Error", "Cannot create BookDetailWindow. The parent window is closed.")
            return  
        self.window = Toplevel(master)  # Create as Toplevel of the main window
        self.window.title('Thông tin chi tiết sách')
        self.window.geometry("400x400")  # Cài đặt kích thước cửa sổ
        window_width = 350
        window_height = 400 #Tăng kích thước cửa sổ
        s_width = self.window.winfo_screenwidth()
        s_height = self.window.winfo_screenheight()
        p_top = int(s_height / 4 - window_height / 4)
        p_right = int(s_width / 2 - window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{p_right}+{p_top}')

        # Đổi màu nền cho cửa sổ
        self.window.configure(bg="#e6f2ff")
        Label(self.window, text="Tiêu đề: "+book_info['title'], bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)
        Label(self.window, text="Tác giả: " + self.format_authors(book_info['authors']), bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)

        if 'description' in book_info:  # Chỉ hiển thị nếu có thông tin nhà xuất bản
            Label(self.window, text="Mô tả: "+book_info['description'], bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)
        if 'publisher' in book_info:  # Chỉ hiển thị nếu có thông tin nhà xuất bản
            Label(self.window, text="Nhà xuất bản: " + book_info['publisher'], bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)

        if 'imageLinks' in book_info:
            response = requests.get(book_info['imageLinks']['thumbnail'])
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

            cover_label = Label(self.window, image=img)
            cover_label.image = img  # Lưu hình ảnh để tránh bị Python hủy
            cover_label.pack()
        if 'publisher' in book_info:
            Label(self.window, text="Nhà xuất bản: " + book_info['publisher'] ,bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)
        if 'genre' in book_info:
            Label(self.window, text="Thể loại: " + book_info['genre'], bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)
        if 'year' in book_info:
            Label(self.window, text="Năm xuất bản: " + book_info['year'], bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)
        if 'pages' in book_info:
            Label(self.window, text="Số trang: " + book_info['pages'], bg='#e6f2ff', font=("arial", 14,"bold")).pack(pady=10)

        if 'image_path' in book_info:
            try:
                img = ImageTk.PhotoImage(Image.open(book_info['image_path']).resize((100, 100)))

                cover_label = Label(self.window, image=img)
                cover_label.image = img  # Lưu hình ảnh để tránh bị Python hủy
                cover_label.pack()
            except FileNotFoundError:
                # Xử lý trường hợp file ảnh không tồn tại
                pass
        # Nếu dữ liệu từ JSON, hiển thị nút đọc
        if is_Owner == 'json':
            read_button = Button(self.window, text="Đọc", command=lambda: self.open_read_page(book_info, on_read_callback),font=("Poppins SemiBold", 13, "bold"), bd=0,
                                            fg='#fff',width=20, height=2,
                                        cursor='hand2', activebackground='#E6E6FA', activeforeground='#6495ED',bg='#6495ED')
            read_button.pack(side='bottom', pady=10,padx=10)

        

 

        self.window.mainloop()
    def open_read_page(self, book_info, on_read_callback):
           read_confirm = messagebox.askyesno("Xác nhận", "Bạn có muốn đọc '" + book_info['title'] + "' không?")

           if read_confirm and on_read_callback:
               self.window.destroy()  # Đóng cửa sổ chi tiết sau khi người dùng chọn Đọc
               on_read_callback(book_info)
             

