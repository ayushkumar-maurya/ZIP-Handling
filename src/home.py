from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
from logo import APP_LOGO


def main(parent):
	# Home Content
	content_frame = Frame(parent)
	content_frame.grid(row=0, column=0, sticky="ew")

	app_logo_img = Image.open(BytesIO(APP_LOGO))
	app_logo_img = app_logo_img.resize((150, 150))
	app_logo_img_tk = ImageTk.PhotoImage(app_logo_img)
	app_logo_label = Label(content_frame, image=app_logo_img_tk)
	app_logo_label.image = app_logo_img_tk
	app_logo_label.pack()

	Label(content_frame, text=app_desc1).pack(fill="x", pady=(30, 0))
	Label(content_frame, text=app_desc2).pack(fill="x", pady=(60, 0))

	# Footer
	footer_frame = Frame(parent)
	footer_frame.grid(row=1, column=0, pady=(10, 0), sticky="ew")
	Label(footer_frame, text="Developed by Ayushkumar Maurya").pack()

	parent.grid_rowconfigure(0, weight=1)
	parent.grid_columnconfigure(0, weight=1)


app_desc1 = "Create a new ZIP archive\n\n"
app_desc1 += "Extract all files from an existing ZIP\n\n"
app_desc1 += "Add new files to an existing ZIP archive\n\n"
app_desc1 += "Merge two existing ZIP archives into one"

app_desc2 = "All the features listed above are fully compatible with encrypted ZIP files\n"
app_desc2 += "The resultant archive will have all included files encrypted for secure storage and transfer"
