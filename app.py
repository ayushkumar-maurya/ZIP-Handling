from tkinter import *

root = Tk()
root.title("Zip Handling")
root.state("zoomed")


def on_enter(e):
	e.widget.config(bg="#BFBFBF")


def on_leave(e, active_btn):
	e.widget.config(bg="#D9D9D9")
	if active_btn[0] is not None:
		active_btn[0].config(bg="#F2F2F2")


def btn_on_click(active_btn, btn):
	if active_btn[0] is not None:
		active_btn[0].config(bg="#D9D9D9")
	btn.config(bg="#F2F2F2")
	active_btn[0] = btn


left_frame = Frame(root, bg="#D9D9D9")
left_frame.place(x=0, y=0, width=200, relheight=1)

right_frame = Frame(root, bg="#F2F2F2")
right_frame.place(x=200, y=0, relwidth=1, relheight=1)

last_clicked_btn = [None]

add_btn = Button(left_frame, text="Add",
				bg="#D9D9D9", activebackground="#BFBFBF",
				bd=0, pady=5,
				command=lambda: btn_on_click(last_clicked_btn, add_btn))
add_btn.grid(row=0, column=0, sticky="ew")
add_btn.bind("<Enter>", on_enter)
add_btn.bind("<Leave>", lambda e: on_leave(e, last_clicked_btn))

merge_btn = Button(left_frame, text="Merge",
				bg="#D9D9D9", activebackground="#BFBFBF",
				bd=0, pady=5,
				command=lambda: btn_on_click(last_clicked_btn, merge_btn))
merge_btn.grid(row=1, column=0, sticky="ew")
merge_btn.bind("<Enter>", on_enter)
merge_btn.bind("<Leave>", lambda e: on_leave(e, last_clicked_btn))

left_frame.grid_columnconfigure(0, weight=1)

Label(right_frame, text="Click").pack()

root.mainloop()
