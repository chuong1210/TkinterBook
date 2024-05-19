import tkinter as tk
from tkinter import Frame, Label, font, PhotoImage
from PIL import ImageTk, Image
from LoginPage import page  # Assuming this is your login page module
import time
from tkinter import Canvas

# Create the main window
w = tk.Tk()

# Window dimensions and positioning
width_of_window = 477
height_of_window = 280
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry(f"{width_of_window}x{height_of_window}+{int(x_coordinate)}+{int(y_coordinate)}")
w.overrideredirect(1)  # Hide title bar

# New window to open (not used in this example)
def new_win():
    q = tk.Tk()
    q.title('main window')
    q.mainloop()

# Background frame
Frame(w, width=487, height=270, bg='#9999FF').place(x=0, y=0)

# Thesis name label
name_thesis = Label(w, text='HUIT CHƯƠNG', fg='white', bg='#9999FF')
name_thesis.configure(font=("Game Of Squids", 26, "bold"))
name_thesis.place(x=120, y=90)

# Loading label
Loading_lb = Label(w, text='Loading...', fg='white', bg='#9999FF')
Loading_lb.configure(font=("Calibri", 14))
Loading_lb.place(x=30, y=215)

# Load images
img_load1 = ImageTk.PhotoImage(Image.open('images\\c2.png'))
img_load2 = ImageTk.PhotoImage(Image.open('images\\c1.png'))


# Function to create a label with border color matching the text
def create_image_label(image, x, y, bg_color='#9999FF'):
    canvas = Canvas(w, width=image.width(), height=image.height(), bg=bg_color)
    canvas.create_image(image.width() // 2, image.height() // 2, image=image)
    canvas.place(x=x-10, y=y)
    return canvas
# Animation function
def animate():
    # Create labels with border color matching the text
    l1 = create_image_label(img_load1, 180, 145, bg_color='#9999FF')
    l2 = create_image_label(img_load2, 200, 145, bg_color='#9999FF')
    l3 = create_image_label(img_load2, 220, 145, bg_color='#9999FF')
    l4 = create_image_label(img_load2, 240, 145, bg_color='#9999FF')
    l5 = create_image_label(img_load2, 260, 145, bg_color='#9999FF')


    w.update_idletasks()
    time.sleep(0.5)

    l1 = create_image_label(img_load2, 180, 145, bg_color='#9999FF')
    l2 = create_image_label(img_load1, 200, 145, bg_color='#9999FF')
    l3 = create_image_label(img_load2, 220, 145, bg_color='#9999FF')
    l4 = create_image_label(img_load2, 240, 145, bg_color='#9999FF')
    l5 = create_image_label(img_load2, 260, 145, bg_color='#9999FF')

    w.update_idletasks()
    time.sleep(0.5)

    l1 = create_image_label(img_load2, 180, 145, bg_color='#9999FF')     
    l2 = create_image_label(img_load2, 200, 145, bg_color='#9999FF')
    l3 = create_image_label(img_load1, 220, 145, bg_color='#9999FF')
    l4 = create_image_label(img_load2, 240, 145, bg_color='#9999FF')
    l5 = create_image_label(img_load2, 260, 145, bg_color='#9999FF')

    w.update_idletasks()
    time.sleep(0.5)

    l1 = create_image_label(img_load2, 180, 145, bg_color='#9999FF')
    l2 = create_image_label(img_load2, 200, 145, bg_color='#9999FF')
    l3 = create_image_label(img_load2, 220, 145, bg_color='#9999FF')
    l4 = create_image_label(img_load1, 240, 145, bg_color='#9999FF')
    l5 = create_image_label(img_load2, 260, 145, bg_color='#9999FF')

    w.update_idletasks()
    time.sleep(0.5)

    
    l1 = create_image_label(img_load2, 180, 145, bg_color='#9999FF')
    l2 = create_image_label(img_load2, 200, 145, bg_color='#9999FF')
    l3 = create_image_label(img_load2, 220, 145, bg_color='#9999FF')
    l4 = create_image_label(img_load2, 240, 145, bg_color='#9999FF')
    l5 = create_image_label(img_load1, 260, 145, bg_color='#9999FF')

    w.update_idletasks()
    time.sleep(0.5)

    # Destroy all labels to avoid memory leaks
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()

    # Open the login page after animation
    w.destroy()
    page()

# Start the animation
animate()

# Keep the window running
w.mainloop()