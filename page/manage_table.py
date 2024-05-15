from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from PIL import ImageTk, Image,ImageDraw
from tkinter import filedialog

class ManageTable:
    def __init__(self, master, data_file, data_key, columns, table_title,allow_images=False):
        self.master = master
        self.data_file = data_file
        self.data_key = data_key
        self.columns = columns
        self.data = []
        self.table_title = table_title
        self.selected_index = None  # Initialize selected_index
        self.allow_images = allow_images



        # Create frames for edit card and table
        self.edit_card_frame = LabelFrame(self.master, bg='#ffffff', bd='1.4',relief="groove")
        self.edit_card_frame.place(x=20, y=80, width=2, height=2)

        # Pack frames side by side
        self.edit_card_frame.pack(side=LEFT, fill="both", expand=True, padx=20, pady=20)
        



        self.create_edit_card()
        self.create_table()
        self.load_data()
        self.populate_table()

    def create_table(self):
        title_frame = Frame(self.master)
        title_frame.pack(fill=X)

        # Thêm label tiêu đề
        title_label = Label(title_frame, text=f"Đây là quản lý {self.table_title}", font=("Arial", 14,'bold'))
        title_label.pack(pady=10)
        # Tạo frame cho table
        self.table_frame = Frame(self.master)
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Tạo Treeview
        self.table = ttk.Treeview(self.table_frame, columns=self.columns, show="headings")

        # Đặt tiêu đề cho các cột
        for col in self.columns:
            self.table.heading(col, text=col)

        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(self.table_frame, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.table.pack(fill=BOTH, expand=True)
        self.edit_card_frame = Frame(self.master, bd=1, relief="solid")
        self.edit_card_frame.pack(padx=20, pady=20)
    def update_book_image(self):
        if not self.table.selection():
            messagebox.showerror("Error", "Please select a book to update.")
            return

        selected_iid = self.table.selection()[0]
        self.selected_index = self.table.index(selected_iid)
        filepath = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.gif')])
        
        if filepath:
            # Update book's image path
            self.data[self.selected_index]['image_path'] = filepath

            # Update JSON and table
            self.save_data()
            self.populate_table()

            # Optionally, update the image shown in the UI
            self.show_preview_image(filepath)
    def show_preview_image(self, filepath):
        # Assuming `self.img_label` is a Label widget where the image should be displayed
        img = Image.open(filepath)
        img.thumbnail((100, 100))  # Resize the image to fit the label
        photo = ImageTk.PhotoImage(img)
        self.img_label.config(image=photo)
        self.img_label.image = photo  # Keep a reference to avoid garbage collection
    def show_book_image(self, image_path):
        # Thử tải hình ảnh từ đường dẫn cung cấp
        try:
            with Image.open(image_path) as img:
                # Định dạng lại hình ảnh cho phù hợp
                img.thumbnail((100, 100))  # ví dụ: hình ảnh sẽ được thu nhỏ để phù hợp với kích thước mong muốn
                img = ImageTk.PhotoImage(img)
                self.img_label.config(image=img)
                self.img_label.image = img  # Giữ tham chiếu đến hình ảnh
        except Exception as e:
            print(e)
            # Nếu có lỗi khi tải ảnh, có thể hiển thị ảnh mặc định hoặc thông báo lỗi
            self.img_label.config(image='')
            self.img_label.image = None
    def select_image(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("PNG files", "*.png"),
                                                          ("JPEG files", "*.jpg;*.jpeg"),
                                                          ("All image files", "*.png;*.jpg;*.jpeg;*.gif"),
                                                          ("All files", "*.*")))
        if file_path:
            # Update the entry to the selected path
            self.img_path_entry.delete(0, END)
            self.img_path_entry.insert(0, file_path)
            
            # Optionally, update the preview image
            self.show_preview_image(file_path)
    def load_data(self):
        # Đọc dữ liệu từ file JSON
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.data = data[self.data_key]
        except FileNotFoundError:
            print(f"Không tìm thấy file {self.data_file}.")
        except json.JSONDecodeError:
            print(f"Lỗi định dạng JSON trong file {self.data_file}.")

    def populate_table(self):
        # Xóa nội dung hiện tại của table
        self.table.delete(*self.table.get_children())

        # Thêm dữ liệu vào table
        for item in self.data:
            values = [item[col] for col in self.columns]
            self.table.insert("", END, values=values, tags=("clickable",))

        self.table.tag_bind("clickable", "<ButtonRelease-1>", self.on_row_click)    # ... (code hiện tại) ...
    def on_row_click(self, event):
        # Lấy ra item ID của dòng đã chạm
        iid = self.table.identify_row(event.y)
        if iid:
            # Lấy index của dữ liệu từ Treeview
            self.selected_index = self.table.index(iid)
            self.table.selection_set(iid)

            # Lấy ra dữ liệu của sách được chọn
            selected_data = self.data[self.selected_index]

            # Cập nhật các entry với thông tin từ bản ghi được chọn
            for i, col in enumerate(self.columns):
                self.entries[i].delete(0, END)
                self.entries[i].insert(0, selected_data[col])

            # Nếu chức năng hình ảnh được cho phép và bản ghi có 'image_path'
            if self.allow_images and 'image_path' in selected_data:
                # Gọi hàm hiển thị hình ảnh của sách
                self.show_book_image(selected_data['image_path'])
    
    def clear_edit_card(self):
        for entry in self.entries:
            entry.delete(0, END)
    def add_record(self):
        # Get data from entry fields
        new_data = [entry.get() for entry in self.entries]

        # Add new record to self.data
        if self.allow_images:
            # Get the image path from the entry and add it to the new_data dictionary
            image_path = self.img_path_entry.get()
            self.data.append({**dict(zip(self.columns, new_data)), 'image_path': image_path})
        else:
            self.data.append(dict(zip(self.columns, new_data)))

        # Save to JSON file
        self.save_data()

        # Update table
        self.populate_table()
        self.clear_edit_card()

    def update_record(self):
        try:
            selected_iid = self.table.selection()[0]
            self.selected_index = self.table.index(selected_iid)
            new_data = [entry.get() for entry in self.entries]
            print(new_data)

            # Always include the image path if allow_images is True,
            # regardless of whether the book previously had an image
    
            self.data[self.selected_index] = dict(zip(self.columns, new_data))

            self.save_data()
            self.populate_table()
            self.clear_edit_card()

        except IndexError:
            messagebox.showwarning("Warning", "No item selected. Please select an item first.")
            return
    def delete_record(self):
        if not self.table.selection():
            messagebox.showerror("Error", "Please select a row to delete.")
            return

        selected_iid = self.table.selection()[0]
        self.selected_index = self.table.index(selected_iid)
        print(self.selected_index,"select")



        del self.data[self.selected_index]
        self.selected_index = None 


        self.save_data()

        self.populate_table()  # Refresh the Treeview

        children = self.table.get_children()
        if not children:  # Check if the table is now empty
            print(123,"eat child")

            self.selected_index = None  # Reset index
        if children:
            try:
                next_iid = self.table.next(selected_iid)
                # Select the next item if it exists
                if next_iid:
                    self.table.selection_set(next_iid)
                    self.selected_index = self.table.index(next_iid)
            except TclError:
                # Handle case when there are no more items after the deleted one
                self.selected_index = None
            # Handle empty table case (e.g., reset index or display message)
        # Option 2: Reset index (if you don't need to maintain selection)
        # self.selected_index = None
        
    def create_edit_card(self):
        # self.edit_card_frame = Frame(self.master, bd=1, relief="solid")
        # self.edit_card_frame.pack(padx=20, pady=20)
        # Các label và entry cho từng trường thông tin
        yCard=0.249
        self.labels = []
        self.entries = []
        for i, col in enumerate(self.columns):
            label = Label(self.edit_card_frame, text=col)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w") # Align label to the west
            self.labels.append(label)
            entry = Entry(self.edit_card_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        if self.allow_images:
            self.img_path_entry = self.entries[self.columns.index('image_path')]

            self.choose_img_button = Button(self.edit_card_frame, text='Choose Image', command=self.select_image, bg='#4cb5f5',font=("Poppins SemiBold", 13, "bold"), bd=0,
                                            fg='#fff',
                                        cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff')
            self.choose_img_button.grid(row=len(self.columns), column=0, columnspan=2, padx=5, pady=5, sticky="ew") 

            # Add the preview image label
            self.img_label = Label(self.edit_card_frame)
            self.img_label.grid(row=len(self.columns)+1, column=0, columnspan=2, pady=5)

        # Action buttons
        self.button4 = Button(self.edit_card_frame, text="Add", command=self.add_record,
                              bg='#4cb5f5', font=("Poppins SemiBold", 10, "bold"), bd=0,
                              fg='#fff', cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff')
        self.button4.grid(row=len(self.columns)+2, column=0, padx=5, pady=5, sticky="ew")

        self.button3 = Button(self.edit_card_frame, text="Delete", command=self.delete_record,
                              bg='#4cb5f5', font=("Poppins SemiBold", 10, "bold"), bd=0,
                              fg='#fff', cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff')
        self.button3.grid(row=len(self.columns)+2, column=1, padx=5, pady=5, sticky="ew")

        self.button5 = Button(self.edit_card_frame, text="Update", command=self.update_record,
                              bg='#4cb5f5', font=("Poppins SemiBold", 10, "bold"), bd=0,
                              fg='#fff', cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff')
        self.button5.grid(row=len(self.columns)+3, column=0, padx=5, pady=5, sticky="ew")

        self.button6 = Button(self.edit_card_frame, text="Clear", command=self.clear_edit_card,
                              bg='#4cb5f5', font=("Poppins SemiBold", 10, "bold"), bd=0,
                              fg='#fff', cursor='hand2', activebackground='#4cb5f5', activeforeground='#ffffff')
        self.button6.grid(row=len(self.columns)+3, column=1, padx=5, pady=5, sticky="ew")    
    # def save_data(self):
        
    #     if self.selected_index is None:
    #         print(self.data,"data")
    #         with open(self.data_file, 'w', encoding='utf-8') as f:
    #             json.dump({self.data_key: self.data}, f)


    #         self.populate_table()
    #         self.clear_edit_card()

    #         return

    #     new_data = [entry.get() for entry in self.entries]
        
    #     print(self.selected_index,"index")
    #     self.data[self.selected_index] = dict(zip(self.columns, new_data))
    #     print(self.data,"data")

    #     with open(self.data_file, 'w', encoding='utf-8') as f:
    #         json.dump({self.data_key: self.data}, f)


    #     self.populate_table()
    #     self.clear_edit_card()
    def save_data(self):
        # Always write the current state of data to file, regardless of whether it's an update or delete
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump({self.data_key: self.data}, f)
        
        # If an update is performed, retrieve the updated data and apply it
        if self.selected_index is not None:
            updated_data = [entry.get() for entry in self.entries]
            self.data[self.selected_index] = dict(zip(self.columns, updated_data))
            
            # After updating the internal data structure, save to file to persist changes
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump({self.data_key: self.data}, f)

        # Refresh the view to reflect changes
        self.populate_table()
        self.clear_edit_card()
# Liên kết sự kiện click vào dòng