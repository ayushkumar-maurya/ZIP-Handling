import os
from tkinter import filedialog
from tkinter import messagebox
from utils.common_feature_items import *
from utils.zip_handler import ZipHandler


def dir_input(dir_entry):
	dir_path = filedialog.askdirectory()
	dir_entry.delete(0, END)
	dir_entry.insert(0, dir_path)


def validate_and_get_inputs(entries):
	res = {'inputs': None, 'error': None}

	src_dir = entries['src_dir'].get()
	pwd = entries['pwd'].get()
	save_loc = entries['save_loc'].get()

	src_dir = src_dir.strip()
	if not os.path.isdir(src_dir):
		res['error'] = "Please mention valid folder location to create zip."
		return res

	save_loc = save_loc.strip()
	if not os.path.isdir(save_loc):
		res['error'] = "Please mention valid location to save zip."
		return res
	dest_zip = os.path.join(save_loc, "{}.zip".format(os.path.basename(os.path.normpath(src_dir))))

	res['inputs'] = {
		'src_dir': src_dir,
		'pwd': pwd,
		'dest_zip': dest_zip
	}

	return res


def perform_create_operation(entries, show_progress_bar):
	show_progress_bar()
	inputs, error = validate_and_get_inputs(entries).values()
	if error:
		messagebox.showerror("Invalid Input", error)
	else:
		zip_handler = ZipHandler()
		zip_handler.create_zip(**inputs)
		messagebox.showinfo(
			"Zip created successfully.",
			"Zip created successfully. Name: {}".format(os.path.basename(inputs['dest_zip']))
		)
	show_progress_bar(False)


def main(parent, show_progress_bar):
	entries = {}

	# Creating required Widgets.
	get_label(parent, "Select folder to create zip", False).grid(row=0, column=0, sticky="ew")
	src_dir_entry_frame, entries['src_dir'] = get_entry_frame(parent).values()
	src_dir_entry_frame.grid(row=1, column=0, pady=attr_row_margin, sticky="ew")
	src_dir_browse_btn = get_btn(parent, "Browse")
	src_dir_browse_btn.grid(row=1, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	get_label(parent, "Password").grid(row=2, column=0, sticky="ew")
	pwd_entry_frame, entries['pwd'] = get_entry_frame(parent, True).values()
	pwd_entry_frame.grid(row=3, column=0, pady=attr_row_margin, sticky="ew")

	get_label(parent, "Save zip at", False).grid(row=4, column=0, sticky="ew")
	save_loc_entry_frame, entries['save_loc'] = get_entry_frame(parent).values()
	save_loc_entry_frame.grid(row=5, column=0, pady=attr_row_margin, sticky="ew")
	save_loc_browse_btn = get_btn(parent, "Browse")
	save_loc_browse_btn.grid(row=5, column=1, padx=attr_col_margin, pady=attr_row_margin, sticky="ns")

	create_btn = get_submit_btn(parent, "Create")
	create_btn.grid(row=6, column=0, pady=15, sticky="w")

	parent.grid_columnconfigure(0, weight=1)

	# Configuring buttons command
	src_dir_browse_btn.config(command=lambda: dir_input(entries['src_dir']))
	save_loc_browse_btn.config(command=lambda: dir_input(entries['save_loc']))
	create_btn.config(command=lambda: perform_create_operation(entries, show_progress_bar))
