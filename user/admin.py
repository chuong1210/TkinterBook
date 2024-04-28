from tkinter import  Label, Entry, OptionMenu, StringVar, PhotoImage, Frame
from PIL import ImageTk, Image as PLimage,ImageDraw,ImageOps
from tkinter import *
import os

class adminPage:
    def __init__(self,master):
        self.window = master
      
        cwd = os.getcwd()
        print(cwd+'wcs')
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))

        # tạo header frame
        header_frame = Frame(self.window, height=100, bg='#a0a0a0')
        header_frame.pack(fill='x')
# tải và hiển thị avatar người dùng
        self.pil_image = PLimage.open('images\\CHUONG.png')

        width, height = self.pil_image.size
        new_width = width // 8
        new_height = height // 8
        self.pil_image = self.pil_image.resize((new_width, new_height))
# Tạo hình tròn bằng cách cắt ảnh
        mask = PLimage.new("L", (new_width, new_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_width, new_height), fill=255)
# Áp dụng mask để cắt ảnh thành hình tròn
        self.pil_image = PLimage.composite(self.pil_image, PLimage.new("RGBA", (new_width, new_height), 0), mask)
# Tạo mặt nạ hình tròn để hình ảnh
        self.avatar_img = ImageTk.PhotoImage(self.pil_image)  
        avatar_label = Label(header_frame, image=self.avatar_img, bg='#a0a0a0')
        avatar_label.image = self.avatar_img  # Lưu hình ảnh để tránh bị Python hủy
        avatar_label.pack(side='left', padx=10,pady=10)

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

        sidebar_frame = Frame(self.window, width=200, bg='#a0a0a0')
        sidebar_frame.pack(fill='y', side='left')

        # tạo các nút để thêm các chức năng quản lý
        Button(sidebar_frame, text="Quản lý người dùng").pack(pady=10)
        Button(sidebar_frame, text="Quản lý sách").pack(pady=10)
        Button(sidebar_frame, text="Cài đặt").pack(pady=10)




        # label chào mừng
        Label(self.window, text="Đây là trang admin", font=("Helvetica", 40)).pack(expand=True)


def run_admin(window):
   # window = Tk()
    adminPage(window)




def page():
    window = Tk()
    adminPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()