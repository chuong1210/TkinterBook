import requests
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from io import BytesIO
import threading
from time import sleep
window = Tk()

load_image = Image.open("images\\loading-gif.gif")
load_image = load_image.resize((100, 100))
loading_img = ImageTk.PhotoImage(load_image)

def threaded_function():
    book_to_search = book_entry.get() 
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + book_to_search)

    if response.status_code == 200:
        response_dict = response.json()
        for widget in cover_frame.winfo_children():
            widget.destroy()

        for item in response_dict['items']:
            book_info = item['volumeInfo']
            book_frame = Frame(cover_frame)
            book_frame.pack(side=LEFT, padx=10, pady=10)

            try:
                img_url = book_info['imageLinks']['thumbnail']
                img_response = requests.get(img_url)
                img_data = img_response.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
                cover_label = Label(book_frame, image=img)
                cover_label.image = img
                cover_label.pack()

                info_label = Label(book_frame, text=f"Title: {book_info['title']}\nAuthor: {', '.join(book_info['authors'])}", justify=LEFT)
                info_label.pack()

            except KeyError:
                pass
    loading_label.config(image='')  # Remove loading image after task is finished

def get_book_info():
    # Show loading image while fetching book info
    loading_label.config(image=loading_img)

    # Create and start new thread to fetch book info
    thread = threading.Thread(target=threaded_function)
    thread.start()


book_entry = Entry(window)
book_entry.pack()

get_info_button = Button(window, text="Get Book Info", command=get_book_info)
get_info_button.pack()

# Label to display loading image
loading_label = Label(window)
loading_label.pack()

cover_canvas = Canvas(window)
cover_canvas.pack(fill=BOTH)

cover_scrollbar = ttk.Scrollbar(window, orient=HORIZONTAL, command=cover_canvas.xview)
cover_scrollbar.pack(side=BOTTOM, fill=X)

cover_canvas.configure(xscrollcommand=cover_scrollbar.set)
cover_frame = Frame(cover_canvas)
cover_canvas.create_window((0, 0), window=cover_frame, anchor="nw")

window.bind("<Configure>", lambda e: cover_canvas.configure(scrollregion=cover_canvas.bbox("all")))

window.mainloop()