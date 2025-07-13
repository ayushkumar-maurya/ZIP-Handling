import os
from tkinter import *
from tkinter import ttk
from config import APP_NAME, APP_PATH
from logo import APP_ICON
import home
from features import create_feature, extract_feature, add_feature, merge_feature


def on_menu_btn_enter(e):
	e.widget.config(bg=attr_btn_hover_bg)


def on_menu_btn_leave(e):
	e.widget.config(bg=attr_btn_bg)
	if active_btn[0] is not None:
		active_btn[0].config(bg=attr_btn_active_bg)


def on_menu_btn_click(btn):
	if active_btn[0] is not None:
		active_btn[0].config(bg=attr_btn_bg)
	active_btn[0] = btn
	active_btn[0].config(bg=attr_btn_active_bg)

	show_progress_bar(False)

	root.title('{} - {}'.format(APP_NAME, btn['text']))

	for widget in feature_frame.winfo_children():
		widget.destroy()
	feature_frame.grid_rowconfigure(0, weight=0)
	feature_frame.grid_columnconfigure(0, weight=0)

	if btn['text'] == 'Home':
		home.main(feature_frame)
	elif btn['text'] == 'Create':
		create_feature.main(feature_frame, show_progress_bar)
	elif btn['text'] == 'Extract':
		extract_feature.main(feature_frame, show_progress_bar)
	elif btn['text'] == 'Add':
		add_feature.main(feature_frame, show_progress_bar)
	elif btn['text'] == 'Merge':
		merge_feature.main(feature_frame, show_progress_bar)


def create_menu_btns():
	btns = []
	btns_text = ['Home', 'Create', 'Extract', 'Add', 'Merge']

	for i in range(len(btns_text)):
		btn = Button(
			menu_frame,
			text=btns_text[i],
			bg=attr_btn_bg,
			activebackground=attr_btn_hover_bg,
			bd=0,
			anchor="w",
			padx=10,
			pady=7
		)

		btn.config(command=lambda b=btn: on_menu_btn_click(b))
		btn.bind("<Enter>", on_menu_btn_enter)
		btn.bind("<Leave>", on_menu_btn_leave)
		btn.grid(row=i, column=0, sticky="ew")
		btns.append(btn)
	menu_frame.grid_columnconfigure(0, weight=1)

	return {'btns': btns, 'btn_count': len(btns_text)}


def show_progress_bar(show=True):
	if show:
		progress.grid(row=menu_btn_count, column=0, pady=(15, 1), sticky="sew")
	else:
		progress.grid_forget()


# Attributes
'''---------------------------------'''
attr_bg1 = '#D9D9D9'
attr_bg2 = '#F2F2F2'
attr_btn_bg = attr_bg1
attr_btn_hover_bg = '#BFBFBF'
attr_btn_active_bg = attr_bg2
'''---------------------------------'''


# Creating project directory.
os.makedirs(APP_PATH, exist_ok=True)

root = Tk()
root.title(APP_NAME)
root.state("zoomed")
root.iconphoto(True, PhotoImage(data=APP_ICON))

active_btn = [None]

menu_frame = Frame(root, bg=attr_bg1)
menu_frame.place(x=0, y=0, width=200, relheight=1)

feature_frame = Frame(root, bg=attr_bg2, padx=10, pady=10)
feature_frame.place(x=200, y=0, width=root.winfo_screenwidth()-200, relheight=1)

menu_btns, menu_btn_count = create_menu_btns().values()

progress = ttk.Progressbar(menu_frame, orient="horizontal", mode="indeterminate")
progress.start(10)

menu_frame.grid_rowconfigure(menu_btn_count, weight=1)

menu_btns[0].invoke()

root.mainloop()
