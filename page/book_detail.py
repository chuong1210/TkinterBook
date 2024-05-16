
from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
import requests
from io import BytesIO
from tkinter import messagebox

import threading
from time import sleep
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
        print(book_info)
        self.window = Toplevel(master) # Tạo một cửa sổ top-level mới
        self.window.title('Thông tin chi tiết sách')

        Label(self.window, text="Tiêu đề: "+book_info['title']).pack()
        Label(self.window, text="Tác giả: " + self.format_authors(book_info['authors'])).pack()

        Label(self.window, text="Mô tả: "+book_info['description']).pack()
        if 'publisher' in book_info:  # Chỉ hiển thị nếu có thông tin nhà xuất bản
            Label(self.window, text="Nhà xuất bản: " + book_info['publisher']).pack()

        if 'imageLinks' in book_info:
            response = requests.get(book_info['imageLinks']['thumbnail'])
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

            cover_label = Label(self.window, image=img)
            cover_label.image = img  # Lưu hình ảnh để tránh bị Python hủy
            cover_label.pack()

        # Nếu dữ liệu từ JSON, hiển thị nút đọc
        if is_Owner == 'json':
            read_button = Button(self.window, text="Đọc", command=lambda: self.open_read_page(book_info, on_read_callback))
            read_button.pack()

        self.window.mainloop()
    def open_read_page(self, book_info, on_read_callback):
           read_confirm = messagebox.askyesno("Xác nhận", "Bạn có muốn đọc '" + book_info['title'] + "' không?")

           if read_confirm and on_read_callback:
               on_read_callback(book_info)
               self.window.destroy()  # Đóng cửa sổ chi tiết sau khi người dùng chọn Đọc

