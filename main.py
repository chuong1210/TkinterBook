
import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
from tkinter import ttk

# Định nghĩa hàm để lấy dữ liệu từ Google Books API
def fetch_books(id):
    try:
        # Gửi yêu cầu GET đến Google Books API
        response = requests.get(f"https://project-gutenberg-api.p.rapidapi.com/books/{id}")
        response.raise_for_status()
        data = response.json()
        
        if "items" in data:
            books = data["items"]
            return books
        else:
            return []  
        
    except requests.RequestException as e:
        messagebox.showerror("Error", str(e))

# Chức năng hiển thị sách trên giao diện
def show_books():
    global books_info
    title = search_entry.get()
    if title:
        books_info = fetch_books(title)
        listbox.delete(0, tk.END)
        for book in books_info:
            listbox.insert(tk.END, book['volumeInfo'].get('title', 'No Title'))

# Hàm để hiển thị nội dung chi tiết của sách được chọn
def show_book_detail(event):
    # Lấy index của sách được chọn
    try:
        index = listbox.curselection()[0]
        book = books_info[index]
        
        book_details = f"Title: {book['volumeInfo'].get('title', 'No Title')}"
        book_details += f"\nAuthors: {', '.join(book['volumeInfo'].get('authors', []))}"
        book_details += f"\nPublished Date: {book['volumeInfo'].get('publishedDate', 'Unknown')}"
        
        messagebox.showinfo("Book Details", book_details)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a book from the list")

# Khởi tạo giao diện Tkinter
root = tk.Tk()
root.title("Book Finder")

search_entry = tk.Entry(root, width=50)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=show_books)
search_button.pack()

listbox = tk.Listbox(root, width=80, height=20)
listbox.pack()
listbox.bind('<<ListboxSelect>>', show_book_detail)

root.mainloop()