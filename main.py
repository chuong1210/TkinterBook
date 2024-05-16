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