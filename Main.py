import qrcode
from tkinter import *
from tkinter import messagebox

def generate_qr():
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("user_qr.png")
        messagebox.showinfo("Success", "QR Code saved as user_qr.png")
    else:
        messagebox.showwarning("Input Required", "Please enter a URL")

# GUI Setup
root = Tk()
root.title("QR Code Generator")
root.geometry("300x150")

Label(root, text="Enter URL:").pack(pady=5)
url_entry = Entry(root, width=40)
url_entry.pack(pady=5)

Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

root.mainloop()
