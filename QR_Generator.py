import qrcode
import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label, Button

# Create a QR Code
qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://www.linkedin.com/in/shahirbilagi43")
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

# Convert the PIL image to a NumPy array with uint8 type
img = np.array(img.convert("L"), dtype=np.uint8)  # Convert to grayscale ("L" mode)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)  # Convert to RGB for tkinter compatibility

# Create a Tkinter window
root = tk.Tk()
root.title("QR Code Viewer")

# Function to open the URL
def open_url():
    import webbrowser
    webbrowser.open("https://www.linkedin.com/in/shahirbilagi43")

# Create a Tkinter-compatible photo image
img_pil = Image.fromarray(img)
img_tk = ImageTk.PhotoImage(img_pil)

# Create a label to display the QR code
label = Label(root, image=img_tk)
label.pack()

# Create a button to open the URL
button = Button(root, text="Open Link", command=open_url)
button.pack()

# Start the Tkinter event loop
root.mainloop()
