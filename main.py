import customtkinter
import os
import tkinter as tk
from tkinter import SUNKEN
from tkinter import filedialog

from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")
WHITE = "#ffffff"
BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
h_size = 600
w_size = 800
global img_path, logo_path, i
size_img_show = 400, 300  #(w_size / 3), (h_size/3)
folder_path = os.path.abspath(os.curdir)


def center_window():
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (w_size / 2)
    y = (screen_height / 2) - (h_size / 2)
    window.geometry('%dx%d+%d+%d' % (w_size, h_size, x, y))


def get_img():
    global img_path, i
    img_path = filedialog.askopenfilename(filetypes=[
        ('image files', '*.png'),
        ('image files', '*.jpg'),
    ])
    img_path_text.delete(0, customtkinter.END)
    img_path_text.insert(0, img_path[len(img_path) - 150:])  #print the last 150 characters of the url
    img = Image.open(img_path)
    img.thumbnail(size_img_show)
    i = ImageTk.PhotoImage(img)
    img_original.create_image(0, 0, image=i, anchor=tk.NW)


def get_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[
        ('image files', '*.png'),
        ('image files', '*.jpg'),
    ])
    logo_path_text.delete(0, customtkinter.END)
    logo_path_text.insert(0, logo_path[len(logo_path) - 150:])


def get_folder():
    global folder_path
    folder_path = ''
    folder_path = filedialog.askdirectory()
    folder_path_text.delete("1.0", tk.END)
    folder_path_text.insert(tk.END, folder_path[len(folder_path) - 150:])


def add_watermark():
    global img_path, logo_path, i
    #todo:check if the paths are selected

    i = Image.open(img_path)
    l = Image.open(logo_path)
    i.paste(l, (size_img_show[0] + 3000,
                size_img_show[1] + 2100))  #todo: I  3000 and 2100 should be a variable to select the corner
    i.save(folder_path + ".jpg")  #todo: use the extenxion from the opened file.
    #todo: Ask if oversave
    i.thumbnail(size_img_show)
    i = ImageTk.PhotoImage(i)
    img_end.create_image(0, 0, image=i, anchor=tk.NW)


#Create windows
window = customtkinter.CTk()  #todo: decoration
window.title("Watermark")
window.config(bg=YELLOW, height=h_size, width=w_size)
center_window()

# Draw Tittle
customtkinter.CTkLabel(window, text="Watermarker", font=(FONT_NAME, 40, 'bold'), fg_color=YELLOW,
                       ).grid(row=0, column=1, columnspan=2)

# Buttons
customtkinter.CTkButton(master=window, text="Get IMG", font=(FONT_NAME, 15, 'bold'),
                        command=lambda: get_img()).grid(row=1, column=0, rowspan=1)

customtkinter.CTkButton(master=window, text="Get LOGO", font=(FONT_NAME, 15, 'bold'),
                        command=lambda: get_logo()).grid(row=2, column=0, rowspan=1)

customtkinter.CTkButton(master=window, text="Save in:", font=(FONT_NAME, 15, 'bold'),
                        command=lambda: get_folder()).grid(row=3, column=0, rowspan=1)

customtkinter.CTkButton(master=window, text="ADD Watermark", font=(FONT_NAME, 15, 'bold'),
                        command=lambda: add_watermark()).grid(row=4, column=1, columnspan=2)
# Locations
img_path_text = customtkinter.CTkEntry(window, height=1, width=600)
img_path_text.grid(row=1, column=1, columnspan=3)

logo_path_text = customtkinter.CTkEntry(window, height=1, width=600)
logo_path_text.grid(row=2, column=1, columnspan=3)

folder_path_text = customtkinter.CTkEntry(window, height=1, width=600)
folder_path_text.insert(tk.END, folder_path[len(folder_path) - 150:])
folder_path_text.grid(row=3, column=1, columnspan=3)

#Background set
# img = tk.PhotoImage(file="wallpaper.png")
# canvas.create_image(w_size, h_size, image=img)

#imgs places
img_original = tk.Canvas(window, width=size_img_show[0], height=size_img_show[1])
img_original.grid(row=5, column=0, columnspan=2)

img_end = tk.Canvas(window, width=size_img_show[0], height=size_img_show[1], relief=SUNKEN)
img_end.grid(row=5, column=2, columnspan=2)

#todo: close the program nicely
window.mainloop()
