import pyperclip
import pyshorteners
import tkinter as tk

root = tk.Tk()

# set the geometry
root.geometry("400x200")

# give a title
root.title("URL Shortener")

# set a background color
root.configure(bg="#49A")

# take 2 string variables to keep the long and short URL
url = tk.StringVar()
url_address = tk.StringVar()

# define 2 functions for shortening URL and copying the URL
def url_shortener():
    url_address.set(pyshorteners.Shortener().tinyurl.short(url.get()))

def copy_url():
    url_short = url_address.get()
    pyperclip.copy(url_short)

tk.Label(root, text="My URL Shortener", font="poppins").pack(pady=10)
tk.Entry(root, textvariable=url).pack(pady=5)
tk.Button(root, text="Generate Short URL", command=url_shortener).pack(pady=7)
tk.Entry(root, textvariable=url_address).pack(pady=5)
tk.Button(root, text="Copy URL", command=copy_url).pack(pady=5)

root.mainloop()
