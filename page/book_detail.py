
from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
import requests
from io import BytesIO
import threading
from time import sleep
class BookDetailWindow:
    def __init__(self, master, book_info):
        self.window = Toplevel(master) # Tạo một cửa sổ top-level mới
        self.window.title('Thông tin chi tiết sách')

        Label(self.window, text="Tiêu đề: "+book_info['title']).pack()
        Label(self.window, text="Tác giả: "+', '.join(book_info['authors'])).pack()
        Label(self.window, text="Mô tả: "+book_info['description']).pack()

        if 'imageLinks' in book_info:
            response = requests.get(book_info['imageLinks']['thumbnail'])
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

            cover_label = Label(self.window, image=img)
            cover_label.image = img  # Lưu hình ảnh để tránh bị Python hủy
            cover_label.pack()

        self.window.mainloop()