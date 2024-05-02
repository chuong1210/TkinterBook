
from tkinter import *
from PIL import ImageTk, Image,ImageDraw
import json
from tkinter import ttk
import requests
from io import BytesIO
#from admin import 
from tkinter import messagebox

import threading
from time import sleep        
import os
class Manage:
            def __init__(self, master):
                self.master = master

                # Window Size and Placement
                master.rowconfigure(0, weight=1)
                master.columnconfigure(0, weight=1)
                screen_width = master.winfo_screenwidth()
                screen_height = master.winfo_height()
                app_width = 1300
                app_height = 690
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 160) - (app_height / 160)
                master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

                master.title("Book system")
                book_id = StringVar()
                title = StringVar()
                author = StringVar()
                genre = StringVar()
                year = StringVar()
                pages = StringVar()
                file_path = StringVar()
                image_path = StringVar()
                description = StringVar()

                # window Icon

                # Navigating through windows
                product_page = Frame(master)
                purchase_page = Frame(master)

                for frame in (product_page, purchase_page):
                    frame.grid(row=0, column=0, sticky='nsew')

                def show_frame(frame):
                    frame.tkraise()

                show_frame(product_page)

                # ======================================================================================
                # =================== HOME PAGE ========================================================
                # ======================================================================================

                product_page.grid_rowconfigure(0, weight=1)
                product_page.grid_columnconfigure(0, weight=1)                
                coverFrame = Frame(product_page, bg='#ffffff')
                

                topFrame = LabelFrame(coverFrame, bg='#f1f1f1', bd='2.4')
                topFrame.place(x=53, y=106, width=897, height=40)
                
                coverFrame_line = Canvas(coverFrame, width=1055, height=1.5, bg="#108cff", highlightthickness=0)
                coverFrame_line.place(x=0, y=130)



                coverFrame2 = Frame(product_page, bg='#ffffff')
                coverFrame2.place(x=0, y=0, width=290, height=830)


            

                def home():
                    win = Toplevel()
                    #admin.home(win)
                    master.withdraw()
                    win.deiconify()





          

               



 

            

                bookLabelManage = Label(coverFrame2, text='Quản lí Sách', font=("Arial", 13, "bold"), bg='#ffffff',
                                     fg='#ff6c38')
                bookLabelManage.place(x=80, y=0)

                coverFrame3 = LabelFrame(coverFrame2, bg='#ffffff', bd='2.4')
                coverFrame3.place(x=20, y=80, width=250, height=475)

                # book Image
                bookImage = Image.open('images\\close_eye.png')
                photo = ImageTk.PhotoImage(bookImage)
                bookImg = Label(coverFrame2, image=photo, bg='#ffffff')
                bookImg.image = photo
                bookImg.place(x=100, y=35)

                book = StringVar()
                type = StringVar()
                discount = StringVar()
                in_stock = StringVar()
                price = StringVar()
                book_id = StringVar()

                # ID NAME AND ENTRY
                # idLabel = Label(coverFrame3, text="#", bg='#ffffff', font=("Arial", 13, "bold"))
                # idLabel.place(x=5, y=41)

                # idName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                #                          font=("", 11, 'bold'), textvariable=book_id)
                # idName_entry.place(x=22, y=44, width=40, height=24)
                # idName_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                BookLb = Label(coverFrame3, text="Sách", bg='#ffffff', font=("Arial", 12, "bold"))
                BookLb.place(x=90, y=40)

                Book_nhap = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                         font=("", 12, 'bold'), textvariable=book)
                Book_nhap.place(x=10, y=70, width=225, height=34)
                Book_nhap.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                typeLb = Label(coverFrame3, text="Thể loại", bg='#ffffff', font=("Arial", 12, "bold"))
                typeLb.place(x=90, y=105)

                Type_nhap = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                       font=("", 12, 'bold'), textvariable=type)
                Type_nhap.place(x=10, y=135, width=225, height=34)
                Type_nhap.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                authorLb = Label(coverFrame3, text="DISCOUNT", bg='#ffffff', font=("Arial", 12, "bold"))
                authorLb.place(x=90, y=170)

                Author_nhap = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                         font=("", 12, 'bold'), textvariable=discount)
                Author_nhap.place(x=10, y=200, width=225, height=34)
                Author_nhap.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                inStockLabel = Label(coverFrame3, text="IN STOCK", bg='#ffffff', font=("Arial", 12, "bold"))
                inStockLabel.place(x=90, y=240)

                inStock_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                      font=("", 12, 'bold'), textvariable=in_stock)
                inStock_entry.place(x=10, y=270, width=225, height=34)
                inStock_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

                # priceLabel = Label(coverFrame3, text="PRICE", bg='#ffffff', font=("Arial", 12, "bold"))
                # priceLabel.place(x=90, y=310)

                # price_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                #                     font=("", 12, 'bold'), textvariable=price)
                # price_entry.place(x=80, y=340, width=100, height=34)
                # price_entry.config(highlightbackground="#6b6a69", highlightcolor="#ff6c38")

         

                def show_all():
                    if os.path.exists('books-detail.json'):
                        with open('books-detail.json', 'r') as file:
                            data = json.load(file)
                            if data:
                                book_tree.delete(*book_tree.get_children())
                                for book_id, book_details in data.items():
                                    book_tree.insert('', END, values=(book_id, *book_details.values()))
                            else:
                                messagebox.showerror("Failed", "No data to show")

                def book_info():
                    viewInfo = book_tree.focus()
                    book_data = book_tree.item(viewInfo)
                    row = book_data['values']
                    if row:
                        book_id.set(row[0])
                        title.set(row[1])
                        author.set(row[2])
                        genre.set(row[3])
                        year.set(row[4])
                        pages.set(row[5])
                        file_path.set(row[6])
                        image_path.set(row[7])
                        description.set(row[8])

                def add_book():
                    if book_id.get() == "":
                        messagebox.showerror("Failed", "Book ID can't be empty")
                    else:
                        new_book = {
                            "title": title.get(),
                            "author": author.get(),
                            "genre": genre.get(),
                            "year": year.get(),
                            "pages": pages.get(),
                            "file_path": file_path.get(),
                            "image_path": image_path.get(),
                            "description": description.get()
                        }
                        if os.path.exists('books-detail.json'):
                            with open('books-detail.json', 'r+') as file:
                                data = json.load(file)
                                data.append(new_book)
                                file.seek(0)
                                json.dump(data, file)
                        else:
                            with open('books-detail.json', 'w') as file:
                                json.dump([new_book], file)
                        show_all()
                        messagebox.showinfo("Success", "Book Record Added Successfully")
                def delete_records():
                    book = book_tree.selection()[0]
                    index = book_tree.item(book)['values'][0]
                    with open('books-detail.json', 'r+') as file:
                        data = json.load(file)
                        del data[index]
                        file.seek(0)
                        json.dump(data, file)
                        show_all()
                        messagebox.showinfo("Success", "Book Record Deleted Successfully")
                def update():
                    book = book_tree.selection()[0]
                    index = book_tree.item(book)['values'][0]
                    with open('books-detail.json', 'r+') as file:
                        data = json.load(file)
                        updated_book = {
                            "title": title.get(),
                            "author": author.get(),
                            "genre": genre.get(),
                            "year": year.get(),
                            "pages": pages.get(),
                            "file_path": file_path.get(),
                            "image_path": image_path.get(),
                            "description": description.get()
                        }
                        data[index] = updated_book
                        file.seek(0)
                        json.dump(data, file)
                    show_all()
                    messagebox.showinfo("Success", "Book Record Updated Successfully")

                self.button3 = Button(coverFrame3)
                self.button3.place(relx=0.539, rely=0.849, width=86, height=25)
                self.button3.configure(relief="flat")
                self.button3.configure(overrelief="flat")
                self.button3.configure(activebackground="#4cb5f5")
                self.button3.configure(cursor="hand2")
                self.button3.configure(foreground="#ffffff")
                self.button3.configure(background="#4cb5f5")
                self.button3.configure(font="-family {Poppins SemiBold} -size 10")
                self.button3.configure(borderwidth="0")
                self.button3.configure(text="""Delete""")
                self.button3.configure(command=delete_records)

                self.button4 = Button(coverFrame3)
                self.button4.place(relx=0.059, rely=0.849, width=84, height=25)
                self.button4.configure(relief="flat")
                self.button4.configure(overrelief="flat")
                self.button4.configure(activebackground="#4cb5f5")
                self.button4.configure(cursor="hand2")
                self.button4.configure(foreground="#ffffff")
                self.button4.configure(background="#4cb5f5")
                self.button4.configure(font="-family {Poppins SemiBold} -size 10")
                self.button4.configure(borderwidth="0")
                self.button4.configure(text="""Add""")
                self.button4.configure(command=add_book)

                self.button5 = Button(coverFrame3)
                self.button5.place(relx=0.059, rely=0.929, width=86, height=25)
                self.button5.configure(relief="flat")
                self.button5.configure(overrelief="flat")
                self.button5.configure(activebackground="#4cb5f5")
                self.button5.configure(cursor="hand2")
                self.button5.configure(foreground="#ffffff")
                self.button5.configure(background="#4cb5f5")
                self.button5.configure(font="-family {Poppins SemiBold} -size 10")
                self.button5.configure(borderwidth="0")
                self.button5.configure(text="""Update""")
                self.button5.configure(command=update)

                def clear_all():
                    book_id.set("")
                    book.set("")
                    type.set("")
                    discount.set("")
                    in_stock.set("")
                    price.set("")

                self.button6 = Button(coverFrame3)
                self.button6.place(relx=0.539, rely=0.929, width=86, height=25)
                self.button6.configure(relief="flat")
                self.button6.configure(overrelief="flat")
                self.button6.configure(activebackground="#4cb5f5")
                self.button6.configure(cursor="hand2")
                self.button6.configure(foreground="#ffffff")
                self.button6.configure(background="#4cb5f5")
                self.button6.configure(font="-family {Poppins SemiBold} -size 10")
                self.button6.configure(borderwidth="0")
                self.button6.configure(text="""Clear""")
                self.button6.configure(command=clear_all)
                

                style = ttk.Style()
                style.theme_use("clam")
                scrollbarx = Scrollbar(product_page, orient=HORIZONTAL)
                scrollbary = Scrollbar(product_page, orient=VERTICAL)
                book_tree = ttk.Treeview(coverFrame)
                book_tree.place(relx=0.0500, rely=0.228, width=896, height=410)
                book_tree.configure(
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
                )
                book_tree.configure(selectmode="extended")

                scrollbary.configure(command=book_tree.yview)
                scrollbarx.configure(command=book_tree.xview)

                scrollbary.place(relx=0.976, rely=0.323, width=25, height=412)
                scrollbarx.place(relx=0.242, rely=0.979, width=1015, height=15)

                book_tree.configure(
                    columns=(
                        "bookId",
                        "BookName",
                        "Type",
                        "Author",
                        "YearOfPublic",
                        "Publisher"
                    )
                )

                book_tree.heading("bookId", text="#", anchor=N)
                book_tree.heading("BookName", text="Sách", anchor=N)
                book_tree.heading("Type", text="Thể loại", anchor=N)
                book_tree.heading("Author", text="Tác giả", anchor=N)
                book_tree.heading("YearOfPublic", text="Năm xuất bản", anchor=N)
                book_tree.heading("Publisher", text="Nhà xuất bản", anchor=N)

                book_tree.column("#0", stretch=NO, minwidth=0, width=0)
                book_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=N)
                book_tree.column("#2", stretch=NO, minwidth=0, width=288, anchor=N)
                book_tree.column("#3", stretch=NO, minwidth=0, width=176, anchor=N)
                book_tree.column("#4", stretch=NO, minwidth=0, width=110, anchor=N)
                book_tree.column("#5", stretch=NO, minwidth=0, width=110, anchor=N)
                book_tree.column("#6", stretch=NO, minwidth=0, width=160, anchor=N)
                book_tree.bind("<ButtonRelease-1>", book_info)
                show_all()




                # ============ LINES ================================
                design_line = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line.place(x=53, y=168)

                design_line2 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line2.place(x=53, y=188)

                design_line3 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line3.place(x=53, y=208)

                design_line4 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line4.place(x=53, y=228)

                design_line5 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line5.place(x=53, y=248)

                design_line6 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line6.place(x=53, y=268)

                design_line7 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line7.place(x=53, y=288)

                design_line8 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line8.place(x=53, y=308)

                design_line9 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line9.place(x=53, y=328)

                design_line10 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line10.place(x=53, y=348)

                design_line11 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line11.place(x=53, y=368)

                design_line12 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line12.place(x=53, y=388)

                design_line13 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line13.place(x=53, y=408)

                design_line14 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line14.place(x=53, y=428)

                design_line15 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line15.place(x=53, y=448)

                design_line16 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line16.place(x=53, y=468)

                design_line17 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line17.place(x=53, y=488)

                design_line18 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line18.place(x=53, y=508)

                design_line19 = Canvas(coverFrame, width=895, height=1.2, bg="#e6e6e6", highlightthickness=0)
                design_line19.place(x=53, y=528)

root = Tk()
app = Manage(root)
root.mainloop()