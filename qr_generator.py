#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox
import pyqrcode

# Initialize the main window
ws = Tk()
ws.title("QR Code Generator")
ws.config(bg='#D2F2F2')

# Function to center the window on the screen
def center_window(window):
    window.update_idletasks()  # Ensure the window size is calculated
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 500  # Set a larger window width
    window_height = 500  # Set a larger window height
    
    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    # Set the window's position and size
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Function to preprocess user input by adding a prefix and postfix when needed
def preprocess_input(input_string):
    # Define common prefixes and postfixes
    common_prefixes = ["http://", "https://", "www."]
    common_postfixes = [".com", ".net", ".org", ".edu", ".in", ".co", ".io"]
    
    # Check for the presence of a common prefix
    has_prefix = any(input_string.startswith(prefix) for prefix in common_prefixes)
    # Check for the presence of a common postfix
    has_postfix = any(input_string.endswith(postfix) for postfix in common_postfixes)
    
    # Add "www." prefix if not present and none of the common prefixes found
    if not has_prefix:
        input_string = "www." + input_string
        
    # Add ".com" postfix if not present and none of the common postfixes found
    if not has_postfix:
        input_string += ".com"
        
    return input_string

# Function to generate QR code
def generate_qr(preprocessed=True):
    input_string = user_input.get()
    if len(input_string) != 0:
        # Preprocess the input string if preprocessed is True
        if preprocessed:
            input_string = preprocess_input(input_string)
        
        global qr, img
        qr = pyqrcode.create(input_string)
        qr_xbm = qr.xbm(scale=5)  # Adjust the scale as needed
        img = BitmapImage(data=qr_xbm)
        display_code(input_string)
    else:
        # Display warning message centered on the screen
        ws.update_idletasks()  # Ensure the window is updated
        messagebox.showwarning('Warning', 'Enter a Valid String!', parent=ws)

# Function to display the QR code
def display_code(input_string):
    img_lbl.config(image=img)
    output.config(text=f"Successfully generated the QR code of: {input_string}")

# Label for the input prompt
lbl = Label(ws, text="Enter any string to generate a unique QR code:", bg='#D2F2F2', font=("Arial", 14))
lbl.pack(pady=10)

# Entry for user input
user_input = StringVar()
entry = Entry(ws, textvariable=user_input, font=("Arial", 14), width=35)
entry.pack(padx=20, pady=5)

# Button to generate QR code with prefix and postfix assumptions
button1 = Button(ws, text="Generate QR Code(with Prefix & Postfix)", command=lambda: generate_qr(True), font=("Arial", 14), width=35)
button1.pack(pady=10)

# Button to generate QR code without any prefix and postfix assumptions
button2 = Button(ws, text="Generate QR Code", command=lambda: generate_qr(False), font=("Arial", 14), width=35)
button2.pack(pady=10)

# Label to display the QR code
img_lbl = Label(ws, bg='#D2F2F2')
img_lbl.pack()

# Label to display status messages
output = Label(ws, text="", bg='#D2F2F2', font=("Arial", 12), wraplength=350)
output.pack(pady=10)

# Start the main event loop and center the window
center_window(ws)
ws.mainloop()


# In[ ]:




