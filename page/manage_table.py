from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox

class ManageTable:
    def __init__(self, master, data_file, data_key, columns, table_title):
        self.master = master
        self.data_file = data_file
        self.data_key = data_key
        self.columns = columns
        self.data = []
        self.table_title = table_title
        self.selected_index = None  # Initialize selected_index


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
        # Lấy index của dòng được chọn
        selected_iid = self.table.identify_row(event.y)
        if selected_iid:
            # Lấy dữ liệu của dòng
            item = self.table.item(selected_iid)
            values = item['values']

            # Tạo card chỉnh sửa (bạn cần tự hoàn thiện phần này)
            for i, value in enumerate(values):
                self.entries[i].delete(0, END)
                self.entries[i].insert(0, value)
    
    def clear_edit_card(self):
        for entry in self.entries:
            entry.delete(0, END)
    def add_record(self):
        # Get data from entry fields
        new_data = [entry.get() for entry in self.entries]

        # Add new record to self.data
        self.data.append(dict(zip(self.columns, new_data)))

        # Save to JSON file
        self.save_data()

        # Update table
        self.populate_table()
        self.clear_edit_card()

    def update_record(self):
        # Get selected index
        selected_iid = self.table.selection()[0]
        self.selected_index = self.table.index(selected_iid)

        # Get updated data from entry fields
        new_data = [entry.get() for entry in self.entries]

        # Update record in self.data
        self.data[self.selected_index] = dict(zip(self.columns, new_data))

        # Save to JSON file
        self.save_data()

        # Update table
        self.populate_table()
        self.clear_edit_card()
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
        self.labels = []
        self.entries = []
        for i, col in enumerate(self.columns):
            label = Label(self.edit_card_frame, text=col)
            label.grid(row=i, column=0, padx=5, pady=5)
            self.labels.append(label)
            entry = Entry(self.edit_card_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        # Nút Lưu và Hủy

        self.button3 = Button(self.edit_card_frame)
        self.button3.place(relx=0.539, rely=0.249, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#4cb5f5")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#4cb5f5")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Delete""")
        self.button3.configure(command=self.delete_record)

        self.button4 = Button(self.edit_card_frame)
        self.button4.place(relx=0.059, rely=0.249, width=84, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#4cb5f5")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#4cb5f5")
        self.button4.configure(font="-family {Poppins SemiBold} -size 10")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Add""")
        self.button4.configure(command=self.add_record)

        self.button5 = Button(self.edit_card_frame)
        self.button5.place(relx=0.059, rely=0.329, width=86, height=25)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#4cb5f5")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#4cb5f5")
        self.button5.configure(font="-family {Poppins SemiBold} -size 10")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Update""")
        self.button5.configure(command=self.update_record)

        self.button6 = Button(self.edit_card_frame)
        self.button6.place(relx=0.539, rely=0.329, width=86, height=25)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#4cb5f5")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#4cb5f5")
        self.button6.configure(font="-family {Poppins SemiBold} -size 10")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Clear""")
        self.button6.configure(command=self.clear_edit_card)
    
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