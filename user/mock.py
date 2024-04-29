
from tkinter import *
from PIL import ImageTk, Image,ImageDraw


class adminPage:

    def __init__(self, master):
        self.window = master
        self.create_header()
        self.create_sidebar()
        self.create_main_content()

    def create_header(self):
# tạo header frame
        header_frame = Frame(self.window, height=100, bg='#a0a0a0')
        header_frame.pack(fill='x')
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


    def create_sidebar(self):
        sidebar_frame = Frame(self.window, width=200, bg='#a0a0a0')
        sidebar_frame.pack(fill='y', side='left')
        Button(sidebar_frame, text="Quản lý người dùng", command=self.manage_users).pack(pady=10)
        Button(sidebar_frame, text="Quản lý sách", command=self.manage_books).pack(pady=10)
        Button(sidebar_frame, text="Cài đặt").pack(pady=10)

    def create_main_content(self):
        self.main_frame = Frame(self.window)
        self.main_frame.pack(expand=True)
        self.home_page()

    def home_page(self):
        self.clear_main_content()
        Label(self.main_frame, text="Đây là trang chính", font=("Helvetica", 40)).pack(expand=True)

    def manage_users(self):
        self.clear_main_content()
        Label(self.main_frame, text="Trang quản lý người dùng", font=("Helvetica", 40)).pack(expand=True)

    def manage_books(self):
        self.clear_main_content()
        Label(self.main_frame, text="Trang quản lý sách", font=("Helvetica", 40)).pack(expand=True)

    def clear_main_content(self):
        for widget in self.main_frame.winfo_children():
                        widget.destroy()

def run_admin(window):
   # window = Tk()
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    adminPage(window)

def page():
    window = Tk()
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    adminPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()