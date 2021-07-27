import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import nomorobo_scraper
import threading

    
main_window = tk.Tk()
main_window.title("Nomorobo_scraper_V1.1.2")
main_window.geometry('330x80')
btn = Button(main_window, text="Start Scraping", fg="green",command= lambda: async_threading(number_of_pages(dropdown)))

#check the amount of pages that was selected to be searched
def number_of_pages(dropdown):
    pages_to_search = int(dropdown.get())
    return(pages_to_search)

#use multithreading even though it doesn't work
def async_threading(pages_to_search):
    main_window.destroy()
    thread = threading.Thread(target=nomorobo_scraper.othermain(pages_to_search))
    thread.daemon = True
    thread.start()

irt = tk.Label(text="Amount of pages to search: ")

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
clicked = StringVar()
clicked.set(options[0])

#dropdown menu
dropdown = Combobox(main_window, textvariable = clicked, values = options)

pages_to_search = int(dropdown.get())

#render all elements on the desired placing
irt.place(x = 1, y = 1)
dropdown.place(x = 175, y = 1)
btn.place(x = 140, y = 50)

main_window.mainloop()

