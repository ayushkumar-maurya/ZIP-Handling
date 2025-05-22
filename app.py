from tkinter import *
from features import add_feature, merge_feature
from utils import colours, button_attributes


def on_menu_btn_enter(e):
	e.widget.config(bg=colours.btn_grp_hover_bg)


def on_menu_btn_leave(e):
	e.widget.config(bg=colours.btn_grp_bg)
	if active_feature['btn'] is not None:
		active_feature['btn'].config(bg=colours.btn_active_bg)


def on_menu_btn_click(btn):
	if active_feature['btn'] is not None:
		active_feature['btn'].config(bg=colours.btn_grp_bg)
	active_feature['btn'] = btn
	active_feature['btn'].config(bg=colours.btn_active_bg)

	if active_feature['frame'] is not None:
		active_feature['frame'].destroy()

	if btn['text'] == 'Add':
		active_feature['frame'] = add_feature(root)
	elif btn['text'] == 'Merge':
		active_feature['frame'] = merge_feature(root)


root = Tk()
root.title("Zip Handling")
root.state("zoomed")

active_feature = {'btn': None, 'frame': None}

menu_frame = Frame(root, bg=colours.bg1)
menu_frame.place(x=0, y=0, width=200, relheight=1)

add_menu_btn = Button(menu_frame, text="Add",
				bg=colours.btn_grp_bg, activebackground=colours.btn_grp_hover_bg,
				bd=button_attributes.bd, anchor=button_attributes.anchor,
				padx=button_attributes.padx, pady=button_attributes.pady,
				command=lambda: on_menu_btn_click(add_menu_btn))

add_menu_btn.grid(row=0, column=0, sticky=button_attributes.sticky)
add_menu_btn.bind("<Enter>", on_menu_btn_enter)
add_menu_btn.bind("<Leave>", lambda e: on_menu_btn_leave(e))

merge_menu_btn = Button(menu_frame, text="Merge",
				bg=colours.btn_grp_bg, activebackground=colours.btn_grp_hover_bg,
				bd=button_attributes.bd, anchor=button_attributes.anchor,
				padx=button_attributes.padx, pady=button_attributes.pady,
				command=lambda: on_menu_btn_click(merge_menu_btn))

merge_menu_btn.grid(row=2, column=0, sticky=button_attributes.sticky)
merge_menu_btn.bind("<Enter>", on_menu_btn_enter)
merge_menu_btn.bind("<Leave>", lambda e: on_menu_btn_leave(e))

menu_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
