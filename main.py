<<<<<<< HEAD
#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
from LoginPage import page

import time

w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    q=Tk()
    q.title('main window')
    q.mainloop()

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
name_thesis=Label(w, text='PROGRAMMED', fg='white', bg='#272727') #decorate it 
name_thesis.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
name_thesis.place(x=80,y=90)

Loading_lb=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
Loading_lb.configure(font=("Calibri", 11))
Loading_lb.place(x=10,y=215)

#making animation

img_load1=ImageTk.PhotoImage(Image.open('images\\c2.png'))
img_load2=ImageTk.PhotoImage(Image.open('images\\c1.png'))




for i in range(5): #5loops
    l1=Label(w, image=img_load1, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=img_load1, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=img_load1, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=img_load2, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=img_load1, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
page()
w.mainloop()
=======
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def fetch_data():
    # Lấy URL từ ô nhập liệu
    url="https://nhasachmienphi.com/doc-online/bach-da-hanh-311518"

    # Khởi tạo trình điều khiển Chrome
    service = Service(executable_path='path/to/chromedriver') # Thay thế bằng đường dẫn tới chromedriver của bạn
    driver = webdriver.Chrome(service=service)

    try:
        # Truy cập trang web
        driver.get(url)

        # Chờ cho JavaScript chạy hoàn tất (nếu cần)
        driver.implicitly_wait(10)  # Chờ tối đa 10 giây

        # Lấy HTML đầy đủ
        html = driver.page_source

        # Phân tích HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Tìm thẻ div có class 'content_p_al'
        content_div = soup.find('div', class_='content_p_al')
        
        # Tìm thẻ div có class 'chapter-c' bên trong content_div
        chapter_div = content_div.find('div', class_='chapter-c')

        # Tìm tất cả thẻ p trong thẻ div có class 'chapter-c'
        paragraphs = chapter_div.find_all('p')
        for paragraph in paragraphs:
            if paragraph.text.strip():
                print(paragraph.text)  # In nội dung của thẻ p

    finally:
        # Đóng trình duyệt
        driver.quit()

fetch_data()
>>>>>>> 435ee1b8166e1fc45fe410d0cdfe5b6ca50cf5a1
