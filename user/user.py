from tkinter import  Label, Entry, OptionMenu, StringVar, PhotoImage, Frame
from PIL import ImageTk, Image as PLimage,ImageDraw
from tkinter import *
import os

class UserPage:
    def __init__(self,master):
        self.window = master
      
        cwd = os.getcwd()
        print(cwd+'wcs')
        self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))

        # tạo header frame
        header_frame = Frame(self.window, height=100, bg='#a0a0a0')
        header_frame.pack(fill='x')
        # tải và hiển thị avatar người dùng
        pil_image = PLimage.open('images\\CHUONG.png')
        self.avatar_img = ImageTk.PhotoImage(pil_image)  
        avatar_label = Label(header_frame, image=self.avatar_img)
        avatar_label.image = self.avatar_img  # Lưu hình ảnh để tránh bị Python hủy
        avatar_label.pack(side='left', padx=10)




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

        # label chào mừng
        Label(self.window, text="Đây là trang user", font=("Helvetica", 40)).pack(expand=True)


def run_user(window):
   # window = Tk()
    UserPage(window)




def page():
    window = Tk()
    UserPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()