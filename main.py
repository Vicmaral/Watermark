import tkinter as tk
from tkinter import ttk, SUNKEN
from tkinter import filedialog
from PIL import Image, ImageTk

WHITE = "#ffffff"
BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
h_size = 600
w_size = 1000
global i

def center_window():
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (w_size / 2)
    y = (screen_height / 2) - (h_size / 2)
    window.geometry('%dx%d+%d+%d' % (w_size, h_size, x, y))


def apply_watermark():
    return


def get_img():
    global i
    img_path = filedialog.askopenfilename(filetypes=[
        ('image files', '*.png'),
        ('image files', '*.jpg'),
    ])
    img_path_text.insert(tk.END, img_path[len(img_path) - 150:])  #print the last 150 characters of the url
    im=Image.open(img_path)
    im.grid()
    # i = ImageTk.PhotoImage(Image.open(img_path))
    # img_original.pack()
    # img_original.create_image(0, 0, image=i, anchor=tk.NW)


def get_logo():
    logo_path = filedialog.askopenfile(mode='r', filetypes=[
        ('image files', '*.png'),
        ('image files', '*.jpg'),
    ])
    logo_path_text.insert(tk.END, logo_path.name[len(logo_path.name) - 150:])


def get_folder():
    folder_path = filedialog.askdirectory()
    folder_path_text.insert(tk.END, folder_path[len(folder_path) - 150:])


#Create windows
window = tk.Tk()
tk.Tk().withdraw()
window.title("Watermark")
window.config(bg=YELLOW, height=h_size, width=w_size)
center_window()

#Background set
# img = tk.PhotoImage(file="wallpaper.png")
# canvas.create_image(w_size, h_size, image=img)

#Draw Tittle
tk.Label(window, text="Watermark", font=(FONT_NAME, 30, 'bold'),
         bg=GREEN).grid(row=0, column=1, columnspan=2)

#Buttons
tk.Button(text="Get IMG", font=(FONT_NAME, 10, 'bold'), padx=1, pady=1,
          command=lambda: get_img()).grid(row=1, column=0, rowspan=1)

tk.Button(text="Get LOGO", font=(FONT_NAME, 10, 'bold'), padx=1, pady=1,
          command=lambda: get_logo()).grid(row=2, column=0, rowspan=1)

tk.Button(text="Choose save folder", font=(FONT_NAME, 10, 'bold'), padx=1, pady=1,
          command=lambda: get_folder()).grid(row=3, column=0, rowspan=1)
#Locations
img_path_text = tk.Text(window, height=1, width=100)
img_path_text.grid(row=1, column=1, columnspan=3)

logo_path_text = tk.Text(window, height=1, width=100)
logo_path_text.grid(row=2, column=1, columnspan=3)

folder_path_text = tk.Text(window, height=1, width=100)
folder_path_text.grid(row=3, column=1, columnspan=3)

#imgs places
img_original = tk.Canvas(window, width=w_size/3, height=h_size/3)
img_original.grid(row=5, column=0, columnspan=2)

img_end = tk.Canvas(window, width=w_size/3, height=h_size/3, relief=SUNKEN)
img_end.grid(row=5, column=2, columnspan=2)

window.mainloop()
