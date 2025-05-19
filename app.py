from tkinter import *
from utils import colours, button_attributes

root = Tk()
root.title("Zip Handling")
root.state("zoomed")


def on_enter(e):
	e.widget.config(bg=colours.btn_grp_hover_bg)


def on_leave(e, active_btn):
	e.widget.config(bg=colours.btn_grp_bg)
	if active_btn[0] is not None:
		active_btn[0].config(bg=colours.btn_active_bg)


def btn_on_click(active_btn, btn):
	if active_btn[0] is not None:
		active_btn[0].config(bg=colours.btn_grp_bg)
	btn.config(bg=colours.btn_active_bg)
	active_btn[0] = btn


left_frame = Frame(root, bg=colours.bg1)
left_frame.place(x=0, y=0, width=200, relheight=1)

right_frame = Frame(root, bg=colours.bg2)
right_frame.place(x=200, y=0, relwidth=1, relheight=1)

last_clicked_btn = [None]

add_btn = Button(left_frame, text="Add",
				bg=colours.btn_grp_bg, activebackground=colours.btn_grp_hover_bg,
				bd=button_attributes.bd, pady=button_attributes.pady,
				command=lambda: btn_on_click(last_clicked_btn, add_btn))
add_btn.grid(row=0, column=0, sticky=button_attributes.sticky)
add_btn.bind("<Enter>", on_enter)
add_btn.bind("<Leave>", lambda e: on_leave(e, last_clicked_btn))

merge_btn = Button(left_frame, text="Merge",
				bg=colours.btn_grp_bg, activebackground=colours.btn_grp_hover_bg,
				bd=button_attributes.bd, pady=button_attributes.pady,
				command=lambda: btn_on_click(last_clicked_btn, merge_btn))
merge_btn.grid(row=1, column=0, sticky=button_attributes.sticky)
merge_btn.bind("<Enter>", on_enter)
merge_btn.bind("<Leave>", lambda e: on_leave(e, last_clicked_btn))

left_frame.grid_columnconfigure(0, weight=1)

Label(right_frame, text="Click").pack()

root.mainloop()
