from tkinter import *
from utils.attributes import *


def get_label(parent, text, optional=True):
	label_frame = Frame(parent, bg=attr_bg2)
	Label(label_frame, text=text, bg=attr_bg2).pack(side="left")
	if not optional:
		Label(label_frame, text='*', bg=attr_bg2, fg="#F00").pack(side="left")
	return label_frame


def get_entry_frame(parent, hide=False):
	entry_frame = Frame(
		parent,
		bg=attr_entry_bg,
		highlightthickness=1,
		highlightbackground=attr_entry_bd_bg,
		highlightcolor=attr_entry_bd_bg,
		padx=5,
		pady=5,
	)
	if not hide:
		entry = Entry(entry_frame, bg=attr_entry_bg, bd=0)
	else:
		entry = Entry(entry_frame, bg=attr_entry_bg, bd=0, show="*")
	entry.pack(fill="x")
	return {'entry_frame': entry_frame, 'entry': entry}


def get_btn(parent, text):
	btn = Button(
		parent,
		text=text,
		bg=attr_btn_bg,
		activebackground=attr_btn_hover_bg,
		bd=0,
		padx=10
	)
	btn.bind("<Enter>", lambda e: e.widget.config(bg=attr_btn_hover_bg))
	btn.bind("<Leave>", lambda e: e.widget.config(bg=attr_btn_bg))
	return btn


def get_submit_btn(parent, text):
	btn = Button(
		parent,
		text=text,
		bg=attr_submit_btn_bg,
		activebackground=attr_submit_btn_hover_bg,
		fg=attr_submit_btn_fg,
		activeforeground=attr_submit_btn_hover_fg,
		bd=0,
		padx=15,
		pady=5
	)
	btn.bind("<Enter>", lambda e: e.widget.config(bg=attr_submit_btn_hover_bg))
	btn.bind("<Leave>", lambda e: e.widget.config(bg=attr_submit_btn_bg))
	return btn
